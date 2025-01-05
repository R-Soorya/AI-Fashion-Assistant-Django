import cv2
from sklearn.cluster import KMeans
from io import BytesIO
from PIL import Image
import numpy as np
import requests


def preprocess_image(image_file):
    print('color_detection : preprocessing image')
    # Reset the file pointer to the beginning
    image_file.seek(0)
    # Convert InMemoryUploadedFile to a NumPy array
    image_bytes = image_file.read()  # Read file-like object as bytes
    image_pil = Image.open(BytesIO(image_bytes))  # Open with PIL
    image_np = np.array(image_pil)  # Convert to NumPy array

    # Convert from RGB to BGR for OpenCV compatibility
    img = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (224, 224))  # Resize to the model's input size
    return img


def get_dominant_color(image):
    print('color_detection : detetecting RGB value')
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(pixels)
    dominant_color = kmeans.cluster_centers_  # Get the most dominant colors
    return tuple(dominant_color.astype(int))  # Return as RGB tuple


def get_color_name_from_api(r, g, b):
    print('color_detection :getting color')
    # Use The Color API to get the color name
    url = f'https://www.thecolorapi.com/id?rgb=rgb({r},{g},{b})'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        color_name = data['name']['value']
        return color_name
    else:
        return "Color name not found"


def color(image_file):
    print('Detecting color...')

    # Preprocess the image
    res = preprocess_image(image_file)

    # Get the dominant colors
    colors = get_dominant_color(res)

    # Extract the second dominant color
    r, g, b = colors[1]

    # Call the API to get the color name
    color_name = get_color_name_from_api(r, g, b)

    print(f'Predicted color: {color_name}')
    return color_name
