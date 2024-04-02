import os
from flask import Flask
from flask import jsonify
import json
import re

def extract_sentences_with_time(vtt_content):
    sentences_with_time = []
    current_sentence = ""
    current_time = ""
    next_time = ""  # To hold the timestamp for a potential new block
    last_added_text = ""  # To avoid duplicating identical consecutive captions
    
    for line in vtt_content.split('\n'):
        if "-->" in line:
            if current_sentence and current_sentence != last_added_text:
                # Append the sentence with the previously stored timestamp
                sentences_with_time.append({"time": current_time if current_time else next_time, "sentence": current_sentence.strip()})
                last_added_text = current_sentence
                current_sentence = ""  # Reset for the next sentence
            
            # Update timestamps
            current_time = next_time if next_time else current_time
            next_time = line.split(" --> ")[0]
            continue
        
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:") or line.startswith("[Music]") or line.strip() == "":
            continue  # Skip headers and empty lines
        
        line_text = re.sub(r'<[^>]+>', '', line).strip()  # Remove HTML-like tags and their contents
        
        if line_text:
            if line_text != last_added_text:
                if current_sentence:
                    current_sentence += " " + line_text
                else:
                    # Update current_time to next_time when starting a new sentence block
                    current_time = next_time
                    current_sentence = line_text
    
    # Append the last sentence block if it exists and is not a duplicate
    if current_sentence and current_sentence != last_added_text:
        sentences_with_time.append({"time": current_time, "sentence": current_sentence.strip()})

    return sentences_with_time

vtt_content = open('subtitles/T4DePn8foj4.en.vtt', 'r').read()
extracted_sentences = extract_sentences_with_time(vtt_content)
for item in extracted_sentences:
    print(item)