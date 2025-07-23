import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyDyPDQICiK0_4gSu-tck8tTWGD9NazwWnU")

models = genai.list_models()

for model in models:
    print(f"Model name: {model.name}")
    print(f"  Description: {model.description}")
    print(f"  Input token limit: {model.input_token_limit}")
    print(f"  Output token limit: {model.output_token_limit}")
    print("-" * 50)
