# UWReverseEngineering

Repository for Reverse Engineering work on UW1/2

## Introduction

UW.idb and UW2.idb are [IDA Pro 5 (Free)](https://www.scummvm.org/news/20180331/) decompilation database files of UW.exe and UW2.exe with some code identified.

See ida.asm for a text version of the disassembly.

The game mechanics are being documented in `Guide to the Ultima Underworlds.md`.

## Following along

Segments are named using the following convention(s):

1. Code segments `segXXX_nnnn`, where `XXX` is the original segment number of the code and `nnnn` is the offset Dosbox debugger loads the data at. 
2. Overlay segments, labeled `ovrXXXX` are dynamically loaded to different offsets at runtime are not renamed. The only way of breaking into these overlays is by either breaking in a normal segment, or set a breakpoint to a memory address this overlay segment is modifying.
3. Data segments are labeled `XXXX_dseg_nnn`, where `XXXX` is a description and `nnn` is the offset of the data in that specific data segment. Using this config, Dosbox typically loads the main data segment at base address `67d6h`.

For example, if you want to set a breakpoint to `seg040_352B_1AC6`, you have to use the command `bp 352B:1AC6`. Use Dosbox [0.74-3-debug](https://github.com/user-attachments/files/15995150/dosbox-74-3-debug.zip) with [this config file](https://github.com/user-attachments/files/15995208/dosbox-0.74-debug.-.Copy.txt) for reproducible offsets. 

## Other notes

Sometimes, when stepping into a function, the code will switch to INT21, which you should not step over, but into and until it returns to the function.

Key variables to look at when researching the file:

* `CurrObj_dseg_2256` is the currently processed game object.
* `PlayerObject_dseg_828E` is the player object.

IDA Pro 5 can have problems rendering fonts, making the program nigh unusable. Changing the font in the settings can fix this issue.