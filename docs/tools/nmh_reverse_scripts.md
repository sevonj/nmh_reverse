# NMH Python Scripts (this repo)

!!! note inline end ""
    __Links__
    [`GitHub`](https://github.com/sevonj/nmh_reverse)
    
    __Games__
    `NMH`
    
    __File formats__
    `FLCG`
    `GMF2` 
    

A collection of scripts for tampering with NMH maps. Also contains Kaitai Struct files.

## Requirements
1. Game files
    - From Wii: Unpack the entire disc image to `./filesystem` with Dolphin emu.
    - From PC (untested): Copy the root folder to `./filesystem/DATA/files`.
1. Python
    - Use python-poetry for automatic dependencies or read pyproject.toml and install them manually.


## Scripts
### unpack_flcg.py
No args.

Extract all open world colliders: `filesystem/DATA/files/STG_HI/*.GCL`


### unpack_gmf2.py
No args.

Extract all open world visuals: `filesystem/DATA/files/STG_HI/*.GM2`

### gm2_mangler.py
args: filename without full path.

Platform for corrupting specific values and quick testing.

### .ksy files
Kaitai Struct files. Useful for further reverse-engineering.

Easiest way to get started is to go to [https://ide.kaitai.io](https://ide.kaitai.io) and load your `.ksy` and sample files there. Right click the `.ksy` file to generate a new python parser.