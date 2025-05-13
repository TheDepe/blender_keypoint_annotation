bl_info = {
    "name": "Keypoint Tools",
    "author": "Dennis Perrett, MPI-IS",
    "version": (1, 0),
    "blender": (4, 4, 3),
    "location": "View3D > Sidebar > Point Tools",
    "description": "Add and export named keypoints",
    "category": "Object",
}
import bpy

from .operators import OBJECT_OT_add_points, OBJECT_OT_export_points
from .panels import VIEW3D_PT_point_tools





# --- Register ---
classes = (
    OBJECT_OT_add_points,
    OBJECT_OT_export_points,
    VIEW3D_PT_point_tools,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.num_points

if __name__ == "__main__":
    register()