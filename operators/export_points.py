import bpy
import json

from bpy.props import StringProperty
from bpy_extras.io_utils import ExportHelper

class OBJECT_OT_export_points(bpy.types.Operator, ExportHelper):
    bl_idname = "export_scene.points_json"
    bl_label = "Export Keypoint Locations (JSON)"

    filename_ext = ".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
    )

    def execute(self, context):
        scene = context.scene
        keypoints_data = {}

        # Get root object
        root = bpy.data.objects.get("Keypoints")
        if not root:
            self.report({'WARNING'}, "No 'Keypoints' root object found.")
            return {'CANCELLED'}

        # Collect child keypoints
        for child in root.children:
            loc = child.matrix_world.translation  # World-space position
            keypoints_data[child.name] = [float(coord) for coord in loc]

        # Write to JSON
        try:
            with open(self.filepath, 'w') as f:
                json.dump(keypoints_data, f, indent=4)
            self.report({'INFO'}, f"Exported {len(keypoints_data)} keypoints to JSON.")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Failed to export: {e}")
            return {'CANCELLED'}
