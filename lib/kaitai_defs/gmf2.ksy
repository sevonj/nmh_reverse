meta:
  id: gmf2
  file-extension: GM2
  encoding: SHIFT-JIS
  endian: be
doc: |
  Grasshopper Manufacture
  No More Heroes world chunk
  GMF - Grasshopper Model File?
  Japanese text encoding.

seq:
  - id: magic
    contents: "GMF2"
  - id: version
    doc: "probably."
    type: u4le
    valid: 2

  # 16B zero
  - contents: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  - id: num_objects
    type: u2le
  - id: num_textures
    type: u2le
  - contents: [0, 0]
  - id: num_materials
    type: u2le
  - id: off_objects
    type: u4le
  - id: off_textures
    type: u4le
  - contents: [0, 0, 0, 0]
  - id: off_materials
    type: u4le
  - id: unk_8
    type: u4le
  - id: unk_9
    type: u4le

  # 56B zeros
  - contents: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  - contents: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  - contents: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  - contents: [0, 0, 0, 0, 0, 0, 0, 0]

  # --- Content Headers

  - id: textures
    type: texture
    repeat: expr
    repeat-expr: num_textures

  - id: materials
    type: material
    repeat: expr
    repeat-expr: num_materials

  - id: world_objects
    type: world_object(_io.pos)
    repeat: expr
    repeat-expr: num_objects

types:
  # --- Common
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
        type: f4le
      - id: y
        type: f4le
      - id: z
        type: f4le

  fl_vector_be:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  fl_vector4:
    seq:
      - id: x
        type: f4le
      - id: y
        type: f4le
      - id: z
        type: f4le
      - id: w
        type: f4le

  short_vector:
    seq:
      - id: x
        type: s2
      - id: y
        type: s2
      - id: z
        type: s2

  # --- Textures

  texture:
    seq:
      - id: name
        type: strz
        size: 8
      - id: off_prev
        type: u4le
      - id: off_next
        type: u4le
      - id: off_data
        type: u4le
      - id: unk_0x14
        type: u4
      - id: size
        type: u4le
      - id: unk_str
        type: strz
        size: 4

    instances:
      data:
        doc: "GHM in-house texture format."
        io: _root._io
        pos: off_data
        size: size

  # --- Materials

  material:
    seq:
      - id: name
        type: strz
        size: 8
      - id: off_prev
        type: u4le
      - id: off_next
        type: u4le
      - id: unk_3
        type: u4le
      - id: off_data
        type: u4le
      - contents: [0, 0, 0, 0]
      - contents: [0, 0, 0, 0]

    instances:
      data:
        io: _root._io
        pos: off_data
        type: material_data

    types:
      material_data:
        seq:
          - contents: [0, 0, 0, 0]
          - contents: [0, 0, 0, 0]

          - id: off_texture
            type: u4le
          - id: unk_3
            doc: "flags?"
            type: u4le
          - id: shaderparams_a
            type: fl_vector4
          - id: shaderparams_b
            doc: "Often RGBA"
            type: fl_vector4

  # --- Objects

  world_object:
    params:
      - id: off
        type: u4
    seq:
      - id: name
        type: strz
        size: 8
      - id: unk_0
        type: u4le
      - id: off_v_buf
        type: u4le
      - id: off_parent
        type: u4le
      - id: off_firstchild
        type: u4le
      - id: off_prev
        type: u4le
      - id: off_next
        type: u4le
      - id: off_surf_list
        type: u4le
      - contents: [0, 0, 0, 0]
      - contents: [0, 0, 0, 0]
      - id: v_scale
        doc: |
          Divide vertex coords by 2^v_scale.
          Parent's v_scale doesn't affect children.
        type: s4le
      - id: origin
        type: fl_vector
      - id: unkf_a
        type: f4le
      - id: unk_b
        type: u4le
      - id: rot_y
        type: f4le
      - id: rot_z
        type: f4le
      - id: unkf_11
        type: f4le
      - id: scale
        type: fl_vector
      - id: off_data_c
        type: u4le
      - id: cullbox_origin
        doc: |
          Appears to be the center of the box, not the start.
        type: fl_vector
      - id: unkf_16
        type: f4le
      - id: cullbox_size
        type: fl_vector
      - id: unkf_1a
        type: f4le

    instances:
      data_c:
        io: _root._io
        pos: off_data_c
        size: 6
        if: off_data_c != 0x3f800000 and off_data_c != 0

      surfaces:
        io: _root._io
        pos: off_surf_list
        type: surface(off_v_buf, v_scale)
        repeat: until
        repeat-until: _.off_next == 0
        if: off_surf_list != 0

    types:
      surface:
        doc: |
          Headers are in a linked list.
        params:
          - id: off_v_buf
            type: u4
          - id: v_scale
            type: s4
        seq:
          - id: off_prev
            type: u4le
          - id: off_next
            type: u4le
          - id: off_data
            type: u4le
          - id: off_material
            type: u4le
          - id: unk_4
            type: u2le
          - id: num_i
            type: u2le
          - contents: [0, 0, 0, 0]
          - id: unk_6
            type: u2le
          - id: unk_7
            type: u2le
          - id: unk_8
            type: u2le
          - id: unk_9
            type: u2le

        instances:
          faces:
            io: _root._io
            pos: off_data
            type: faces

          v_buf:
            io: _root._io
            pos: off_v_buf
            type:
              switch-on: v_scale
              cases:
                -1: fl_vector_be
                _: short_vector
            repeat: expr
            repeat-expr: num_i

        types:
          faces:
            seq:
              - id: data_size
                type: u4
              - id: num_v_smthn_total
                type: u2
              - id: unk_2
                type: u2
              - contents: [0, 0, 0, 0, 0, 0, 0, 0]
              - contents: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

              - id: data
                size: data_size

          face:
            seq:
              - id: unk_0
                type: u2
              - id: num_smthn
                type: u2
                if: unk_0 == 0x99
              - id: unk_1
                type: i
                repeat: expr
                repeat-expr: num_smthn
                if: unk_0 == 0x99

            types:
              i:
                seq:
                  - id: idx
                    type: u2
                  - id: unk
                    size: 9
