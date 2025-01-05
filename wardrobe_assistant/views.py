import os
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .assistant.classification import classify
from django.conf import settings
from .models import Outfit, OutfitPlan
from django.http import JsonResponse
from .assistant import recommendation
from datetime import date, timedelta

# Create your views here.
UPLOAD_FOLDER = os.path.join(settings.BASE_DIR,'wardrobe_assistant/assistant/collections')

def wardrobe_assistant(request):
    if request.method == 'POST':
        images = request.FILES.getlist('image')
        if not images:
            return HttpResponse("No images uploaded.")
        
        # Allowed extensions
        valid_extensions = ['jpeg', 'jpg', 'png']

        # Lists to track valid and invalid files
        # image_path = []
        invalid_extensions = []

        # Validate extensions and collect valid/invalid files
        valid_files = []
        for image in images:
            ext = image.name.split('.')[-1].lower()
            if ext in valid_extensions:
                valid_files.append(image)
            else:
                invalid_extensions.append(image.name)

        outfits = []
        invalid = []

        for image in images:
            outfit = classify(image)
            if outfit == 'Invalid Image':
                invalid.append(os.path.basename(image))
            else:
                outfits.append(outfit)

                print(request.user, outfit['category'])

                # Assign a unique filename for the user
                new_filename = generate_filename(request.user, outfit['category'])
                

                outfit = Outfit.objects.create(
                    user = request.user,
                    name = new_filename,
                    # image = os.path.join('outfits', f"{new_filename}.jpg"),
                    image = image,
                    color = outfit['color'],
                    category = outfit['category']
                    )

        print('\nOutfits', outfits)
        print('\nInvalid', invalid)

        # Pass data to the template
        return render(request, 'wardrobe.html', {
            # 'invalid_images': invalid,
            'invalid_extensions': invalid_extensions,
        })
    
    return render(request, 'wardrobe.html')


def generate(request):
    if request.method == 'GET':

        OutfitPlan.objects.all().delete()
        user = request.user
        outfits = Outfit.objects.filter(user=user)

        collections = {
            'top': [],
            'bottom': []
        }

        for outfit in outfits:
            entry = {
                'filename': outfit.name,
                'color': outfit.color
            }

            if outfit.category == 'top':
                collections['top'].append(entry)
            elif outfit.category == 'bottom':
                collections['bottom'].append(entry)

        print('\nCollections:', collections)
        response = recommendation.recommend(collections)
        print('\nResponse:', response)

        # Pair the tops and bottoms for display
        pairs = []
        start_date = date.today()

        for day_index, pair in enumerate(response.values(), start=1):
            top_name = '_'.join(pair['top'].split(' ')).lower()
            bottom_name = '_'.join(pair['bottom'].split(' ')).lower()
            print(f"\nTop_name: {top_name}")
            print(f"Bottom_name: {bottom_name}")

            # Fetch top and bottom outfits from the database
            top_outfit = Outfit.objects.get(user=user, name=top_name)
            bottom_outfit = Outfit.objects.get(user=user, name=bottom_name)

            # Generate color pair
            color_pair = f"{top_outfit.color}-{bottom_outfit.color}"

            # Save to OutfitPlan table
            OutfitPlan.objects.create(
                user=user,
                date=start_date + timedelta(days=day_index - 1),  # Increment date by day index
                top=top_outfit,
                bottom=bottom_outfit,
                color=color_pair
            )

        outfit_plans = OutfitPlan.objects.filter(user=user)
        pairs = [
            {
                'top': {'image': plan.top.image, 'name': plan.top.name},
                'bottom': {'image': plan.bottom.image, 'name': plan.bottom.name}
            }
            for plan in outfit_plans
        ]

        #     pairs.append({
        #         'top': {
        #             'filename': top_outfit.image
        #         },
        #         'bottom': {
        #             'filename': bottom_outfit.image
        #         }
        #     })

        # print('\nPairs:', pairs)

        return render(request, 'plan_your_outfit.html', {'pairs': pairs})



def generate_filename(user, category):
    """
    Generate a unique filename for the given category (e.g., 'shirt', 'trouser') 
    for a specific user.
    """
    if category.lower() == 'top':
        prefix = 'shirt'
    elif category.lower() == 'bottom':
        prefix = 'trouser'
    else:
        prefix = 'item'

    # Filter existing items by the user and category
    existing_items = Outfit.objects.filter(user=user, category=category)

    if existing_items.exists():
        # Extract numbers from existing filenames for the user and find the max
        last_number = max(
            [
                int(item.name.split('_')[-1])
                for item in existing_items
                if '_' in item.name and item.name.split('_')[-1].isdigit()
            ],
            default=0
        )
    else:
        last_number = 0

    # Increment the number for the new filename
    new_number = last_number + 1
    return f"{prefix}_{new_number}"


def wardrobe_and_collections(request):
    invalid_extensions = []
    outfits = []

    if request.method == 'POST':
        images = request.FILES.getlist('image')
        if not images:
            return HttpResponse("No images uploaded.")
            # return render(request, 'wardrobe_and_collections.html', {
            #     'invalid_extensions': invalid_extensions,
            #     'outfits': outfits,
            # })

        # Allowed extensions
        valid_extensions = ['jpeg', 'jpg', 'png']
        invalid_extensions = []
        outfits = []
        invalid = []

        # Validate extensions
        for image in images:
            ext = image.name.split('.')[-1].lower()
            if ext not in valid_extensions:
                invalid_extensions.append(image.name)
            else:
                # Save valid images and classify them
                # Use your classify function here
                outfit = classify(image)
                if outfit == 'Invalid Image':
                    invalid.append(os.path.basename(image))
                else:
                    outfits.append(outfit)

                    print(request.user, outfit['category'])

                    # Assign a unique filename for the user
                    new_filename = generate_filename(request.user, outfit['category'])
                    

                    outfit = Outfit.objects.create(
                        user = request.user,
                        name = new_filename,
                        # image = os.path.join('outfits', f"{new_filename}.jpg"),
                        image = image,
                        color = outfit['color'],
                        category = outfit['category']
                        )
                

    # Fetch outfits for the authenticated user
    if request.user.is_authenticated:
        outfits_ = Outfit.objects.filter(user=request.user)

    return render(request, 'wardrobe_and_collections.html', {
        'outfits': outfits_,
        'invalid_extensions': invalid_extensions,
    })

def delete_outfit(request, outfit_id):
    # Get the outfit object or return a 404 if not found
    outfit = get_object_or_404(Outfit, id=outfit_id, user=request.user)
    
    if request.method == 'POST':

        #Get the image path
        image_path = outfit.image.path

        # Delete the outfit from the database
        outfit.delete()

        if os.path.exists(image_path):
            os.remove(image_path)
        # Provide a success message to the user
        messages.success(request, "Outfit deleted successfully.")

        # Redirect back to the collections page
        return redirect(reverse('wardrobe:wardrobe_and_collections'))
    
    # If the request method isn't POST, redirect back to the collections page
    return redirect(reverse('wardrobe:wardrobe_and_collections'))

def plan_your_outfit(request):
    user = request.user
    action = request.GET.get('action')

    if action == 'generate':

        existing_plan = {}
        outfits = Outfit.objects.filter(user=user)
        existing_outfit_table = OutfitPlan.objects.filter(user=user).order_by('date')
        if existing_outfit_table.exists():
            for index, plan in enumerate(existing_outfit_table, start=1):
                day_key = f'day {index}'
                existing_plan[day_key] = {
                    'top' : f'{plan.top.name} ({plan.top.color})',
                    'bottom' : f'{plan.bottom.name} ({plan.bottom.color})'
                }

        print('\nExisting Plan:',existing_plan)
        OutfitPlan.objects.all().delete()
        
        collections = {
            'top': [],
            'bottom': []
        }

        for outfit in outfits:
            entry = {
                'filename': outfit.name,
                'color': outfit.color
            }

            if outfit.category == 'top':
                collections['top'].append(entry)
            elif outfit.category == 'bottom':
                collections['bottom'].append(entry)

        print('\nCollections:', collections)
                    
        response = recommendation.recommend(collections, existing_plan)

        print('\nResponse:', response)

        # Pair the tops and bottoms for display
        pairs = []
        start_date = date.today()

        for day_index, pair in enumerate(response.values(), start=1):
            top_name = '_'.join(pair['top'].split(' ')).lower()
            bottom_name = '_'.join(pair['bottom'].split(' ')).lower()
            print(f"\nTop_name: {top_name}")
            print(f"Bottom_name: {bottom_name}")

            # Fetch top and bottom outfits from the database
            top_outfit = Outfit.objects.get(user=user, name=top_name)
            bottom_outfit = Outfit.objects.get(user=user, name=bottom_name)

            # Generate color pair
            color_pair = f"{top_outfit.color}-{bottom_outfit.color}"

            # Save to OutfitPlan table
            OutfitPlan.objects.create(
                user=user,
                date=start_date + timedelta(days=day_index - 1),  # Increment date by day index
                top=top_outfit,
                bottom=bottom_outfit,
                color=color_pair
            )

    outfit_plans = OutfitPlan.objects.filter(user=user)
    
    pairs = [
        {
            'top': {'image': plan.top.image, 'name': plan.top.name},
            'bottom': {'image': plan.bottom.image, 'name': plan.bottom.name}
        }
        for plan in outfit_plans
    ]


    return render(request, 'plan_your_outfit.html', {'pairs': pairs})
         