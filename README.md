# AI Fashion Assistant

The AI Fashion Assistant is a Django-based application that provides intelligent outfit recommendations based on user preferences and wardrobe collections. It integrates machine learning algorithms and open source models (Gen AI models) to ensure each outfit plan is stylish, trendy, and personalized.

## Features

### 1. Wardrobe Collection Management

Add, edit, or delete items in your wardrobe.

Categorize clothing items as tops or bottoms.

### 2. Outfit Recommendations

Generate a weekly outfit plan tailored to your preferences.

Focus on color harmony, trendy combinations, and occasion-specific styles.

Suggestions include casual and semi-formal outfits.

### 3. User Preferences

Input personal preferences such as:

Gender: Male or Female.

Skin Tone: Fair, Medium, or Dark.

Body Shape: Rectangle, Oval, etc.

Face Shape: Oval, Round, etc.

Dress Type: Casual, Formals, etc.

Recommendations are optimized for the given preferences.

## Technologies Used

### Backend

Python

Django Framework

### Frontend

HTML

CSS

### Machine Learning

Hugging Face Transformers (nathanReitinger/FASHION-vision)

Pre-trained models (Gemini) for feature extraction and classification

## Installation

### Pre-requisites

Python 3.8+

Virtual Environment (recommended)

Git

### Steps

#### Clone the repository:

git clone https://github.com/R-Soorya/AI-Fashion-Assistant-Django.git

#### Navigate to the project directory:

cd AI-Fashion-Assistant-Django

#### Set up a virtual environment:

python -m venv fashion
source fashion/bin/activate   # For Linux/Mac
fashion\Scripts\activate    # For Windows

#### Install the dependencies:

pip install -r requirements.txt

#### Apply database migrations:

python manage.py migrate

#### Run the development server:

python manage.py runserver

#### Open the application in your browser at http://127.0.0.1:8000/.

## Usage

Add clothing items to your wardrobe.

Specify your preferences.

Generate a personalized weekly outfit plan.

## Future Enhancements

Incorporate accessory suggestions.

Provide outfit suggestions based on weather conditions.

Expand the recommendation system to include dresses and footwear.


Soorya R.AI and Backend DeveloperGitHub: Soorya03

License

This project is licensed under the MIT License - see the LICENSE file for details.

