# GCT0

!!! note inline end ""
    __Games__
    [`NMH`](/nmh_reverse/games/NMH)
    
    __Extensions__
    `.gct`
    `.bin`

    __Tools__  
    [DolphinTextureExtraction-tool](/nmh_reverse/tools/DolphinTextureExtraction-tool)
    [nmh_reverse_scripts](/nmh_reverse/tools/nmh_reverse_scripts)


Grasshopper texture file.

A very simple texture container. Contains a small header and data starting from 0x40.

```cpp
// Header

int32 magic = 'GCT0';
int32 encoding; // See enum Encoding below
int16 w;
int16 h;
// 4-byte null?
int32 unknown; // Flags?

```

```cpp
/*
  Source: https://wiki.tockdom.com/wiki/TEX0_(File_Format)
  This seems to match perfectly with dolphin's texture format overlay.

  It is unclear if all encodings are used.
*/
enum Encoding {
    I4 = 0x00,
    I8 = 0x01,
    IA4 = 0x02,
    IA8 = 0x03,
    RGB565 = 0x04,
    RGB5A3 = 0x05,  // Used
    RGBA32 = 0x06,  // Used
    C4 = 0x08,
    C8 = 0x09,
    C14X2 = 0x0A,
    CMPR = 0x0E     // Used
}; 
```