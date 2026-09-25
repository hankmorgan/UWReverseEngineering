#!/usr/bin/env python3
"""
Unpack the FM Towns UW2 executable and read its symbol table.

The FM Towns UW2 disc carries /UW2.EXP, a Phar Lap 386|DOS-Extender
"P3" flat-model 32-bit x86 build. Its load image is COMPRESSED, and it ships a
PubSym symbol table naming 3237 original Looking Glass functions.

Formats are documented in the 386|LINK Reference Manual, Appendix D:
  D.3   .EXP file header          https://archive.org/details/386-link
  D.3.1 packed load image
  D.5   PubSym symbol table

Usage:
    python3 uw2fmt.py iso   <bin> <out.iso>     extract ISO9660 from a MODE1/2352 bin
    python3 uw2fmt.py unpack <UW2.EXP> <out.bin>  write the unpacked load image
    python3 uw2fmt.py syms   <UW2.EXP>            print name<TAB>offset<TAB>segment
    python3 uw2fmt.py at     <UW2.EXP> <name>     hexdump a named function
"""
import struct, sys, os


def iso_from_bin(binpath, outpath):
    """MODE1/2352: 2048 bytes of user data at offset 16 of each 2352 byte sector."""
    n = 0
    with open(binpath, 'rb') as f, open(outpath, 'wb') as g:
        while True:
            s = f.read(2352)
            if len(s) < 2352:
                break
            g.write(s[16:16 + 2048])
            n += 1
    return n


def unpack_image(exp):
    """Return the unpacked load image. Appendix D.3.1.

    Blocks are a 2 byte count then data. High bit clear is a literal block of
    `count` bytes. High bit set is a repeat block: `count & 0x7fff` is the number
    of bytes to produce, then a length byte and that many bytes are the string to
    repeat. A length byte of zero means a single zero byte.
    """
    img_off = struct.unpack_from('<I', exp, 0x26)[0]
    img_size = struct.unpack_from('<I', exp, 0x2a)[0]
    flags = struct.unpack_from('<H', exp, 0x72)[0]
    memreq = struct.unpack_from('<I', exp, 0x74)[0]
    src = exp[img_off:img_off + img_size]
    if not flags & 1:
        return bytes(src)
    out = bytearray()
    i = 0
    while i < len(src) - 1:
        cnt = struct.unpack_from('<H', src, i)[0]
        i += 2
        if cnt & 0x8000:
            n = cnt & 0x7fff
            if i >= len(src):
                break
            slen = src[i]
            i += 1
            if slen == 0:
                out += b'\x00' * n
            else:
                s = src[i:i + slen]
                i += slen
                out += (s * ((n + slen - 1) // slen))[:n]
        else:
            out += src[i:i + cnt]
            i += cnt
    if len(out) != memreq:
        print(f"warning: unpacked {len(out)} but header says {memreq}", file=sys.stderr)
    return bytes(out)


def symbols(exp):
    """Yield (name, offset, segment_index). Appendix D.5.

    Segment entries: name, offset-in-load-image(4), size(4), selector(2), flags(2).
    Public entries:  name, offset-in-segment(4), segment index(2), 1-relative.
    Both FLAT_CODE and FLAT_DATA sit at offset 0, so a symbol offset is an offset
    into the unpacked image directly.
    """
    off = struct.unpack_from('<I', exp, 0x2e)[0]
    size = struct.unpack_from('<I', exp, 0x32)[0]
    sym = exp[off:off + size]
    assert sym[:4] == b'SYM1', sym[:4]
    hdrsize = struct.unpack_from('<H', sym, 4)[0]
    i = hdrsize
    while i < len(sym) - 6:
        n = sym[i]
        if n == 0 or i + 1 + n + 6 > len(sym):
            break
        name = sym[i + 1:i + 1 + n]
        if not all(32 <= c < 127 for c in name):
            break
        p = i + 1 + n
        val = struct.unpack_from('<I', sym, p)[0]
        if sym[p + 4:p + 8] == b'\xff\xff\xff\xff':      # segment entry
            i = p + 12
            continue
        yield name.decode('latin-1'), val, struct.unpack_from('<H', sym, p + 4)[0]
        i = p + 6


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    if cmd == 'iso':
        print(f"{iso_from_bin(sys.argv[2], sys.argv[3])} sectors")
        return 0
    exp = open(sys.argv[2], 'rb').read()
    if cmd == 'unpack':
        img = unpack_image(exp)
        open(sys.argv[3], 'wb').write(img)
        print(f"{len(img)} bytes")
    elif cmd == 'syms':
        for n, a, s in symbols(exp):
            print(f"{n}\t{a:#010x}\t{s}")
    elif cmd == 'at':
        img = unpack_image(exp)
        want = sys.argv[3]
        for n, a, s in symbols(exp):
            if n == want:
                print(f"{n} at {a:#010x} (segment {s})")
                for o in range(a, min(a + 96, len(img)), 16):
                    print(f"  {o:08x}  {img[o:o+16].hex(' ')}")
                return 0
        print(f"no symbol named {want}", file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
