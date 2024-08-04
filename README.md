# No More Heroes file format reversing

> [!NOTE]  
> Better instructions [here](https://sevonj.github.io/nmh_reverse/tools/nmh_reverse_scripts/).

![image](https://github.com/user-attachments/assets/625044d5-f970-4bf6-aafe-20b4fb902551)

Contains [Kaitai Struct](https://kaitai.io/) definitions.

Requirements:
- Game files: Extract the Wii disc image to ./filesystem with Dolphin Emulator.
- Python, kaitaistruct package. Optionally manage deps with poetry.

Known data:
- `.GCL` files: World collisions
- `.GM2` files: World textures, materials, geometry.
