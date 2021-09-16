# This script creates two kinds of isometric cameras.
# The one, TrueIsocam called camera, is the mathematical correct isometric camera
# with the 54.736 rotation to get the 30 degrees angles at the sides of the rhombus.

# The other, GameIsocam called camera, is a camera with which you can render
# isometric tiles for a 2d game. Here we need a 60 degrees angle instedad of
# the 54.736 one to get a proper stairs effect and a ratio of 2:1

# Then there is the special case with a 4:3 ratio, which is button 3.
# You can also make 2D games with that one. The view is more topdown
# though as with a 2:1 ratio of the traditional game iso view.

# You can of course set up everything by hand. This script is a convenient solution so that you don't have to setup it again and again.

# The script is under Apache license

bl_info = {
    "name": "Create IsoCam",
    "description": "Creates a true isometric camera or a isometric camera for game needs",
    "author": "Reiner 'Tiles' Prokein",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Toolshelf",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Add_Mesh/Create_IsoCam",
    "category": "Create"}

import bpy
from bpy.types import Operator
from bpy_extras.object_utils import AddObjectHelper

ORTHO_SCALE = 14.123
CAMERA_TYPE = 'ORTHO'
BLENDER_OPT = {'REGISTER', 'UNDO'}

def setup_camera(object, rotation, bl_label):
    object.rotation_euler = rotation
    object.data.type = CAMERA_TYPE
    object.data.ortho_scale = ORTHO_SCALE
    object.name = bl_label

class TrueIsoCam(Operator, AddObjectHelper):
    """Create a new TrueIsocam"""
    bl_idname = "scene.create_trueisocam"
    bl_label = "TrueIsocam"
    bl_options = BLENDER_OPT

    def execute(self, context):
        bpy.ops.object.camera_add(location=(30.60861, -30.60861, 30.60861))
        setup_camera(bpy.context.active_object, (0.955324, 0, 0.785398), self.bl_label)
        bpy.ops.view3d.object_as_camera()

        return {'FINISHED'}

class GameIsoCam(bpy.types.Operator):
    """Creates a camera with isometric view for game needs"""
    bl_idname = "scene.create_gameisocam"
    bl_label = "GameIsocam"
    bl_options = BLENDER_OPT

    def execute(self, context):
        bpy.ops.object.camera_add(location=(30.60861, -30.60861, 25.00000))
        setup_camera(bpy.context.active_object, (1.047198, 0, 0.785398), self.bl_label)
        bpy.ops.view3d.object_as_camera()

        return {'FINISHED'}

class GameIsoCam4x3(bpy.types.Operator):
    """Creates a camera with a special 4:3 iso view for game needs"""
    bl_idname = "scene.create_gameisocam4to3"
    bl_label = "GameIsocam4to3"
    bl_options = BLENDER_OPT

    def execute(self, context):
        bpy.ops.object.camera_add(location=(23.42714, -23.42714, 37.4478))
        setup_camera(bpy.context.active_object, (0.724312, 0, 0.785398), self.bl_label)
        bpy.ops.view3d.object_as_camera()

        return {'FINISHED'}

class IsoCamMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_select_submenu"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        layout.operator("scene.create_trueisocam", text="Isometric Camera", icon='VIEW_CAMERA')
        layout.operator("scene.create_gameisocam", text="Isometric Game Camera", icon='VIEW_CAMERA')
        layout.operator("scene.create_gameisocam4to3", text="Isometric Game Camera 4:3", icon='VIEW_CAMERA')

# Registration

def add_Menu_button(self, context):
    self.layout.separator()
    self.layout.menu(
        IsoCamMenu.bl_idname,
        text="Isometric Cameras",
        icon='VIEW_CAMERA')


def register():
    bpy.utils.register_class(TrueIsoCam)
    bpy.utils.register_class(GameIsoCam)
    bpy.utils.register_class(GameIsoCam4x3)
    bpy.utils.register_class(IsoCamMenu)
    bpy.types.VIEW3D_MT_add.append(add_Menu_button)


def unregister():
    bpy.utils.unregister_class(TrueIsoCam)
    bpy.utils.unregister_class(GameIsoCam)
    bpy.utils.unregister_class(GameIsoCam4x3)
    bpy.utils.unregister_class(IsoCamMenu)
    bpy.types.VIEW3D_MT_add.remove(add_Menu_button)


if __name__ == "__main__":
    register()
