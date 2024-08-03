import json

# Load JSON data from file
with open('resume.json', 'r') as file:
    data = json.load(file)

# Print the data
print(json.dumps(data, indent=4))