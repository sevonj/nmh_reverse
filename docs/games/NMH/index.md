# NMH

No More Heroes

## File lists
- [RNHE41 (Wii US)](Files RNHE41.md)

## Roadmap

### Asset types

- [ ] [GMF2](/nmh_reverse/formats/gmf2)
    - [ ] Textures
        - [ ] All values (header)
        - [x] Data  
            It's a GCT0 file.
    - [ ] Materials
        - [ ] All values
    - [ ] Objects
        - [ ] Transform
            - [x] Position
            - [ ] Rotation
            - [x] Scale
        - [ ] Geometry
            - [ ] Vertices
                - [x] Common short int format
                    - [x] Vertex scale 
                - [ ] Other formats...
            - [ ] Idx buffers
                - [ ] Common tristrip format
                    - [x] Indices
                    - [ ] UV?
                    - [ ] Normals?
                    - [ ] Remaining data
                - [ ] Other formats...
            - [ ] Bones?
            - [ ] Anims?
        - [x] Culling
        - [x] Hierarchy
        - [x] Unknown references to other objects  
                They're parent/first child/prev/next
        - [ ] data_c buffer
        - [ ] All values
- [ ] [FLCG](/nmh_reverse/formats/flcg)
    - [ ] Materials (what are these dummy materials even used for?)
    - [ ] Models
        - [ ] Linked list
        - [ ] Transform
            - [x] Position
            - [ ] Rotation?
            - [ ] Scale?
        - [ ] Data1
        - [ ] Col Tris
            - [x] Geometry
            - [ ] Linked list?
            - [ ] unk_3
        - [ ] Unknown vectors
- [ ] [GCT0](/nmh_reverse/formats/gct0)
    - [x] Size
    - [x] Encodings 
    - [ ] Convert to png
    - [ ] Convert from png
    - [ ] All header values
- [ ] RMHG
- [ ] RSAR
- [ ] RSTM
- [ ] STMD
- [ ] SEST
- [ ] STSD
- [ ] THP
- [ ] STRIMAG2
- [ ] GAN2