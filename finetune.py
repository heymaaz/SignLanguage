
"""
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


"""
import re

def extract_sentences(vtt_content):
    sentences = []
    current_sentence = ""
    last_added = ""  # Keep track of the last added segment to avoid duplicates
    
    for line in vtt_content.split('\n'):
        # Remove timestamps and align instructions
        if "-->" in line or line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        
        # Remove HTML-like tags and their contents
        line_text = re.sub(r'<[^>]+>', '', line).strip()
        
        if not line_text or line_text == last_added:
            # Skip empty lines and duplicates
            continue
        
        if line_text.endswith(('.', '?', '!')):
            # End of a sentence
            current_sentence += " " + line_text
            sentences.append(current_sentence.strip())
            current_sentence = ""  # Reset for the next sentence
        else:
            # Mid-sentence or continuation
            if current_sentence and not current_sentence.endswith(line_text):
                current_sentence += " " + line_text
            elif not current_sentence:
                current_sentence = line_text
            
        last_added = line_text  # Update last added segment
    
    # Catch any trailing sentence without proper punctuation
    if current_sentence:
        sentences.append(current_sentence.strip())

    return sentences

# Example usage with your provided content
vtt_content = """
WEBVTT
Kind: captions
Language: en

00:00:03.600 --> 00:00:05.910 align:start position:0%
 
so<00:00:03.919><c> many</c><00:00:04.319><c> females</c><00:00:04.960><c> gathered</c><00:00:05.279><c> together</c><00:00:05.759><c> on</c>

00:00:05.910 --> 00:00:05.920 align:start position:0%
so many females gathered together on
 
00:00:05.920 --> 00:00:08.150 align:start position:0%
so many females gathered together on
this<00:00:06.080><c> cliff</c><00:00:06.720><c> inevitably</c><00:00:07.600><c> attract</c><00:00:08.000><c> the</c>

00:00:08.150 --> 00:00:08.160 align:start position:0%
this cliff inevitably attract the
 
00:00:08.160 --> 00:00:11.669 align:start position:0%
this cliff inevitably attract the
attention<00:00:08.960><c> of</c><00:00:09.200><c> a</c><00:00:09.360><c> rival</c><00:00:09.920><c> adult</c><00:00:10.400><c> male</c>

00:00:11.669 --> 00:00:11.679 align:start position:0%
attention of a rival adult male
 
00:00:11.679 --> 00:00:15.030 align:start position:0%
attention of a rival adult male
his<00:00:12.000><c> aim</c><00:00:12.400><c> is</c><00:00:12.639><c> to</c><00:00:12.880><c> defeat</c><00:00:13.360><c> scarface</c><00:00:14.559><c> and</c><00:00:14.719><c> take</c>

00:00:15.030 --> 00:00:15.040 align:start position:0%
his aim is to defeat scarface and take
 
00:00:15.040 --> 00:00:24.870 align:start position:0%
his aim is to defeat scarface and take
over<00:00:15.280><c> his</c><00:00:15.440><c> females</c>

00:00:24.870 --> 00:00:24.880 align:start position:0%
"""
sentences = extract_sentences(vtt_content)
for sentence in sentences:
    print(sentence+'\n')
