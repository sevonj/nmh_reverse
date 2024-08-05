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
    char zeropad[4];  // Maybe there's some unused value here.
    int len_data;     // Texture data size
    char unk_str[4];  // Unknown string truncated to 4B.
} textureHeader;
```

Texture data itself is just a baked in [GCT0](/nmh_reverse/formats/gct0) file.

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
} materialHeader;

/*
  Material data
  48B
*/
struct {
    char zeropad[8];          //
    int off_texture;          // Texture header
    int unk_3;                // Maybe flags.
    float shaderparams_a[4];  //
    float shaderparams_b[4];  // Often RGBA
} materialData;
```


## Objects
### Hierarchy and linked lists

Objects have hierarchy; some are children of other objects.
Each object knows up to four other objects within the file, as offsets.

:   **off_parent, off_firstchild, off_prev, off_next.**

These are either an object's offset in the file, or zero if there's no object.

Prev/next chain together a linked list of objects that have the same parent. Parent/firstchild is a vertical chain up and down the hierarchy.

### Transform
Objects have position, scale and rotation. Parent's transform naturally affects the children. Position and scale are obvious vectors, but rotation is unclear.

### Geometry


## More

ksy spec for this format: [gmf2.ksy](https://github.com/sevonj/nmh_reverse/blob/master/lib/kaitai_defs/gmf2.ksy)