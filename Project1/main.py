import os
import openai
from data import papers
from process import *

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv('API_KEY')

engine = "text-davinci-003"
max_tokens = 1000
temperature = 0.1

paper = papers.transformer

prompt = 'Summarize the following research paper:'

## This will cause an error, split the paper string so the length is less than 13000
api_prompt = f'{prompt}\n\n{paper}'

response = openai.Completion.create(engine=engine, prompt=prompt,temperature=temperature, max_tokens=max_tokens)

print(response.choices[0].text)