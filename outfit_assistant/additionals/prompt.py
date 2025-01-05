
def generate_prompt(preference):
    prompt = f"""

Generate a list of 5  {preference['dress_type']} outfit combinations for a {preference['gender']}, {preference['body_shape']} body shape, {preference['skin_tone']} skin tone, and {preference['height']} height.
Each outfit should focus on pairing colors thoughtfully to create a polished, professional look.
Consider options like well-matched suits, shirts, trousers, and accessories, using color combinations that highlight the skin tone and complement the face and body shape.
Ensure each suggestion balances style with classic, sophisticated formality suitable for various professional settings.

The output should be structured in JSON format, adhering strictly to the following guidelines:

Output format:
    {{ "shirt 1" : "pant 1" }},
    {{ "shirt 2" : "pant 2" }},
    {{ "shirt 3" : "pant 3" }}

Generate a list of 5 pairs of well and good combination of outfit.
Each shirt name should also clearly indicate the shirt and color (e.g., "pale pink shirt").
Each pant name should also clearly indicate the pant and color (e.g., "charcoal gray pant").
There should not be any brand name (e.g., "oxford" )
If it is a casual wear you can aslo suggest t-shirt or any kind of casual dress that is in trend.
Make sure that there should not be any brand
    
Ensure that the color combinations are well-coordinated and suitable for a classic, sophisticated formal setting.
The outfit pairings should be easy for the user to understand and follow for a stylish and professional look.

There should not be more than 6 suggestions.
The output should be in the above json format. The should not be any other extra content like explanation.
Ensure that there are no additional explanations or content outside of the JSON structure.

    """
    return prompt
