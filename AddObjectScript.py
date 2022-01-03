import bpy


for y in range(20):
    for x in range(20):
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(y, x, 0))
        bpy.context.active_object.name = f"Harald_{y}_{x}"
        # bpy.ops.material.new()
        # color = i / 3
        # bpy.data.materials[bpy.ops.material.new()].node_tree.nodes["Principled BSDF"].inputs[
        #     0
        # ].default_value = (color, color, color, 1)

