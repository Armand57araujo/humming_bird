import subprocess
import os

def create_video(input_file, output_file, rendered_output_path, audio_path):
    """
    Creates a video using ffmpeg with specified input and output paths.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to save the output file.
        rendered_output_path (str): Path to check if rendered output exists.
        audio_path (str): Path to check if the audio exists.
    """
    try:
        # Check if paths exist before proceeding
        if not os.path.exists(rendered_output_path):
            print(f"Rendered output path does not exist: {rendered_output_path}")
            return
        
        if not os.path.exists(audio_path):
            print(f"Audio path does not exist: {audio_path}")
            return

        # Run ffmpeg to process the video
        subprocess.run([
            'ffmpeg', '-i', input_file, '-vf', 'scale=1920:1080', output_file
        ], check=True)
        print("File generated successfully!")

    except subprocess.CalledProcessError as e:
        print("Error in ffmpeg process:", e)
