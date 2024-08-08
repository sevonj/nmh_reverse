"""
    Batch import all .obj files in a directory and subdirectories.
    For convenience.
    
    
    Installation:
        (this is not permanent, just close and reopen blender to get rid of it)
        - Paste this into blender's scripting tab
        - Press the play button once.
    
    Usage:
        - Use the new import option: File > Import > "Wavefront .obj recursive"
        - Select your directory and hit import.
        
    Notes:
        - Due to inefficiency and large number of files, this may take a while.
          If you just want NMH1 open world and hate waiting, you should move
          chunks 51 and above elsewhere; they are not part of the map and
          contain thousands of models.
"""

bl_info = {
    "name": "Obj walk import",
    "blender": (4, 20, 0),
    "category": "Object",
}

import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, CollectionProperty
from bpy.types import Operator
import os

# --- Importer


class ImportSomeData(Operator, ImportHelper):
    """Import all Wavefront (.obj) files in directory and subdirectories."""

    bl_idname = "import_test.some_data"
    bl_label = "Import this dir"

    # ImportHelper mixin class uses this
    filename_ext = ""
    files = CollectionProperty(type=bpy.types.PropertyGroup)

    filter_glob: StringProperty(
        default="",
        options={"HIDDEN"},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self, context):
        dirname = os.path.dirname(self.filepath)
        print(dirname)

        for root, _, files in os.walk(dirname):
            for filename in files:
                filepath = os.path.join(root, filename)
                if filepath.lower().endswith(".obj"):
                    print(filepath)
                    bpy.ops.wm.obj_import(filepath=filepath)

        return {"FINISHED"}


# --- Setup


def menu_func_import(self, context):
    self.layout.operator(ImportSomeData.bl_idname, text="Wavefront .obj recursive")


def register():
    bpy.utils.register_class(ImportSomeData)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ImportSomeData)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()
