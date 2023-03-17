import json
import openai

# Load the JSON file
try:
    with open('api_key.json') as f:
        data = json.load(f)
    openai.api_key = data['OPENAI_API_KEY']
except:
    print('Need to create api_key.json file with OPENAI_API_KEY')
    exit(1)

# list models
models = openai.Model.list()

# https://help.openai.com/en/articles/7039783-chatgpt-api-faq

# print the first model's id
mod = models.data[0].id

# create a completion
completion = openai.Completion.create(model=mod, prompt="Hello world")

# print the completion
print(completion.choices[0].text)

