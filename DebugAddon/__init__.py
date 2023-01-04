# SPDX-License-Identifier: GPL-2.0-or-later
"""
sachaamm_makehuman_io_addon

What is it about? Anything, whatever I think it can speedup workflow,
I'll try to add it. Enjoy <3
"""

# https://www.youtube.com/watch?v=UVDf2VSmRvk

from sachaamm_makehuman_io_addon import atest
import bpy
from sachaamm_makehuman_io_addon import util
from sachaamm_makehuman_io_addon import exporter

bl_info = {
    "name": "My Test Add-on",
    "blender": (3, 3, 0),
    "category": "Object",
}


class PT_TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "my New Tab"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Add a cube", icon='CUBE')
        row = layout.row()
        util.hello(row)
        exporter.just_a_test()
        row = layout.row()
        row.operator("object.modifier_add")


class PT_TestButton(bpy.types.Operator):
    """Do something"""
    bl_idname = "import_scene.makehuman_mhx2"
    bl_description = 'Import from MHX2 file format (.mhx2)'
    bl_label = "Import MHX2"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_options = {'PRESET', 'UNDO'}

    def execute(self, context):
        print("hello world")

# Only needed if you want to add into a dynamic menu.


def menu_func(self, context):
    self.layout.operator(atest.HelloWorldOperator.bl_idname,
                         text="Hello World Operator")


def register():
    print("Hello World, My Test Add-on is now registered")
    bpy.utils.register_class(PT_TestPanel)
    bpy.utils.register_class(PT_TestButton)
    bpy.types.VIEW3D_MT_view.append(menu_func)
    # self.layout.operator()


def unregister():
    print("Goodbye World, My Test Add-on is now unregistered")
    bpy.utils.unregister_class(PT_TestPanel)
    bpy.utils.unregister_class(PT_TestButton)
