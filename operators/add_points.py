import bpy
from ..data.keypoints import KEYPOINTS

class OBJECT_OT_add_points(bpy.types.Operator):
    bl_idname = "object.add_points"
    bl_label = "Reset and Add Keypoints"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        root_name = "Keypoints"

        # -----------------------------
        # Remove existing root object
        # -----------------------------
        root = bpy.data.objects.get(root_name)
        if root:
            # Delete all children (keypoints)
            for child in root.children:
                bpy.data.objects.remove(child, do_unlink=True)
            # Delete the root object itself
            bpy.data.objects.remove(root, do_unlink=True)

        # -----------------------------
        # Create root Empty object
        # -----------------------------
        root = bpy.data.objects.new(root_name, None)
        root.empty_display_type = 'SPHERE'
        scene.collection.objects.link(root)

        # -----------------------------
        # Create keypoints as children
        # -----------------------------
        for kp_name, kp_location in KEYPOINTS.items():
            # Create sphere mesh
            bpy.ops.mesh.primitive_uv_sphere_add(
                radius=0.01,  # Tiny radius
                location=kp_location
            )
            sphere = context.active_object
            sphere.name = kp_name

            # Parent to root
            sphere.parent = root

            # Set viewport display color (Blender must be in Material Preview or Rendered view to see it)
            mat = bpy.data.materials.get("KeypointMaterial")
            if not mat:
                mat = bpy.data.materials.new(name="KeypointMaterial")
                mat.diffuse_color = (1.0, 0.5, 0.0, 1.0)  # Orange RGBA
                mat.use_nodes = False  # Simpler for display color only
            sphere.data.materials.append(mat)


        self.report({'INFO'}, f"Added keypoints parented to '{root_name}'")
        return {'FINISHED'}
