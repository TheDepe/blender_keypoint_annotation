import bpy

class VIEW3D_PT_point_tools(bpy.types.Panel):
    bl_label = "Point Tools"
    bl_idname = "VIEW3D_PT_point_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Point Tools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        #layout.prop(scene, "num_points")
        layout.operator("object.add_points", text="Add/Reset Keypoints")
        layout.operator("export_scene.points_json", text="Export Points (JSON)")
