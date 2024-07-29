meta:
  id: nmh_gm2
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
    contents: 'GMF2'
  - id: version
    doc: "probably."
    type: u4le
    valid: 2
    
  # 16B zero
  - contents: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  
  - id: num_objects
    type: u2le
  - id: num_textures
    type: u2le
  - contents: [0,0]
  - id: num_materials
    type: u2le
  - id: unk_4
    type: u4le
  - id: unk_5
    type: u4le
  - contents: [0,0,0,0]
  - id: unk_7
    type: u4le
  - id: unk_8
    type: u4le
  - id: unk_9
    type: u4le
  
  # 56B zeros
  - contents: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  - contents: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  - contents: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  - contents: [0,0,0,0,0,0,0,0]
  
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
    type: world_object
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
  
  # --- Textures
  
  texture:
    seq:
      - id: name
        type: strz
        size: 8
      - id: unk_0
        type: u4le
      - id: unk_1
        type: u4le
      - id: offset
        type: u4le
      - contents: [0,0,0,0]
      - id: size
        type: u4le
      - id: unk_5
        type: u4le
    
    instances:
    
      data_magic:
        doc: "Just to be extra sure"
        io: _root._io
        pos: offset
        contents: 'GCT0'
        
      data:
        doc: "GHM in-house texture format."
        io: _root._io
        pos: offset
        size: size
    
        
  # --- Materials
        
  material:
    seq:
      - id: name
        type: strz
        size: 8
      - id: unk_0
        type: u4le
      - id: unk_2
        type: u4le
      - id: unk_3
        type: u4le
      - id: offset
        type: u4le
      - contents: [0,0,0,0]
      - contents: [0,0,0,0]
      
    instances:
      data:
        io: _root._io
        pos: offset
        type: material_data
    
    types:
      material_data:
        seq:
          - contents: [0,0,0,0]
          - contents: [0,0,0,0]
          
          - id: unk_2
            doc: "unique?"
            type: u4le
            
          - id: unk_3
            doc: "flags?"
            type: u4le
            
          - id: unkf_4
            type: f4le
          - id: unkf_5
            type: f4le
          - id: unkf_6
            type: f4le
          - id: unkf_7
            type: f4le
            
            # Probably RGBA
          - id: unkf_8
            type: f4le
          - id: unkf_9
            type: f4le
          - id: unkf_a
            type: f4le
          - id: unkf_b
            type: f4le
 
 # --- Objects
 
  world_object:
    seq:
      - id: name
        type: strz
        size: 8
      - id: unk_0
        type: u4le
      - id: off_i_buf
        type: u4le
      - id: unk_2
        type: u4le
      - id: unk_3
        type: u4le
      - id: unk_4
        type: u4le
      - id: unk_5
        type: u4le
      - id: offset_surf_list
        type: u4le
      - contents: [0,0,0,0]
      - contents: [0,0,0,0]
      - id: unk_7
        type: u4le
      - id: origin
        type: fl_vector
      - id: unkf_a
        type: f4le
      - id: unk_b
        type: u4le
      - id: unkf_c
        type: f4le
      - id: unkf_d
        type: f4le
      - id: unkf_e
        type: f4le
      - id: unkf_f
        type: f4le
      - id: unkf_10
        type: f4le
      - id: unkf_11
        type: f4le
      - id: offset_c
        type: u4le
      - id: unkf_13
        type: f4le
      - id: unkf_14
        type: f4le
      - id: unkf_15
        type: f4le
      - id: unkf_16
        type: f4le
      - id: unkf_17
        type: f4le
      - id: unkf_18
        type: f4le
      - id: unkf_19
        type: f4le
      - id: unkf_1a
        type: f4le
        
    instances:
      surfaces:
        io: _root._io
        pos: offset_surf_list
        type: surface(off_i_buf)
        repeat: until
        repeat-until: _.next_offset == 0
        if: offset_surf_list != 0
        
      data_b:
        io: _root._io
        pos: offset_c
        size: 4
        if: offset_c != 0x3f800000
        
        
        
    types:
      surface:
        doc: |
          Headers are in a linked list.
        params:
          - id: off_buf_b
            type: u4
        seq:
          - id: prev_offset
            type: u4le
          - id: next_offset
            type: u4le
          - id: data_offset
            type: u4le
            
          - id: unk_3
            type: u4le
          - id: unk_4
            type: u2le
          - id: num_i
            type: u2le
          - contents: [0,0,0,0]
          - id: unk_6
            type: u2le
          - id: unk_7
            type: u2le
          - id: unk_8
            type: u2le
          - id: unk_9
            type: u2le
        
        instances:
          buf_a:
            io: _root._io
            pos: data_offset
            type: v_buf(off_buf_b)
          
          buf_b:
            io: _root._io
            pos: off_buf_b
            size: 6
            repeat: expr
            repeat-expr: num_i
          
        types:
          v_buf:
            params:
              - id: off_buf_b
                type: u4
                
            seq:
              - id: data_size
                type: u4
              - id: num_v_smthn_total
                type: u2
              - id: unk_2
                type: u2
              - contents: [0,0,0,0,0,0,0,0]
              - contents: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
              
              - id: vs
                type: face(off_buf_b)
                repeat: until
                repeat-until: _.unk_0 == 0
          face:
            params:
              - id: off_buf_b
                type: u4
                
            seq:
              - id: unk_0
                type: u2
              - id: num_smthn
                type: u2
                if: unk_0 == 0x99
              - id: unk_1
                type: v(off_buf_b)
                repeat: expr
                repeat-expr: num_smthn
                if: unk_0 == 0x99
            
            types:
              v:
                params:
                  - id: off_buf_b
                    type: u4
                    
                seq:
                  - id: idx
                    type: u2
                  - id: unk
                    size: 9
                
                instances:
                  data_b:
                    io: _root._io
                    pos: off_buf_b + idx * 6
                    size: 6
            
            #instances:
            #  check_next:
            #    doc: ""
            #    pos: _root.pos + 1
            #    type: u2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        