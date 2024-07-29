meta:
  id: nmh_gcl
  file-extension: GCL
  encoding: utf-8
  endian: be
doc: |
 No More Heroes World Collision

seq:
  - id: magic
    contents: 'FLCG'
  - contents: [1,0,0,0]
  - contents: [0,0,0,0]
  - id: num_areas
    type: u2
  - id: num_materials
    type: u2
  - id: unk_1
    size: 48
  - id: materials
    type: material
    repeat: expr
    repeat-expr: num_materials
  - id: area_headers
    type: area_header
    repeat: expr
    repeat-expr: num_areas

  - type: align(32)
  - id: areas
    type: area
    repeat: expr
    repeat-expr: num_areas
    
types:
  align:
    doc: |
      Byte alignment
    params:
      - id: size
        type: u4
    seq:
      - size: (size - _io.pos) % size
  fl_vector:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
  material:
    doc: |
      These are probably materials:
      The names are usually nondescriptive, but
      "LAMBERT1" sounds like a material.
    seq:
      - id: name
        type: strz
        size: 8
      - id: unk0
        type: f4
      - size: 20
  area_header:
    seq:
      - id: name
        type: strz
        size: 8
      - size: 72
  area:
    seq:
      - id: unk4
        type: u4
      - id: unk5
        type: u4
      - id: num_unknown1s
        type: u4
      - id: num_unknown2s
        type: u4
      - id: bbox_min
        type: fl_vector
      - id: bbox_max
        type: fl_vector
      - id: unknown1s
        type: area_unknown1
        repeat: expr
        repeat-expr: num_unknown1s
      - id: unknown2s
        type: area_unknown2
        repeat: expr
        repeat-expr: num_unknown2s
  area_unknown1:
    seq:
      - id: unk_0
        type: u4
      - id: unk_1
        type: u4
      - id: unk_2
        type: u4
      - id: unk_3
        type: u4
      - id: unkf_0
        type: f4
      - id: unkf_1
        type: f4
      - id: unkf_2
        type: f4
      - id: unkf_3
        type: f4
  area_unknown2:
    seq:
      - id: unk_1
        type: u4
      - id: unk_2
        type: u4
      - id: unk_3
        type: u4
      - id: v0
        type: fl_vector
      - id: v1
        type: fl_vector
      - id: v2
        type: fl_vector
     