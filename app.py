from flask import Flask, render_template, request, jsonify
from model_engine.nlp_processing import process_user_input
from model_engine.model_customizer import customize_model
from model_engine.animation_engine import apply_animation
from model_engine.generate_video import create_video
from model_engine.rendering import render_model
from model_engine.speech_sync import generate_speech, apply_lip_sync
from model_engine.import_fbx import import_fbx_and_apply_textures  # Import the function

app = Flask(__name__, static_url_path='/node_modules', static_folder='node_modules')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_model():
    data = request.get_json()  # Correctly calling the method to parse JSON
    
    if not data or "text" not in data:
        return jsonify({"error": "No input provided or 'text' field missing"}), 400

    try:
        user_input = data["text"]
        app.logger.debug(f"User Input: {user_input}")  # Replaced print with debug

        # Process the input
        features, actions, speech_text = process_user_input(user_input)
        app.logger.debug(f"Features: {features}, Actions: {actions}, Speech Text: {speech_text}")  # Replaced print with debug

        # Customize the 3D model
        model_path = customize_model(features)
        app.logger.debug(f"Model Path: {model_path}")  # Replaced print with debug

        # Generate speech audio
        audio_path = generate_speech(speech_text)
        app.logger.debug(f"Audio Path: {audio_path}")  # Replaced print with debug

        # Apply lip-sync and animations
        synced_model_path = apply_lip_sync(model_path, audio_path)
        app.logger.debug(f"Synced Model Path: {synced_model_path}")  # Replaced print with debug

        animation_path = apply_animation(synced_model_path, actions)
        app.logger.debug(f"Animation Path: {animation_path}")  # Replaced print with debug

        # Render the final model
        rendered_output_path = render_model(animation_path, audio_path)
        app.logger.debug(f"Rendered Output Path: {rendered_output_path}")  # Replaced print with debug

        # Generate the final video
        output_video_path = "static/assets/final_output.mp4"  # Path for final scaled video
        create_video(rendered_output_path, output_video_path)
        app.logger.info(f"Output Video Path: {output_video_path}")  # Replaced print with info for final output

        return jsonify({
            "rendered_output": rendered_output_path,
            "final_output": output_video_path
        })
    except Exception as e:
        app.logger.error(f"Error during processing: {str(e)}")  # Log the error
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)




















#------------------------------------------------------------------------------------------------------------------------

# from flask import Flask, render_template, request, jsonify
# from model_engine.nlp_processing import process_user_input  # Ensure this function exists
# from model_engine.model_customizer import customize_model  # Ensure this function exists
# from model_engine.animation_engine import apply_animation  # Ensure this function exists
# from model_engine.generate_video import create_video  # Ensure this function exists
# from model_engine.rendering import render_model  # Ensure this function exists
# from model_engine.speech_sync import generate_speech, apply_lip_sync  # Ensure these functions exist

# app = Flask(__name__, static_url_path='/node_modules', static_folder='node_modules')

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/generate", methods=["POST"])
# def generate_model():
#     data = request.get_json()  # Correctly calling the method to parse JSON
    
#     if not data or "text" not in data:
#         return jsonify({"error": "No input provided or 'text' field missing"}), 400

#     try:
#         user_input = data["text"]
#         app.logger.debug(f"User Input: {user_input}")  # Replaced print with debug

#         # Process the input
#         features, actions, speech_text = process_user_input(user_input)
#         app.logger.debug(f"Features: {features}, Actions: {actions}, Speech Text: {speech_text}")  # Replaced print with debug

#         # Customize the 3D model
#         model_path = customize_model(features)
#         app.logger.debug(f"Model Path: {model_path}")  # Replaced print with debug

#         # Generate speech audio
#         audio_path = generate_speech(speech_text)
#         app.logger.debug(f"Audio Path: {audio_path}")  # Replaced print with debug

#         # Apply lip-sync and animations
#         synced_model_path = apply_lip_sync(model_path, audio_path)
#         app.logger.debug(f"Synced Model Path: {synced_model_path}")  # Replaced print with debug

#         animation_path = apply_animation(synced_model_path, actions)
#         app.logger.debug(f"Animation Path: {animation_path}")  # Replaced print with debug

#         # Render the final model
#         rendered_output_path = render_model(animation_path, audio_path)
#         app.logger.debug(f"Rendered Output Path: {rendered_output_path}")  # Replaced print with debug

#         # Generate the final video
#         output_video_path = "static/assets/final_output.mp4"  # Path for final scaled video
#         create_video(rendered_output_path, output_video_path)
#         app.logger.info(f"Output Video Path: {output_video_path}")  # Replaced print with info for final output

#         return jsonify({
#             "rendered_output": rendered_output_path,
#             "final_output": output_video_path
#         })
#     except Exception as e:
#         app.logger.error(f"Error during processing: {str(e)}")  # Log the error
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)

















#------------------------------------------------------------------------------------------------

# from flask import Flask, render_template, request, jsonify
# from model_engine.nlp_processing import process_user_input
# from model_engine.model_customizer import customize_model
# from model_engine.animation_engine import apply_animation
# from model_engine.generate_video import create_video
# from model_engine.rendering import render_model
# from model_engine.speech_sync import generate_speech, apply_lip_sync

# app = Flask(__name__, static_url_path='/node_modules', static_folder='node_modules')

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/generate", methods=["POST"])
# def generate_model():
#     data = request.get_json()  # Correctly calling the method to parse JSON
    
#     if not data or "text" not in data:
#         return jsonify({"error": "No input provided or 'text' field missing"}), 400

#     try:
#         user_input = data["text"]
#         app.logger.debug(f"User Input: {user_input}")  # Replaced print with debug

#         # Process the input
#         features, actions, speech_text = process_user_input(user_input)
#         app.logger.debug(f"Features: {features}, Actions: {actions}, Speech Text: {speech_text}")  # Replaced print with debug

#         # Customize the 3D model
#         model_path = customize_model(features)
#         app.logger.debug(f"Model Path: {model_path}")  # Replaced print with debug

#         # Generate speech audio
#         audio_path = generate_speech(speech_text)
#         app.logger.debug(f"Audio Path: {audio_path}")  # Replaced print with debug

#         # Apply lip-sync and animations
#         synced_model_path = apply_lip_sync(model_path, audio_path)
#         app.logger.debug(f"Synced Model Path: {synced_model_path}")  # Replaced print with debug

#         animation_path = apply_animation(synced_model_path, actions)
#         app.logger.debug(f"Animation Path: {animation_path}")  # Replaced print with debug

#         # Render the final model
#         rendered_output_path = render_model(animation_path, audio_path)
#         app.logger.debug(f"Rendered Output Path: {rendered_output_path}")  # Replaced print with debug

#         # Generate the final video
#         output_video_path = "static/assets/final_output.mp4"  # Path for final scaled video
#         create_video(rendered_output_path, output_video_path)
#         app.logger.info(f"Output Video Path: {output_video_path}")  # Replaced print with info for final output

#         return jsonify({
#             "rendered_output": rendered_output_path,
#             "final_output": output_video_path
#         })
#     except Exception as e:
#         app.logger.error(f"Error during processing: {str(e)}")  # Log the error
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
















# # from flask import Flask, render_template, request, jsonify
# # from model_engine.nlp_processing import process_user_input
# # from model_engine.model_customizer import customize_model
# # from model_engine.animation_engine import apply_animation
# # from model_engine.generate_video import create_video
# # from model_engine.rendering import render_model
# # from model_engine.speech_sync import generate_speech, apply_lip_sync

# # app = Flask(__name__, static_url_path='/node_modules', static_folder='node_modules')

# # @app.route("/")
# # def index():
# #     return render_template("index.html")

# # @app.route("/generate", methods=["POST"])
# # def generate_model():
# #     data = request.get_json()  # Correctly calling the method to parse JSON
    
# #     if not data or "text" not in data:
# #         return jsonify({"error": "No input provided or 'text' field missing"}), 400

# #     try:
# #         user_input = data["text"]
# #         print(f"User Input: {user_input}")

# #         # Process the input
# #         features, actions, speech_text = process_user_input(user_input)
# #         print(f"Features: {features}, Actions: {actions}, Speech Text: {speech_text}")

# #         # Customize the 3D model
# #         model_path = customize_model(features)
# #         print(f"Model Path: {model_path}")

# #         # Generate speech audio
# #         audio_path = generate_speech(speech_text)
# #         print(f"Audio Path: {audio_path}")

# #         # Apply lip-sync and animations
# #         synced_model_path = apply_lip_sync(model_path, audio_path)
# #         print(f"Synced Model Path: {synced_model_path}")

# #         animation_path = apply_animation(synced_model_path, actions)
# #         print(f"Animation Path: {animation_path}")

# #         # Render the final model
# #         rendered_output_path = render_model(animation_path, audio_path)
# #         print(f"Rendered Output Path: {rendered_output_path}")

# #         # Generate the final video
# #         output_video_path = "static/assets/final_output.mp4"  # Path for final scaled video
# #         create_video(rendered_output_path, output_video_path)
# #         print(f"Output Video Path: {output_video_path}")

# #         return jsonify({
# #             "rendered_output": rendered_output_path,
# #             "final_output": output_video_path
# #         })
# #     except Exception as e:
# #         app.logger.error(f"Error during processing: {str(e)}")
# #         return jsonify({"error": str(e)}), 500

# # if __name__ == "__main__":
# #     app.run(debug=True)
