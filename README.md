# UWReverseEngineering
Repository for Reverse Engineering work on UW1/2


UW2.idb is an IDA 5 (Free) decompilation of UW2.exe with some code identified.

Get IDA at https://www.scummvm.org/news/20180331/


See ida.asm for a text version of the disassembly.

Segments are named using the following convention(s)

seg00X_nnnn
where X is the original segment number of the code and nnnn is the offset Dosbox debugger loads the data at.

Overlay segments which are dynamically loaded to different offsets at runtime are not renamed.

Key variables to look at when researching the file:

CurrObj_dseg_2256 is the currently processed game object.
PlayerObject_dseg_828E  is the player object.

the number after dseg_ is the offset for the data. Typically it will be at offset ds:offset
with Dosbox typically loading (for me) the main data segment at base address 67d6