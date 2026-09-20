# UW2 FM Towns: the original symbol names

The Japanese FM Towns release of Ultima Underworld II carries a 32 bit build of the game that was **linked with its symbol table left in**. It names 3237 things, functions and globals both, with the names the original developers used.

This folder holds the extracted symbol list, the tooling to regenerate it from the disc, and notes on how to map those names onto the DOS disassembly in this repository.

## What is on the disc

`/UW2.EXP` is a [Phar Lap 386|DOS-Extender](https://en.wikipedia.org/wiki/Phar_Lap_(company)) `P3` flat model 32 bit x86 executable, run by the `RUN386.EXE` that sits beside it. It is a genuine recompile of the same source, not an emulation layer: the header declares `reloc size 0` and `seginfo size 0`, so unlike DOS `UW2.EXE` there are **no overlays and no segment relocation**. Everything lives in one flat address space.

The data files are almost all the DOS ones. Of 69 files in `/DATA`, **63 are byte identical to the GOG release**, including `OBJECTS.DAT`, `COMOBJ.DAT`, `CMB.DAT`, `TERRAIN.DAT`, `SKILLS.DAT`, `PALS.DAT`, `PLAYER.DAT`, `SCD.ARK`, `T64.TR` and all six `.SYS` fonts. Only `CONTROLS.DAT` and `LEV.ARK` differ, and four files are new (`JCNV.ARK`, `JSTRINGS.PAK`, `BABGLOBJ.DAT`, `PALS.16`), all Japanese text or FM Towns colour depth. So this build reads the same data the DOS one does.

## Why the addresses look wrong at first

**The load image is compressed.** Symbol offsets index the *unpacked* image, so no fixed delta will ever line them up against the file, and trying to fit one is a dead end. Once the image is unpacked the offsets index it **directly, with no delta at all**.

Header offset `0x72` is the load image flags word, and bit 0 is the packed bit. Offset `0x74` gives the unpacked size, `0x78b10` (494352) against `0x6c96e` (444782) stored. The packing is documented in the 386|LINK Reference Manual, appendix D.3.1: the image is a series of blocks, each a 2 byte count then data. High bit clear means a literal block of `count` bytes. High bit set means a repeat block, where `count & 0x7fff` is how many bytes to produce, followed by a length byte and that many bytes as the string to repeat; a length byte of zero means a single zero byte.

The symbol table is appendix D.5. Segment records carry `ffffffff` then a 4 byte value and are longer than public records, so they have to be parsed separately or the stride desynchronises and the rest of the table turns to noise.

## Confidence

Unpacking produces exactly the 494352 bytes the header states, with zero difference. After that:

* **90.9% of `e8` call targets land exactly on a named symbol.**
* Every game function starts with a textbook prologue, `push ebx / push ecx / push edx / push esi / push ebp / mov ebp,esp / sub esp,N`.
* The C library decodes correctly: `toupper_` is `cmp eax,0x61 / jl / cmp eax,0x7a / jg / sub eax,0x20 / ret`, `abs_` is `test eax,eax / jge / neg eax / ret`, `strlen_` is `repne scasb / not ecx`.

## What is in `uw2_symbols.tsv`

3237 rows of name, offset into the unpacked image, and segment index. 2050 fall in the code band at `0x1234` to `0x61dd5` and 1187 above it are data. Names with a trailing underscore are the Watcom register calling convention decoration; plain names such as `do_uwshade` are assembly labels and are code too, so the underscore is not a reliable code and data test. The top of the code band is C library (`fcloseall_`, `strnicmp_`, `getenv_`), so the game's own code sits below that.

A sample of what is now named, against routines this repository can currently only call things like `seg031_2CFA_D1F`:

* **Critter AI**: `crit_hndlr_walk_`, `crit_hndlr_fly_`, `crit_hndlr_swim_`, `crit_head_for_loc_`, `crit_drunkwalk_`, `crit_mill_`, `crit_guard_`, `crit_offense_`, `crit_offense_find_target_`, `crit_defense_`, `crit_flee_`, `crit_avoid_player_`, `crit_hover_`, `crit_die_`
* **Combat**: `resolve_attack_`, `do_attack_`, `fin_attack_`, `player_attack_`, `player_3dattack_`, `critter_attack_`, `missile_newhit_`, `do_objhit_`, `damage_critter_`, `damage_object_`, `DetermineBetterHit_`
* **Physics**: `bounce_obj_`, `do_2dbounce_`, `do_zbounce_`, `phys_bounce_up_`, `do_that_jump_kinda_thing_`, `BlockingTerrain_`, `BridgeHeight_`, `get_terrain_`
* **Inventory**: `AddToInventory_`, `AddToEmptySlot_`, `AddToOccupiedSlot_`, `CombineObjs_`, `EncumCheck_`, `AskHowMany_`

**The named globals are arguably worth more than the function names.** A function name is a convenience, but a named global turns an opaque instruction into a readable one. `mov cs:seg004_6950, dl` means nothing on its own; knowing that word is `gouraud_base_col` explains the whole routine around it.

## A worked example: model surface colours

The 3D model bytecode carries a shade opcode whose operand has never been fully understood, and the port maps three known values and returns 0 for anything else. The FM Towns handler is called `do_uwshade`, and DOS UW1 has the same routine at `seg004_2BCE`. They correspond instruction for instruction:

| DOS UW1 `seg004_2BCE` | FM Towns `do_uwshade` |
| --- | --- |
| `lodsw` / `mov cx, ax` | `lodsw` / `movsx ecx, ax` |
| `lodsw` / `mov bx, ax` | `lodsw` / `movsx eax, ax` |
| `mov dx, [bx]` | `mov dx, word ptr [eax + 0x6c178]` (`dbase_data`) |
| `mov cs:seg004_6950, dl` | `mov byte ptr [0x6bc74], dl` (`gouraud_base_col`) |
| `mov dx, dseg_5c99_2934` | `mov dx, word ptr [0x6c168]` (`cdist`) |
| `mov di, 1620h` | `mov edi, 0x96542` (`resbuf`) |
| `add al, dl` / `cmp al, 0Eh` / `jbe` / `mov al, 0Eh` | identical, same clamp |

So the operand is **not a small set of special cases**. It is an offset to a word, whose **low byte is the face colour**, and the per vertex shade is that plus a global (`cdist`) clamped to a maximum of 14. Any implementation that treats unlisted operands as a default will paint those faces one flat colour.

## The model interpreter's opcode table

UW's 3D models are not meshes. They are bytecode for a small stack machine, and every opcode dispatches through a jump table. In the FM Towns build that table sits at `0x7628c` in the unpacked image, addressed as `base + opcode * 2` with 4 byte entries, and because this build kept its symbols **every entry points at a named handler**.

`model_opcodes.tsv` is that table read out: 113 opcodes, 100 of them real handlers and 13 pointing at `do_int2`, the invalid-opcode stub. For comparison, `UnderworldGodot`'s `modelloader.cs` names 33, some of them as `M3_UW_FACE_UNK16` and `M3_UW_FACE_UNK40`.

**Three of those 33 names are wrong**, which matters because two of them change behaviour:

| opcode | `modelloader.cs` | actually |
| --- | --- | --- |
| `0x00BC` | `M3_UW_FACE_SHADE` | `do_uwcolv` |
| `0x00BE` | `M3_UW_FACE_TWOSHADES` | `do_movei`, not a colour opcode at all |
| `0x00D4` | `M3_UW_VERTEX_DARK` | `do_uwshade`, the real shade opcode |

### These models are BSP trees

`do_sortnorm` reads six words of plane data, then **two relative offsets to back and front subtrees which it calls recursively**, then continues. `do_sortnorm_x0`, `_y0` and `_z0` read four words and jump into the same tail. `do_sfcal` takes one such offset, and `do_ihcall` another. So a model is a tree, not a flat stream, and a walker that assumes otherwise runs off the rails at the first sort node.

That is what a naive `esi` sum gets wrong, and it is why five lengths in this table had to be read out of the handlers by hand rather than computed:

| opcode | handler | naive | actual | why |
| --- | --- | --- | --- | --- |
| `0x0006` | `do_sortnorm` | 20 | **16** | 6 words of plane data, then two subtree offsets, then `add esi, 4` |
| `0x000c`/`0e`/`10` | `do_sortnorm_x0`/`y0`/`z0` | 16 | **12** | 4 words, then a jump into that same tail |
| `0x0012` | `do_sfcal` | 4 | **2** | one subtree offset, not two |
| `0x0018` | `do_org` | 0 | **12** | uses `lodsd`, three 32 bit reads, not 16 bit |
| `0x0050`/`ba` | `do_ihcall`/`_ind` | 6 | **4** | shared tail reads one offset then `add esi, 2` |

With those corrected, **all 32 UW1 builtin models walk cleanly to their terminator**, up from 12.

### How far to trust each row

The `length_source` column is the point of the table, so it is worth reading before relying on a number:

- **`read + exercised`** (10) and **`read`** (4): the length was read out of the handler's assembly by hand.
- **`exercised`** (26): the opcode appears in the shipped UW1 models and all 32 walk to a terminator. A wrong length desyncs the stream and hits an invalid opcode almost immediately, so these are empirically sound even where the number was not hand derived.
- **`esi-sum only, unverified`** (39): produced by summing `esi` movements in the handler, and **nothing exercises it**. Treat with suspicion. That method silently undercounts any handler that delegates to a helper: `do_defres` advances `esi` inside `modify_mes`, so the sum said 2 where the truth is 8.
- **`unknown`** (21) and **`invalid-opcode stub`** (13): no length derived, or the entry is `do_int2`.

The `uses_in_uw1_models` column counts occurrences across the 32 builtin models, decoded with the corrected lengths.

## Mapping names onto the DOS disassembly

DOS `UW2.EXE` has no symbols, so the two have to be tied together by content. Strings work: the routine that references a given string in DOS is the same routine that references it in FM Towns. The DOS side is text processing over `uw2_asm.asm` because IDA has already labelled the strings and tracked the cross references; the FM Towns side is a search for the string's offset as a 32 bit immediate, then the owning symbol.

`dos_to_fmtowns_anchors.tsv` holds 13 confirmed pairs found this way, including `ErrorCanNoLongerRun_ovr114_D1` = `pfatal_code_`, `CrunchObjectList_seg029_2A8E_1200` = `ObjCrunch_`, `LoadCritterAnimations_ovr117_0` = `preload_cr_`, `InitConversation_ovr103_53C` = `Converse_`.

One of them is an independent check on the method rather than an output of it. The anchor `npc_attitude` pairs FM Towns `do_demand_` with IDA's existing `do_demand_ovr097_13BD`. Somebody had already identified that function by hand and the real symbol agrees exactly, and their callee counts match at 9 and 9.

The anchor set is small because DOS `UW2.EXE` only holds 266 strings, most game text living in `STRINGS.PAK`. The way to get the rest is to propagate outward from the anchors by matching callee sets, which is ordinary binary diffing, rather than to look for more strings.

## The UW1 FM Towns disc

That release is the same Phar Lap flat 32 bit shape, packed, unpacking to 527188 bytes as its header states. **It has no symbol table**: both copies on the disc, `/UW.EXP` and `/UW/UW.EXP`, report symtab offset 0 and size 0, so it was linked without symbols.

The UW2 names still reach it. Both builds come from the same toolchain and share code, so a function unchanged between the games has near identical bytes. Taking each named UW2 function's first 24 bytes, discarding degenerate probes, and keeping only probes occurring exactly once in the UW1 image gives **113 confidently named UW1 functions**, in `uw1_propagated_names.tsv` with both offsets. Among them: `DoWanderingMonsters_`, `CritterLook_`, `ItemWeight_`, `delete_trap_`, `is_this_wandering_`, `solve_compass_`, `print_path_to_`, `set_next_square_on_path_`, `deltatotheta_`, `Obj_FreeLinkChain_`, `Obj_FindInMap_`, `get_phys_data_`, `mob_init_`, `mob_to_static_`, `preset_grid_`, `kill_all_effects_`.

113 is a floor rather than a ceiling. It comes from exact byte equality on a short probe, so it only catches functions the compiler emitted identically. Structural matching of the sort BinDiff does would name many more.

## Caveats

**Where FM Towns disagrees with DOS, DOS wins.** This is a 32 bit recompile of the same source, so anything width dependent can differ legitimately: `int` is 32 bits here and 16 bits in the DOS build, so overflow, truncation and shift behaviour are all fair game, and the renderer was reworked for the machine's own video hardware. Treat it as a witness to structure and intent, not to behaviour.

The names are also the developers' names, not documentation. `misc` and `polym` are as unhelpful as anything IDA would invent.

## Tools

Both scripts are plain Python 3 with no dependencies.

```
uw2fmt.py iso    <bin> <out.iso>      extract ISO9660 from a MODE1/2352 disc image
uw2fmt.py unpack <UW2.EXP> <out.bin>  write the unpacked load image
uw2fmt.py syms   <UW2.EXP>            print name, offset, segment
uw2fmt.py at     <UW2.EXP> <name>     hexdump a named function

uwxref.py anchors  <image.bin> <symbols.tsv> <uw2_asm.asm> <UW2.EXE>
uwxref.py graph    <image.bin> <symbols.tsv>    FM Towns call graph
uwxref.py dosgraph <uw2_asm.asm>                DOS call graph
```

The disc image itself is not included here for the obvious reason.
