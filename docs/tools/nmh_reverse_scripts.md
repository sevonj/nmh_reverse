# NMH Python Scripts (this repo)

!!! note inline end ""
    __Links__
    [`GitHub`](https://github.com/sevonj/nmh_reverse)
    
    __Games__
    [`NMH`](/nmh_reverse/games/NMH)
    
    __File formats__
    [`FLCG`](/nmh_reverse/formats/flcg)
    [`GCT0`](/nmh_reverse/formats/gct0)
    [`GMF2`](/nmh_reverse/formats/gmf2)
    

A collection of scripts for tampering with NMH maps. Also contains Kaitai Struct files.

## Requirements
1. Game files
    - From Wii: Unpack the entire disc image to `./filesystem` with Dolphin emu.
    - From PC (untested): Copy the root folder to `./filesystem/DATA/files`.
1. Python
    - Use python-poetry for automatic dependencies or check what's imported in the scripts and install them manually.


## Scripts
**unpack_all.py**
:   Unpacks everything that can be unpacked. If you just want the models, use this.

**unpack_gct0.py**
:   Unusable for anything else than gathering info.

**unpack_flcg.py**
:   Extract an FLCG file (.GCL)

**unpack_gmf2.py**
:   Extract a GMF2 file (.GM2)

**gm2_mangler.py**
:   Platform for corrupting specific values and quick testing.
    ![img](img/mangled.png){ align=left }

**blender/recursive_obj.py**
:   Convenience .obj import script for those who don't enjoy clicking through every world chunk separately.
    You can find it [here](https://github.com/sevonj/nmh_reverse/blob/master/blender/recursive_obj.py).

**.ksy files**

:   See [Kaitai Struct](/nmh_reverse/tools/kaitaistruct)