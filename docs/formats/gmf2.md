# GMF2

!!! note inline end ""
    __Games__
    [`NMH`](/nmh_reverse/games/NMH)
    
    __Extensions__
    `.gm2`

    __Tools__  
    [nmh_reverse_scripts](/nmh_reverse/tools/nmh_reverse_scripts)

Grasshopper model file.

GMF2 Contents:

- Textures
- Materials
- Objects
    - Geometry

The format is _mostly_ little-endian.

The file uses offsets and linked lists for everything, but it's also possible to traverse the file using texture/material/object counts.

## Header
```cpp
// GMF2 header 56B(or more if there are unused values in the following null
// padding) struct GMF2Header {
struct GMF2Header {
  char magic[4];        // 'GMF2'
  int version;          // 2, Probably version.
  char zeropad[16];     //
  short num_objects;    //
  short num_textures;   //
  short num_unused;     //
  short num_materials;  //
  int off_objects;      //
  int off_textures;     // Always 0x70
  int off_unused;       //
  int off_materials;    //
  int unk_0x30;         //
  int unk_0x34;         //
};
```

## Textures
```cpp
/*
  Texture header
  32B
*/
struct {
    char name[8];     // Texture name truncated to 8B.
    int off_prev;     // Previous texture in linked list
    int off_next;     // Next texture in linked list
    int off_data;     // Texture data offset within this file
    int unk_0x14;     // Zero in all world chunks.
    int len_data;     // Texture data size
    char unk_str[4];  // Unknown string truncated to 4B.
} gmf2Texture;
```

Texture data itself is just a [GCT0](/nmh_reverse/formats/gct0) file.

## Materials
```cpp
/*
  Material header
  32B
*/
struct {
    char name[8];     // Material name truncated to 8B.
    int off_prev;     // Previous material in linked list
    int off_next;     // Next material in linked list
    int unk_3;        // Maybe flags.
    int off_data;     // Material data offset
    char zeropad[8];  // 
} gmf2Material;

/*
  Material data
  48B
*/
struct {
    char zeropad[8];          //
    int off_texture;          // Texture header
    int unk_3;                // Maybe flags.
    float shaderparams_a[4];  //
    float shaderparams_b[4];  // RGB(A?) tint
} gmf2MaterialData;
```


## Objects
??? info "World coords"

    The unit of distance in all 3d coordinates are 10m (or very close anyway, I didn't check).  
    Divide them by 10 to get realistic sized models

These seem to be used as bones in characters.

```cpp
// Object header
// 128B
struct GMF2Object {
  char name[8];               // Object name truncated to 8B. Shift JIS
  int flags;                  //
  int off_v_buf;              // Vertex buffer offset.
  int off_parent;             // Parent object
  int off_firstchild;         // Child object
  int off_prev;               // Previous object in linked list
  int off_next;               // Next object in linked list
  int off_surfaces;           //
  int unused;                 // probably unused
  int unk_0x28;               // Zero in all world chunks.
  int v_divisor;              // Exponent of vertex divisor.
  float position[3];          // XYZ coords.
  float unk_0x3c;             // Unused 4th component of previous vector?
  float rotation[3];          // Euler rotation? Quaternion?
  float unk_0x4c;             //
  float scale[3];             // XYZ scale.
  float off_v_format;         // Either 1.0f or an offset to index format.
  float cullbox_position[3];  // XYZ coords.
  float unk_0x6c;             // Unused 4th component of previous vector?
  float cullbox_size[3];      // XYZ size.
  float unk_0x7c;             // Unused 4th component of previous vector?
};
```
### Flags
```cpp
// Very hastily tested. Probably not an exhaustive list.
enum GMF2ObjectFlags {
  VISIBLE = 0x1,                // Hiding an object hides its children too.
  D = 0x8,                      // Makes dark billboarded objects transparent
  BILLBOARD = 0x40,             //
  L = 0x800,                    // Makes billboarded objects dark
  NO_AMBIENT_LIGHT = 0x1000,    // Shadows are pure black
  NO_DIRECT_LIGHT = 0x2000,     //
  DONT_CAST_SHADOW = 0x100000,  //
};
```

### Hierarchy and linked lists

Objects have hierarchy; some are children of other objects.
Each object knows up to four other objects in the file:

:   **parent, firstchild, prev, next.**

These references are either an offset in the file, or zero if there's no object.

Prev/next chain together a linked list of objects that have the same parent. Parent/firstchild is a vertical chain up and down the hierarchy.

### Transform
Objects have position, scale and rotation. Parent's transform naturally affects the children. Position and scale are obvious vectors, but rotation is unclear.

### Geometry
#### Vertex buffer

Vertex buffers appear to only contain position. There's one shared vertex buffer for all surfaces in the model.

```cpp
//  Most models in world use this format. Divide the coords by 2^v_divisor.
//  6B big-endian
int16_t x;
int16_t y;
int16_t z;
```
```cpp
// if v_divisor == -1, the buffer is float vectors instead. Divisor is not used.
// 12B big-endian
float x;
float y;
float z;
```
#### Surfaces

```cpp
// Surface
// 32B
struct GMF2Surface {
  int off_prev;      // Previous surface in linked list
  int off_next;      // Next surface in linked list
  int off_data;      // Surface data
  int off_material;  // Which material to use
  short unk_0x10;    // Corrupting this seems to do nothing.
  short num_v;       // number of vertices in shared vertex buffer
  int unk_0x14;      // Zero in all world chunks
  short unk_0x18;    // Corrupting this crashes the game.
  short unk_0x1a;    // Corrupting this causes transparency glitches.
  short unk_0x1c;    // Corrupting this seems to do nothing.
  short unk_0x1e;    // Corrupting this seems to do nothing.
};
```

```cpp
// Surface data
// big-endian

uint32_t len_data;
uint16_t num_vertices;
int16_t unknown;      // Corrupting this seems to do nothing.
int8_t zeropad[24];
```

##### Triangle strips:

Each surface contains a number of tri-strips. Keep reading them until num_vertices is exhausted.


```cpp
// Triangle strip header
// 4B big-endian, variable size
uint16_t command;  // GPU command?
uint16_t num_v;    // Number of vertices in this strip
```
'command' is always 0x99(?) It's probably a [Wii draw command](https://wiki.tockdom.com/wiki/Wii_Graphics_Code).
 0x98 is (non-indexed) tri-strip, so maybe 0x99 is an indexed tri-strip.

After the header you get vertices, which are all one of these types:

```cpp
// Tristrip vertex type A
// 11B big-endian
uint16_t idx;
int8_t normal_x;
int8_t normal_y;
int8_t normal_z;
uint16_t color; // Unknown how this exactly works.
int16_t u;
int16_t v;
```

```cpp
// Tristrip vertex type B
// 9B big-endian
uint16_t idx;
int8_t normal_x;
int8_t normal_y;
int8_t normal_z;
int16_t u;
int16_t v;
```
Vast majority of NMH open world models use type A. Type B is found occasionally, for example in billboard model in NMH chunk 24 (the one with atm & burger suplex).

It seems that `off_v_format` pointed in the [object](#objects) determines the type.

## More

ksy spec for this format: [gmf2.ksy](https://github.com/sevonj/nmh_reverse/blob/master/lib/kaitai_defs/gmf2.ksy)