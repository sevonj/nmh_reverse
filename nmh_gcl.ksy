meta:
  id: nmh_gcl
  file-extension: GCL
  encoding: utf-8
  endian: be
doc: |
  FLGC
  No More Heroes World Collisions
  One distance unit appears to be 10m.

seq:
  - id: magic
    contents: "FLCG"
  - contents: [1, 0, 0, 0]
  - contents: [0, 0, 0, 0]
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

  area:
    seq:
      - id: name
        type: strz
        size: 8
      - id: unkf_0
        type: f4
      - id: unk_1
        type: u4
      - contents: [0, 0, 0, 0, 0, 0, 0, 0]
      - id: unk_2
        type: u4
      - id: unk_3
        type: u4
      - id: origin
        type: fl_vector
      - contents: [0, 0, 0, 0]
      - id: unkf_4
        type: f4
      - contents: [0, 0, 0, 0]
      - id: off_data
        type: u4
      - contents: [0, 0, 0, 0]
      - contents: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    instances:
      data:
        io: _root._io
        pos: off_data
        type: area_data

    types:
      area_data:
        seq:
          - id: off_data1
            type: u4
          - id: off_colmesh
            type: u4
          - id: num_data1
            type: u4
          - id: num_col_tris
            type: u4
          - id: unk_vec_a
            type: fl_vector
          - id: unk_vec_b
            type: fl_vector

        instances:
          data1:
            io: _root._io
            pos: off_data1
            type: data1
            repeat: expr
            repeat-expr: num_data1

          col_mesh:
            io: _root._io
            pos: off_colmesh
            type: col_tri
            repeat: expr
            repeat-expr: num_col_tris

        types:
          data1:
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

          col_tri:
            seq:
              - id: unk_1
                type: u4
              - contents: [0, 0, 0, 0]
              - id: unk_3
                type: u4
              - id: v0
                type: fl_vector
              - id: v1
                type: fl_vector
              - id: v2
                type: fl_vector
