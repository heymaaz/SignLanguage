from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a sign language translator, skilled in translating English to BSL GLOSS. You should respond to the following prompts only with the BSL GLOSS after convertion. Don't worry about punctuation."},
    {"role": "user", "content": "approximately 70 million children don't"}
  ]
)

print(completion.choices[0].message.content)