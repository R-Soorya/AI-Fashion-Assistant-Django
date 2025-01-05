
from . import prompt
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def recommend(collections, existing_plan):

    # print("Classified Collections:\n")
    # for category, items in collections.items():
    #     print(f"{category.capitalize()}:")
    #     for item in items:
    #         print(f"  - Filename: {item['filename']}, Color: {item['color']}")
    #     print()
    if existing_plan:
        prompt_ = prompt.regeneration_prompt(collections, existing_plan)
    else:
        prompt_ = prompt.generate_prompt(collections)
    refined_prompt = [
        {
            'role': 'user',
            'parts': [prompt_]
        }
    ]
    response = model.generate_content(refined_prompt)

    # print('Response:',response.text)

    cleaned_response = json_response(response)

    # print('Json Response:\n',cleaned_response,'\n')
    return cleaned_response

    # pairs.save_outfit_images(cleaned_response, collections)

def json_response(response):
    try:
        # Navigate to the text part of the response
        raw_text = response.text

        # Remove the marker
        cleaned_text = raw_text.replace("```json", "").replace("```", "").strip()

        # Convert JSON string to a Python dictionary
        cleaned_response = json.loads(cleaned_text)

        # print("\ncleaned response:",cleaned_response)
        
        return cleaned_response
    except KeyError as e:
        print("KeyError encountered while parsing response:", e)
        return {}
    except json.JSONDecodeError as e:
        print("JSONDecodeError encountered:", e)
        return {}
    except Exception as e:
        print("Unexpected error encountered:", e)
        return {}
# collections = {'top': [{'filename': 'shirt_1.jpg', 'color': 'Cloud Burst'}, {'filename': 'shirt_2.jpg', 'color': 'Gray Nurse'}, {'filename': 'shirt_3.jpg', 'color': 'Pigeon Post'}, {'filename': 'shirt_4.jpg', 'color': 'Van Cleef'}, {'filename': 'shirt_5.jpg', 'color': 'Desert Storm'}], 'bottom': [{'filename': 'trouser_1.jpg', 'color': 'Indian Khaki'}, {'filename': 'trouser_2.jpg', 'color': 'Dune'}, {'filename': 'trouser_3.jpg', 'color': 'Eerie Black'}]}


# regenerate_prompt = prompt.regeneration_prompt(collections)







