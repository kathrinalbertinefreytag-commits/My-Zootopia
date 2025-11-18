import json
import webbrowser
import os

# Paths To Files
JSON_FILE = "animals_data.json"
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"


# 1. FUNCTION FOR SERIALIZING A SINGLE ANIMAL
def serialize_animal(animal_obj):
    name = animal_obj.get("name", "")
    diet = animal_obj.get("diet", "")
    locations = animal_obj.get("locations", [])
    type_ = animal_obj.get("type", "")

    location_text = ", ".join(locations) if locations else ""

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'

    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    if location_text:
        output += f'      <strong>Location:</strong> {location_text}<br/>\n'
    if type_:
        output += f'      <strong>Type:</strong> {type_}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


# 2. LOAD JSON DATA
try:
    with open(JSON_FILE, "r") as f:
        animals_data = json.load(f)
except FileNotFoundError:
    print(f"Error: {JSON_FILE} not found.")
    exit()


# 3. BUILD HTML LIST ITEMS USING THE FUNCTION
animals_info = ""
for animal in animals_data:
    animals_info += serialize_animal(animal)


# 4. LOAD TEMPLATE
try:
    with open(TEMPLATE_FILE, "r") as f:
        template = f.read()
except FileNotFoundError:
    print(f"Error: {TEMPLATE_FILE} not found.")
    exit()


# 5. REPLACE PLACEHOLDER
if "__REPLACE_ANIMALS_INFO__" not in template:
    print("Warning: Placeholder '__REPLACE_ANIMALS_INFO__' not found in template.")

output_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)


# 6. WRITE OUTPUT FILE
with open(OUTPUT_FILE, "w") as f:
    f.write(output_html)

print(f"HTML file '{OUTPUT_FILE}' generated successfully!")


# 7. OPEN IN BROWSER
full_path = os.path.abspath(OUTPUT_FILE)
webbrowser.open(f"file://{full_path}")