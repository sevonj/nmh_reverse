# No More Heroes file format reversing

![image](https://github.com/user-attachments/assets/8f57d4c7-f891-4d9d-889d-fe0d712a71b9)

Contains [Kaitai Struct](https://kaitai.io/) definitions.

Requirements:
- Game files: Extract the Wii disc image to ./filesystem with Dolphin Emulator.
- Python, kaitaistruct package. Optionally manage deps with poetry.

Known data:
- `.GCL` files: World collisions
- `.GM2` files: World textures, materials, geometry.
