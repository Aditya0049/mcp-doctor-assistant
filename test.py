import openai

openai.api_key = "sk-Lm29aYjdfgO1tW4pXs93mHzZqK7UyPe3Q0lNKw9cXvJH"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="What is the meaning of love?",
    max_tokens=50
)

print(response.choices[0].text.strip())
