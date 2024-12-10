from model_engine.import_fbx import import_fbx_and_apply_textures
import shutil

def customize_model(features, base_model="3D_assets/base_model.blend"):
    """
    Customize a 3D model based on input features and save it as a new model.
    
    Parameters:
    - features: A dictionary or structure containing customization details.
    - base_model: Path to the base .blend file (default is '3D_assets/base_model.blend').
    
    Returns:
    - Path to the customized model.
    """
    # Define paths
    fbx_file = "3D_assets/models/model1.fbx"  # Placeholder: Select model based on features
    texture_folder = "3D_assets/textures"
    customized_model = "static/assets/customized_model.blend"

    # Check if base model or FBX file exists
    if not os.path.exists(base_model):
        raise FileNotFoundError(f"Base model not found: {base_model}")
    if not os.path.exists(fbx_file):
        raise FileNotFoundError(f"FBX file not found: {fbx_file}")
    
    # Import FBX and apply textures
    import_fbx_and_apply_textures(fbx_file, texture_folder, customized_model)
    
    # Optional: If no customization is needed, copy the base model
    if not features:
        shutil.copy(base_model, customized_model)
    
    return customized_model



# def customize_model(features, base_model="3D_assets/base_model.blend"):
#     """
#     Apply customizations to the 3D model based on features.
#     """
#     customized_model = "static/assets/customized_model.blend"
#     # Apply customizations using Blender scripting or external libraries
#     # Placeholder: Copy the base model for now
#     import shutil
#     shutil.copy(base_model, customized_model)
#     return customized_model

# from model_engine.import_fbx import import_fbx_and_apply_textures

# def customize_model(features):
#     fbx_file = "3D_assets/models/model1.fbx"  # Select a default model or match features
#     texture_folder = "3D_assets/textures"
#     output_file = "static/assets/animated_model.blend"
    
#     # Import and customize model
#     import_fbx_and_apply_textures(fbx_file, texture_folder, output_file)
    
#     return output_file
