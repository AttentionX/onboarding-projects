import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv('API_KEY')

engine = "text-davinci-003"
max_tokens = 1000
temperature = 0.1

context = ''

index = 0
while True:
    print("Type Prompt: ")
    prompt = input()

    context += prompt

    response = openai.Completion.create(engine=engine, prompt=prompt,temperature=temperature, max_tokens=max_tokens)

    context += response

    print(index, response.choices[0].text)
    index += 1