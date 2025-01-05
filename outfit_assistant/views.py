from django.shortcuts import render, HttpResponse
from .additionals import recommendation_outfit, color_generator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required 
def outfit_assistant(request):
    if request.method == 'POST':
        # Get data from form inputs
        gender = request.POST.get('gender')
        body_shape = request.POST.get('body_shape')
        skin_tone = request.POST.get('skin_tone')
        height = request.POST.get('height')
        dress_type = request.POST.get('dress_type')

        # Prepare preference dictionary
        preference = {
            'gender': gender,
            'body_shape': body_shape,
            'skin_tone': skin_tone,
            'height': height,
            'dress_type': dress_type
        }
        # Generate suggestions based on preference
        response = recommendation_outfit.generate_suggestions(preference)

        final_response = []
        for item in response:
            capitalized_item = {}
            for key, value in item.items():
                capitalized_item[key.title()] = value.title()
            final_response.append(capitalized_item)

        color_generator.generate_color_image(final_response)

        # Pass everything inside a context dictionary
        context = {
            'final_response': final_response,
            'gender': gender,
            'body_shape': body_shape,
            'skin_tone': skin_tone,
            'height': height,
            'dress_type': dress_type,
        }

        print('\nFinal Response:',final_response)

        return render (request, 'outfit_assistant.html', context)
    
    return render(request,'outfit_assistant.html')