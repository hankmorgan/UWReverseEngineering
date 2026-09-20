#!/usr/bin/env python3
"""
Cross-reference the DOS UW2 disassembly against the named FM Towns build.

The FM Towns UW2 executable ships a symbol table with the original Looking Glass
function names (see uw2fmt.py). The DOS binary has none, only IDA's guessed
names. Strings present in both binaries anchor one to the other: a routine that
references a given string in DOS is the same routine that references it in FM Towns.

Validated on 2026-09-20: the anchor `npc_attitude` pairs FM Towns `do_demand_` with
IDA's `do_demand_ovr097_13BD`, an exact independent agreement, and their callee
counts match at 9 and 9.

Usage:
    python3 uwxref.py anchors <uw2fmt_image.bin> <symbols.tsv> <uw2_asm.asm> <UW2.EXE>
    python3 uwxref.py graph   <uw2fmt_image.bin> <symbols.tsv>     FM Towns call graph
    python3 uwxref.py dosgraph <uw2_asm.asm>                        DOS call graph
"""
import sys, os, re, struct, io, bisect, collections


def load_syms(path):
    s = []
    for line in open(path):
        p = line.rstrip('\n').split('\t')
        if len(p) == 3 and p[2] == '1':
            s.append((int(p[1], 16), p[0]))
    s.sort()
    return s


def owner_fn(syms):
    addrs = [a for a, _ in syms]
    def owner(off):
        i = bisect.bisect_right(addrs, off) - 1
        return syms[i][1] if i >= 0 else None
    return owner


def fmt_call_graph(img, syms):
    """Call edges from e8 rel32, attributed to the enclosing symbol."""
    owner = owner_fn(syms)
    g = collections.defaultdict(set)
    p = 0
    while p < len(img) - 5:
        if img[p] == 0xe8:
            t = p + 5 + struct.unpack_from('<i', img, p + 1)[0]
            if 0 <= t < len(img):
                c, ce = owner(p), owner(t)
                if c and ce and c != ce:
                    g[c].add(ce)
        p += 1
    return g


def dos_call_graph(asmpath):
    """Call edges parsed out of the IDA listing, attributed to the enclosing proc."""
    g = collections.defaultdict(set)
    cur = None
    for l in io.open(asmpath, encoding='latin-1'):
        if ' proc ' in l:
            cur = l.split()[0]
        elif cur and re.match(r'\s*call\s', l):
            m = re.search(r'call\s+(?:near ptr |far ptr )?([A-Za-z_][A-Za-z0-9_]*)', l)
            if m and m.group(1) != cur:
                g[cur].add(m.group(1))
    return g


def shared_strings(img, dos, minlen=10):
    def S(d):
        return set(m.group().decode('latin-1')
                   for m in re.finditer(rb'[\x20-\x7e]{%d,}' % minlen, d))
    out = S(img) & S(dos)
    # drop gradient/ramp tables, which share long runs by coincidence
    return [s for s in out
            if re.search(r'[A-Za-z]{4}', s) and not re.search(r"(.)\1{5,}|<=>\?<=>\?", s)]


def anchors(img, syms, asmpath, dospath):
    owner = owner_fn(syms)
    asm = io.open(asmpath, encoding='latin-1').read().split('\n')
    dos = open(dospath, 'rb').read()
    for s in sorted(shared_strings(img, dos), key=len, reverse=True):
        probe = s[:24]
        si = img.find(probe.encode('latin-1'))
        if si < 0:
            continue
        pat = struct.pack('<I', si)
        refs, start = [], 0
        while True:
            j = img.find(pat, start)
            if j < 0:
                break
            refs.append(j); start = j + 1
        fmt = sorted({owner(r) for r in refs if owner(r)})
        dosprocs = set()
        for i, l in enumerate(asm):
            if probe[:20] in l and 'db ' in l:
                m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s', l)
                if m:
                    lab = m.group(1)
                    for j, l2 in enumerate(asm):
                        if lab in l2 and j != i and 'db ' not in l2:
                            for k in range(j, -1, -1):
                                if ' proc ' in asm[k]:
                                    dosprocs.add(asm[k].split()[0]); break
                break
        if fmt and dosprocs:
            yield s[:40], fmt, sorted(dosprocs)


def main():
    if len(sys.argv) < 3:
        print(__doc__); return 1
    cmd = sys.argv[1]
    if cmd == 'anchors':
        img = open(sys.argv[2], 'rb').read()
        syms = load_syms(sys.argv[3])
        for s, f, d in anchors(img, syms, sys.argv[4], sys.argv[5]):
            print(f"{s!r}\n    FMT {f}\n    DOS {d}")
    elif cmd == 'graph':
        img = open(sys.argv[2], 'rb').read()
        g = fmt_call_graph(img, load_syms(sys.argv[3]))
        for k in sorted(g):
            print(f"{k}\t{len(g[k])}\t{','.join(sorted(g[k]))}")
    elif cmd == 'dosgraph':
        g = dos_call_graph(sys.argv[2])
        for k in sorted(g):
            print(f"{k}\t{len(g[k])}\t{','.join(sorted(g[k]))}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
