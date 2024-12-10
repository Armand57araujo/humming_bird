import os
import subprocess
import bpy

def render_model(model_path, output_dir="static/assets"):
    """
    Render the animation using Blender's command-line interface.
    """
    # Define paths for output video
    rendered_video_path = os.path.join(output_dir, "rendered_video.mp4")
    
    # Render the animation using Blender's command-line interface
    os.system(f"blender -b {model_path} -o {rendered_video_path} -a")  # '-o' specifies output path
    
    return rendered_video_path


def combine_audio_and_video(video_file, audio_file, output_file):
    """
    Combine the rendered video with audio using FFmpeg.
    """
    command = [
        "ffmpeg", "-i", video_file, "-i", audio_file,
        "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", output_file
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Final video with audio saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error in FFmpeg process: {e}")


def render_and_sync(model_path, audio_path, output_dir="static/assets"):
    """
    Render the 3D model and then combine it with the provided audio.
    """
    # Step 1: Render the model into a video using Blender
    rendered_video = render_model(model_path, output_dir)
    
    # Step 2: Define the final output file path
    final_output_video_path = os.path.join(output_dir, "final_output.mp4")
    
    # Step 3: Combine the rendered video with audio using FFmpeg
    combine_audio_and_video(rendered_video, audio_path, final_output_video_path)
    
    return final_output_video_path























#----------------------------------------------------------------------------------------------------------------

# import os
# import subprocess

# def render_model(model_path, audio_path, output_dir="static/assets"):
#     """
#     Combine animations and audio into a final rendered video.
#     """
#     # Define paths for output video
#     rendered_video_path = os.path.join(output_dir, "rendered_video.mp4")
#     final_output_video_path = os.path.join(output_dir, "final_output.mp4")
    
#     # Render the animation using Blender's command-line interface
#     # Ensure Blender renders to the correct output file
#     os.system(f"blender -b {model_path} -o {rendered_video_path} -a")  # '-o' specifies output path
    
#     # Combine audio and video using FFmpeg
#     try:
#         # FFmpeg command to combine video and audio
#         subprocess.run([
#             "ffmpeg", "-i", rendered_video_path, "-i", audio_path, 
#             "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", final_output_video_path
#         ], check=True)
#         print(f"Final video saved at: {final_output_video_path}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error while combining video and audio: {e}")
    
#     return final_output_video_path


#------------------------------------------------------------------------------------------------------------

# import os

# def render_model(model_path, audio_path, output_dir="static/assets"):
#     """
#     Combine animations and audio into a final rendered video.
#     """
#     output_video = os.path.join(output_dir, "final_output.mp4")
#     # Render the animation using Blender's command-line interface
#     os.system(f"blender -b {model_path} -a")
#     # Combine audio and video using FFmpeg
#     os.system(f"ffmpeg -i {model_path} -i {audio_path} -c:v copy -c:a aac {output_video}")
#     return output_video

