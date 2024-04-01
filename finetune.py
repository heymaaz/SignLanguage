import jsonlines

# Load the data
with jsonlines.open('gloss.jsonl') as reader:
    gloss_jsonl = [obj for obj in reader]

converted_jsonl = []

system_message = {
    "role": "system",
    "content": "You are a sign language translator, skilled in translating English to BSL GLOSS. You should respond to the prompts only with the BSL GLOSS after conversion. Don't worry about punctuation. If gloss is not available, use fingerspelling."
}

for item in gloss_jsonl:
    new_item = {
        "messages": [
            system_message,
            {"role": "user", "content": item["text"]},
            {"role": "assistant", "content": item["gloss"]}
        ]
    }
    converted_jsonl.append(new_item)

# Save the data
with jsonlines.open('gloss_converted.jsonl', 'w') as writer:
    writer.write_all(converted_jsonl)


