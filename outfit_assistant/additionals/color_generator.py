from sentence_transformers import SentenceTransformer, util
import pandas as pd
from PIL import Image
import ast
import numpy as np
import os
from django.conf import settings

# print("Color Embedding Path:", os.path.join(settings.BASE_DIR, 'outfit_assistant/model/color_embeddings.csv'))


color_data = pd.read_csv(os.path.join(settings.BASE_DIR,'outfit_assistant/additionals/model/color_embeddings.csv'))

model = SentenceTransformer(os.path.join(settings.BASE_DIR,'outfit_assistant/additionals/model/sentence_transformer'))

# Convert the string representation of embeddings into actual NumPy arrays
color_data['Embedding'] = color_data['Embedding'].apply(lambda x: np.array(ast.literal_eval(x), dtype=np.float32))


# Find the closest matching color
def get_closest_color(text_input):
    input_embedding = model.encode(text_input)
    similarities = color_data['Embedding'].apply(lambda x: util.cos_sim(input_embedding, x).item())
    best_match = color_data.iloc[similarities.idxmax()]
    return (int(best_match['R']), int(best_match['G']), int(best_match['B'])), best_match['color_name']


def generate_color_image(final_response, size=(500, 500)):

    print('\nGenerating color...')

    output_dir = os.path.join(settings.BASE_DIR,'outfit_assistant/static/color')

    # Define folders for keys and values
    keys_dir = os.path.join(output_dir, "top")
    values_dir = os.path.join(output_dir, "bottom")
    
    # Ensure base and subdirectories exist
    for directory in [keys_dir, values_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            # Clear any existing images in the subdirectory
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path) and file.endswith(('.png', '.jpg', '.jpeg')):
                    os.remove(file_path)

    # Process the final response
    for item in final_response:
        for key, value in item.items():
            # Handle the key
            rgb_key, best_match_key = get_closest_color(key)
            if rgb_key:
                image_key = Image.new("RGB", size, rgb_key)
                file_name_key = f"{key}.png"
                file_path_key = os.path.join(keys_dir, file_name_key)
                image_key.save(file_path_key)
                print(f"Image for key '{key}' ('{best_match_key}') saved as {file_path_key}")
            else:
                print(f"No match found for key '{key}'.")

            # Handle the value
            rgb_value, best_match_value = get_closest_color(value)
            if rgb_value:
                image_value = Image.new("RGB", size, rgb_value)
                file_name_value = f"{value}.png"
                file_path_value = os.path.join(values_dir, file_name_value)
                image_value.save(file_path_value)
                print(f"Image for value '{value}' ('{best_match_value}') saved as {file_path_value}")
            else:
                print(f"No match found for value '{value}'.")


