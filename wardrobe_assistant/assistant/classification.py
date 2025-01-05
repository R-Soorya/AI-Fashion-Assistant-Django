# Load model directly
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image
from django.conf import settings
import os
from .color_detection import color  

model_path = os.path.join(settings.BASE_DIR,'wardrobe_assistant/assistant/classification_model')

processor = AutoImageProcessor.from_pretrained(model_path)
model = AutoModelForImageClassification.from_pretrained(model_path)


# Load class labels
labels = model.config.id2label

# Define categories for top and bottom
TOP_CATEGORIES = ["T - shirt / top", "Shirt", "Pullover", "Coat"]
BOTTOM_CATEGORIES = ["Trouser"]

def classify(image_file):
    print('\nClassifying image...')
    try:
        # image_path = image_file
       # Open the image file using PIL
        image = Image.open(image_file)
        inputs = processor(images=image, return_tensors="pt")

        # Get model predictions
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            max_logit = logits.max().item()
            predicted_class_idx = logits.argmax(-1).item()
        
        # Check if the maximum logit is greater than 7
        if max_logit <= 3:
            print("Invalid Image: Logits value too low.")
            return "Invalid Image"

        # Print the predicted label
        predicted_label = labels[predicted_class_idx]
        print(f"Predicted class label: {predicted_label}")

        detected_color = color(image_file)

        # Classify as top or bottom
        if any(top_item in predicted_label for top_item in TOP_CATEGORIES):
            return {
                "name": predicted_label,
                "category": "top",
                "color": detected_color
            }
        elif any(bottom_item in predicted_label for bottom_item in BOTTOM_CATEGORIES):
            return {
                "name": predicted_label,
                "category": "bottom",
                "color": detected_color
            }
        else:
            return None 
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return None