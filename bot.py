import openai
import os


# Set the API key for the openai module

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


# print(os.environ["api_key"])
openai.api_key = os.environ["api_key"]

with open("fina_add.txt", "r") as f:
    code = f.read()

# Use the OpenAI API
response = openai.Completion.create(
    engine="davinci",
    prompt="Explain the following code:\n\n" + code,
    max_tokens=1000,
    temperature=0.7,
)

# Extract the explanation
explanation = response.choices[0].text

# Write the output file
with open("explanation.txt", "w") as f:
    f.write(explanation)
