import json

# Load the JSON file
with open('api_key.json') as f:
    data = json.load(f)

# Extract the API key
api_key = data['OPENAI_API_KEY']

print(api_key)