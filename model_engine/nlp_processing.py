# This file contains the functions for processing natural language input from the user.

# def process_user_input(text):
#     """
#     Extract features, actions, and speech text from user input.
#     """
#     features = {"skin": "fair", "hair": "brown", "eyes": "blue"}  # Default
#     actions = ["smile", "wave"]  # Default
#     speech_text = text  # For simplicity, use the whole text as dialogue
#     return features, actions, speech_text


import re

def process_user_input(text):
    """
    Extract features, actions, and speech text from user input.
    """
    # Example patterns for extracting features and actions
    feature_patterns = {
        "skin": r"\bskin\s*:\s*(\w+)",  # Example: "skin: fair"
        "hair": r"\bhair\s*:\s*(\w+)",  # Example: "hair: brown"
        "eyes": r"\beyes\s*:\s*(\w+)",  # Example: "eyes: blue"
    }
    
    action_patterns = [r"\bsmile\b", r"\bwave\b", r"\bjump\b", r"\bdance\b"]  # Expand this list

    # Default values
    features = {"skin": "default", "hair": "default", "eyes": "default"}
    actions = []
    speech_text = text

    # Extract features
    for feature, pattern in feature_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            features[feature] = match.group(1)

    # Extract actions
    for action_pattern in action_patterns:
        if re.search(action_pattern, text, re.IGNORECASE):
            actions.append(re.search(action_pattern, text, re.IGNORECASE).group(0))

    # Separate speech text (naive implementation for simplicity)
    command_keywords = ["skin", "hair", "eyes", "smile", "wave", "jump", "dance"]
    speech_text = " ".join(word for word in text.split() if word.lower() not in command_keywords)

    return features, actions, speech_text









# user input needs to be further broken down to reflect the features and actions of the model. This function is a placeholder for that functionality. The function currently returns default values for features and actions, and uses the entire input text as the speech text. This function should be updated to extract relevant information from the input text and return structured data for model customization and animation. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used to customize the 3D model and generate animations accordingly. The speech text can be used for generating speech audio and lip-syncing with the model's mouth movements. The extracted features and actions can be used