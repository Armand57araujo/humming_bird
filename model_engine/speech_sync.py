import pyttsx3
import os
import mediapipe as mp
import bpy
from pocketsphinx import LiveSpeech

# Initialize Mediapipe FaceMesh for mouth landmarks (if you need to use it for real-time facial analysis)
mp_face_mesh = mp.solutions.face_mesh

phoneme_to_viseme = {
    "p": "closed_lips",
    "b": "closed_lips",
    "m": "closed_lips",
    "f": "upper_teeth_on_lip",
    "v": "upper_teeth_on_lip",
    "s": "slightly_open_tight",
    "z": "slightly_open_tight",
    "a": "fully_open",
    "æ": "fully_open",
    "o": "rounded_lips",
    "e": "half_open",
    "i": "stretched_lips",
    "default": "neutral"
}

def generate_speech(text, output_dir="static/assets"):
    """
    Generate speech from text and save it as an audio file.
    """
    engine = pyttsx3.init()
    audio_path = os.path.join(output_dir, "speech_output.wav")
    engine.save_to_file(text, audio_path)
    engine.runAndWait()
    return audio_path

def extract_phonemes(audio_path):
    """
    Extract phonemes from the audio using PocketSphinx.
    """
    phonemes = []
    
    # PocketSphinx requires a configuration setup
    config = {
        'hmm': '/path/to/pocketsphinx/model',  # Provide path to your model directory
        'dict': '/path/to/pocketsphinx/model/cmudict-en-us.dict',  # Dictionary for mapping words to phonemes
        'lm': '/path/to/pocketsphinx/model/en-us.lm.bin',  # Language model
    }
    
    # Use PocketSphinx's LiveSpeech feature to process the audio file
    speech = LiveSpeech(**config)
    
    for phrase in speech:
        for word in phrase:
            phoneme = word[0]  # Retrieve the phoneme (if it's available in the dictionary)
            timestamp = word.start_time  # Get the timestamp of the phoneme
            phonemes.append((phoneme, timestamp))
    
    return phonemes

def map_phonemes_to_visemes(phoneme_list):
    """
    Map extracted phonemes to visemes using the predefined dictionary.
    """
    viseme_list = []
    for phoneme, timestamp in phoneme_list:
        viseme = phoneme_to_viseme.get(phoneme, phoneme_to_viseme["default"])
        viseme_list.append((viseme, timestamp))
    return viseme_list

def apply_lip_sync(model_path, audio_path, output_dir="static/assets"):
    """
    Synchronize lip movements with speech audio on a 3D model.
    """
    phonemes = extract_phonemes(audio_path)
    visemes = map_phonemes_to_visemes(phonemes)

    # Load the model in Blender
    bpy.ops.wm.open_mainfile(filepath=model_path)
    model_object = bpy.context.active_object

    if not model_object:
        raise ValueError("No active model object found in Blender")

    # Apply shape keys for visemes
    for viseme, timestamp in visemes:
        if viseme in model_object.data.shape_keys.key_blocks:
            shape_key = model_object.data.shape_keys.key_blocks[viseme]
            shape_key.value = 1
            frame = int(timestamp * bpy.context.scene.render.fps)
            shape_key.keyframe_insert(data_path="value", frame=frame)

    # Save the updated model
    output_file = os.path.join(output_dir, "lip_synced_model.blend")
    bpy.ops.wm.save_as_mainfile(filepath=output_file)

    return output_file























#------------------------------------------------------------------------------------------------

# import pyttsx3
# import os
# import mediapipe as mp
# # from visemesync import phoneme_to_viseme

# # Initialize Mediapipe FaceMesh for mouth landmarks
# mp_face_mesh = mp.solutions.face_mesh

# phoneme_to_viseme = {
#     "p": "closed_lips",
#     "b": "closed_lips",
#     "m": "closed_lips",
#     "f": "upper_teeth_on_lip",
#     "v": "upper_teeth_on_lip",
#     "s": "slightly_open_tight",
#     "z": "slightly_open_tight",
#     "a": "fully_open",
#     "æ": "fully_open",
#     "o": "rounded_lips",
#     "e": "half_open",
#     "i": "stretched_lips",
#     "default": "neutral"
# }

# def generate_speech(text, output_dir="static/assets"):
#     """
#     Generate speech from text and save it as an audio file.
#     """
#     engine = pyttsx3.init()
#     audio_path = os.path.join(output_dir, "speech_output.wav")
#     engine.save_to_file(text, audio_path)
#     engine.runAndWait()
#     return audio_path

# def extract_phonemes(audio_path):
#     """
#     Placeholder for extracting phonemes and their timestamps from audio.
#     Implement this using a library like PocketSphinx or Google Speech-to-Text.
#     """
#     # Example phoneme extraction (manually created for demonstration)
#     return [("p", 0.1), ("a", 0.3), ("s", 0.5)]  # Phoneme and timestamp pairs

# def map_phonemes_to_visemes(phoneme_list):
#     """
#     Map extracted phonemes to visemes using the predefined dictionary.
#     """
#     viseme_list = []
#     for phoneme, timestamp in phoneme_list:
#         viseme = phoneme_to_viseme.get(phoneme, phoneme_to_viseme["default"])
#         viseme_list.append((viseme, timestamp))
#     return viseme_list

# def apply_lip_sync(model_path, audio_path, output_dir="static/assets"):
#     """
#     Synchronize lip movements with speech audio on a 3D model.
#     """
#     phonemes = extract_phonemes(audio_path)
#     visemes = map_phonemes_to_visemes(phonemes)

#     # Placeholder: Update the model's mouth shapes using visemes
#     animated_model = os.path.join(output_dir, "lip_synced_model.blend")
    
#     # Example: Use Mediapipe or Blender API to manipulate the model
#     with mp_face_mesh.FaceMesh(static_image_mode=False) as face_mesh:
#         for viseme, timestamp in visemes:
#             print(f"Applying viseme '{viseme}' at timestamp {timestamp}")
#             # Logic to modify the 3D model's mouth shape using Blender or Mediapipe

#     # Save the updated model
#     # (Placeholder: Return the same model path for now)
#     return animated_model