import json

# Load your data from a JSON file
with open('your_file.json', 'r') as f:
    data = json.load(f)

formatted_data = []

for entry in data:
    prompt = entry['Patient']
    completion = entry['Doctor']
    
    formatted_entry = {"prompt": prompt, "completion": completion}
    
    formatted_data.append(formatted_entry)

# Save the formatted data to a new JSON file
with open('formatted_data.json', 'w') as f:
    for item in formatted_data:
        f.write(json.dumps(item) + '\n')
