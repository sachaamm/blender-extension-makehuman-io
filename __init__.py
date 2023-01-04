# SPDX-License-Identifier: GPL-2.0-or-later
"""
AlexTest

What is it about? Anything, whatever I think it can speedup workflow,
I'll try to add it. Enjoy <3
"""

import bpy

bl_info = {
    "name": "My Test Add-on",
    "blender": (3, 30, 0),
    "category": "Object",
}


class TestPanel(bpy.types.Panel):
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
        # util.hello(row)


def register():
    print("Hello World, My Test Add-on is now registered")
    bpy.utils.register_class(TestPanel)


def unregister():
    print("Goodbye World, My Test Add-on is now unregistered")
    bpy.utils.unregister_class(TestPanel)
