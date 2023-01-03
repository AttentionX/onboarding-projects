import os
import openai

engine = "text-davinci-003"
max_tokens = 1000
temperature = 0.1

context = ''

while True:
    prompt = ''

    prompt = context += prompt

    response = openai.Completion.create(engine=engine, prompt=prompt,temperature=temperature, max_tokens=max_tokens)

    context += response

    print(index, response.choices[0].text)