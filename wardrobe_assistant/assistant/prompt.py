
def generate_prompt(collections):

    print('\nGenerating Prompt')

    # Generate the formatted wardrobe details without .jpg extension
    top_details = "\n".join([f"{i+1}.  {item['filename'].split('.')[0].capitalize().replace('_', ' ')}: {item['color']}" 
                              for i, item in enumerate(collections['top'])])
    bottom_details = "\n".join([f"{i+1}.  {item['filename'].split('.')[0].capitalize().replace('_', ' ')}: {item['color']}" 
                                 for i, item in enumerate(collections['bottom'])])

    # Define the main prompt structure
    prompt = f"""
Create a weekly outfit plan using the provided wardrobe collection, ensuring that each pairing is stylish, trendy, and color-coordinated.
Each outfit should consist of one top and one bottom, carefully chosen to provide a balanced mix of casual and semi-formal styles, making each day’s outfit unique and visually appealing.

Key Focus Areas:

**Focus on Neutral colours:**
The basic of any fashion is to focus on neutral colours because those colourswill make other colours prominent.
So, when it comes to wearing neutral colours,always have at least one base in your overall outfits like wearing a base layer of neutral colour when you are wearing a blazer on it or a neutral T-shirt for dark  pants and shoes.
Neutral colours like white, grey, sky blue, and khaki will be veryattractive on any occasion for men. These are the colours that go with other colours, this is the base foundation for any outfits and carry outstanding stylingessence around.

**Enhanced Color Harmony:** Prioritize color combinations that complement each other beautifully or create interesting contrasts for an elevated look. Use contemporary color trends, such as earthy tones, soft pastels, and vibrant accents, to add variety and appeal. Pair colors thoughtfully—like beige with navy or olive with cream—to ensure each outfit looks sophisticated and cohesive.

**Trendy and Cohesive Combinations:** Use popular color schemes to create a stylish and modern wardrobe plan. Try monochromatic pairings for a sleek look or contrasting hues for a bold statement. Employ color schemes such as complementary or analogous palettes to make each day’s outfit unique. Consider popular color pairings like muted greens with neutrals or bold colors like burgundy with lighter shades for a refreshing contrast.

**Occasion-Specific Variety:** Curate a balance between casual looks for relaxed days and semi-formal outfits for a polished appearance. Ensure that the color combinations provide a cohesive flow throughout the week, adding freshness and a sense of style to each day’s outfit.

Objective: Generate a weekly outfit plan that goes beyond basic matching, focusing on highly appealing color combinations to elevate each look. Each day’s outfit should feature a thoughtfully selected color pairing that enhances the overall look, aligned with the latest trends for a modern and stylish appearance.

Wardrobe details:

**Tops:**
{top_details}

**Bottoms:**
{bottom_details}

Generate a 5-day outfit plan.

The response should be strictly in the below mention json format.
Output format:
{{
    day 1: {{top: top name, bottom: bottom name}},
    day 2: {{top: top name, bottom: bottom name}},
    day 3: {{top: top name, bottom: bottom name}},
    day 4: {{top: top name, bottom: bottom name}},
    day 5: {{top: top name, bottom: bottom name}}
}}

The top name should be the shirt name like Shirt 1 and not the color of the shirt.
The bottom name should be the pant name like Trouser 1 and not the color of the shirt.

Ensure that the color combinations are well-coordinated and suitable for a classic, sophisticated formal setting.

The output should be in the json format. There should not be any other extra content like explanation.
Ensure that there are no additional explanations or content outside the JSON structure.
"""

    # Print the final prompt to verify formatting
    # print(prompt)
    return prompt

def regeneration_prompt(collections, existing_plan):

    print('\nRegeneration Prompt')
    print('\nPrevious plan:',existing_plan)

    # Generate the formatted wardrobe details without .jpg extension
    top_details = "\n".join([f"{i+1}.  {item['filename'].split('.')[0].capitalize().replace('_', ' ')}: {item['color']}" 
                              for i, item in enumerate(collections['top'])])
    bottom_details = "\n".join([f"{i+1}.  {item['filename'].split('.')[0].capitalize().replace('_', ' ')}: {item['color']}" 
                                 for i, item in enumerate(collections['bottom'])])

    # Define the prompt structure for regenerating suggestions
    prompt = f"""
The previously generated weekly outfit plan as follow:

{existing_plan}

The previous plan is not satisfactory.
Provide a new and improved weekly outfit plan with enhanced color pairings and better coordination than the previous response.
Focus more on creative and stylish combinations that stand out and align with the guidelines below

Regenerate a new weekly outfit plan using the provided wardrobe collection, carefully selecting one top and one bottom for each day.
Each pairing should showcase a stylish, polished look with an emphasis on excellent color coordination and aesthetic appeal, ensuring that this plan surpasses the previous one.

Key Focus Areas:

**Focus on Neutral colours:**
The basic of any fashion is to focus on neutral colours because those colourswill make other colours prominent.
So, when it comes to wearing neutral colours,always have at least one base in your overall outfits like wearing a base layer of neutral colour when you are wearing a blazer on it or a neutral T-shirt for dark  pants and shoes.
Neutral colours like white, grey, sky blue, and khaki will be veryattractive on any occasion for men. These are the colours that go with other colours, this is the base foundation for any outfits and carry outstanding stylingessence around.

**Enhanced Color Harmony:** Prioritize color combinations that complement each other beautifully or create interesting contrasts for an elevated look. Use contemporary color trends, such as earthy tones, soft pastels, and vibrant accents, to add variety and appeal. Pair colors thoughtfully—like beige with navy or olive with cream—to ensure each outfit looks sophisticated and cohesive.

**Trendy and Cohesive Combinations:** Use popular color schemes to create a stylish and modern wardrobe plan. Try monochromatic pairings for a sleek look or contrasting hues for a bold statement. Employ color schemes such as complementary or analogous palettes to make each day’s outfit unique. Consider popular color pairings like muted greens with neutrals or bold colors like burgundy with lighter shades for a refreshing contrast.

**Occasion-Specific Variety:** Curate a balance between casual looks for relaxed days and semi-formal outfits for a polished appearance. Ensure that the color combinations provide a cohesive flow throughout the week, adding freshness and a sense of style to each day’s outfit.

Objective: Generate a weekly outfit plan that goes beyond basic matching, focusing on highly appealing color combinations to elevate each look. Each day’s outfit should feature a thoughtfully selected color pairing that enhances the overall look, aligned with the latest trends for a modern and stylish appearance.

Wardrobe details:

**Tops:**
{top_details}

**Bottoms:**
{bottom_details}

Generate a 5-day outfit plan.

The response should be strictly in the below mention json format.
Output format:
{{
    day 1: {{top: top name, bottom: bottom name}},
    day 2: {{top: top name, bottom: bottom name}},
    day 3: {{top: top name, bottom: bottom name}},
    day 4: {{top: top name, bottom: bottom name}},
    day 5: {{top: top name, bottom: bottom name}}
}}

The top name should be the shirt name like Shirt 1 and not the color of the shirt.
The bottom name should be the pant name like Trouser 1 and not the color of the shirt.

Ensure that the color combinations are well-coordinated and suitable for a classic, sophisticated formal setting.

The output should be in the json format. There should not be any other extra content like explanation.
Ensure that there are no additional explanations or content outside the JSON structure.
"""

    # Print the final prompt to verify formatting
    # print(prompt)
    return prompt

