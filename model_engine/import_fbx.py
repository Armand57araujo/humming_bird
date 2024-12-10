import sys
import os

# Set the path to Blender's Python directory
blender_python_path = '/Applications/Blender.app/Contents/Resources/4.3/python/lib/python3.11/site-packages'
sys.path.append(blender_python_path)

# Now you should be able to import bpy
import bpy
print('bpy module is working with manual path setting')

def import_fbx_and_apply_textures(fbx_file, texture_folder, output_file):
    """
    Import an FBX file and apply textures to the imported mesh.
    - fbx_file: Path to the .fbx file.
    - texture_folder: Folder containing texture images (e.g., PNG files).
    - output_file: The path where the modified Blender file will be saved.
    """
    # Import the .fbx file
    bpy.ops.import_scene.fbx(filepath=fbx_file)

    # Get the imported objects
    imported_objects = bpy.context.selected_objects

    for obj in imported_objects:
        if obj.type == 'MESH':  # Ensure we're working with meshes
            # Apply textures if material exists
            for material in obj.data.materials:
                if material and material.use_nodes:
                    # Get material nodes
                    nodes = material.node_tree.nodes
                    # Find the texture node or create one
                    texture_node = nodes.new(type='ShaderNodeTexImage')
                    
                    # Find corresponding texture
                    texture_name = os.path.splitext(os.path.basename(fbx_file))[0] + ".png"
                    texture_path = os.path.join(texture_folder, texture_name)
                    
                    if os.path.exists(texture_path):
                        # Load and link texture
                        image = bpy.data.images.load(texture_path)
                        texture_node.image = image
                        material.node_tree.links.new(
                            nodes.get('Principled BSDF').inputs['Base Color'],
                            texture_node.outputs['Color']
                        )
    
    # Save the updated .blend file
    bpy.ops.wm.save_as_mainfile(filepath=output_file)
    print(f"Saved customized model as {output_file}")

# Example usage
if __name__ == "__main__":
    import_fbx_and_apply_textures(
        fbx_file="3D_assets/models/model1.fbx",   # Path to your FBX model
        texture_folder="3D_assets/textures",      # Path to your texture folder
        output_file="static/assets/animated_model.blend"  # Output path for the .blend file
    )
















#-------------------------------------------------------------------------------------------------------



# import os
# import bpy

# def import_fbx_and_apply_textures(fbx_file, texture_folder, output_file):
#     """
#     Import an FBX file and apply textures to the imported mesh.
#     - fbx_file: Path to the .fbx file.
#     - texture_folder: Folder containing texture images (e.g., PNG files).
#     - output_file: The path where the modified Blender file will be saved.
#     """
#     # Import the .fbx file
#     bpy.ops.import_scene.fbx(filepath=fbx_file)

#     # Get the imported objects
#     imported_objects = bpy.context.selected_objects

#     for obj in imported_objects:
#         if obj.type == 'MESH':  # Ensure we're working with meshes
#             # Apply textures if material exists
#             for material in obj.data.materials:
#                 if material and material.use_nodes:
#                     # Get material nodes
#                     nodes = material.node_tree.nodes
#                     # Find the texture node or create one
#                     texture_node = nodes.new(type='ShaderNodeTexImage')
                    
#                     # Find corresponding texture
#                     texture_name = os.path.splitext(os.path.basename(fbx_file))[0] + ".png"
#                     texture_path = os.path.join(texture_folder, texture_name)
                    
#                     if os.path.exists(texture_path):
#                         # Load and link texture
#                         image = bpy.data.images.load(texture_path)
#                         texture_node.image = image
#                         material.node_tree.links.new(
#                             nodes.get('Principled BSDF').inputs['Base Color'],
#                             texture_node.outputs['Color']
#                         )
    
#     # Save the updated .blend file
#     bpy.ops.wm.save_as_mainfile(filepath=output_file)
#     print(f"Saved customized model as {output_file}")

# # Example usage
# if __name__ == "__main__":
#     import_fbx_and_apply_textures(
#         fbx_file="3D_assets/models/model1.fbx",   # Path to your FBX model
#         texture_folder="3D_assets/textures",      # Path to your texture folder
#         output_file="static/assets/animated_model.blend"  # Output path for the .blend file
#     )
