# No More Heroes file format reversing

> [!NOTE]  
> Better instructions [here](https://sevonj.github.io/ghm_docs/tools/nmh_reverse_scripts/).  
> The file format documentation effort has been moved to its own repo. What remains here not maintained. See [ghm_docs](https://github.com/sevonj/ghm_docs) for the new repo.

![image](https://github.com/user-attachments/assets/625044d5-f970-4bf6-aafe-20b4fb902551)

Contains [Kaitai Struct](https://kaitai.io/) definitions.

Requirements:
- Game files: Extract the Wii disc image to ./filesystem with Dolphin Emulator.
- Python, kaitaistruct package. Optionally manage deps with poetry.

Known data:
- `.GCL` files: World collisions
- `.GM2` files: World textures, materials, geometry.
