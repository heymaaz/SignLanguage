import os
from flask import Flask
from flask import jsonify
from flask import Response, stream_with_context
from flask_cors import CORS

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


app = Flask(__name__)
# Allow all origins for development purposes
CORS(app, resources={r"/url/*": {"origins": "*"}})

mock_glosses = [
    {"time": "00:00:00.000", "gloss": "FIVE TECHNOLOGY MYTHS WRONG MORE SIGNAL BARS"},
    {"time": "00:00:02.940", "gloss": "MORE BARS BETTER SERVICE"},
    {"time": "00:00:04.920", "gloss": "PHONE SHOW HOW CLOSE"},
    {"time": "00:00:06.600", "gloss": "CELL-TOWER NEAR NOT"},
    {"time": "00:00:08.580", "gloss": "SPEED FULL SIGNAL STILL FEEL SLOW"},
    {"time": "00:00:10.740", "gloss": "IF NETWORK BUSY AIRPLANE MODE"},
    {"time": "00:00:12.660", "gloss": "CHARGE PHONE FAST TECHNICALLY"},
    # Add the rest of your mock glosses here...
]


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/url/<url>')

def download_subs(url):
    import yt_dlp
    ydl_opts = {
        'writesubtitles': True,
        'subtitleslangs': ['en'],  # Specify the language code for the subtitles you want to download
        'skip_download': True,  # Skip downloading the video
        'writeautomaticsub': True,  # Write the automatically generated subtitle file
        'outtmpl': 'subtitles/%(id)s.%(ext)s', # Save to subtitles folder
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_id = info_dict.get('id', None)
        subtitle_file_path = f'subtitles/{video_id}.en.vtt'  # Path for subtitle file

        if video_id:
            if os.path.exists(subtitle_file_path):
                print('File already exists:', subtitle_file_path)
                filename = subtitle_file_path.split('.')[0]
            else:
                ydl.download([video_id])
                filename = ydl.prepare_filename(info_dict).split('.')[0]

        print(filename)
        
        def generate(subtitles_with_time):
            for gloss_data in mock_glosses:
                print(gloss_data)
                yield f"data: {json.dumps(gloss_data)}\n\n"
            '''
            for subtitle_with_time in subtitles_with_time:
                #print(subtitle_with_time)
                completion = client.chat.completions.create(
                #model="gpt-4",
                model="gpt-4-turbo-preview",
                #model="ft:gpt-3.5-turbo-0125:personal:gloss-2:99E2oJOT",
                messages=[
                    {"role": "system", "content": """
                    You are a sign language translator, skilled in translating English to BSL GLOSS. 
                    You should respond to the prompts only with the BSL GLOSS after conversion. 
                    Don't worry about punctuation or capitalisation but keep the new line characters in the same place.
                    You should keep the same number of lines as the subtitles. number of lines are: """+str(len(subtitles_with_time))+"""
                    which can be found in the subtitles using the new line character \n.
                    Try to keep the glosses short and simple.
                    FOr example, if the subtitle is "Hello, how are you?", the gloss should be "HELLO HOW YOU"
                    If the subtitle is "I am fine \n thank you", the gloss should be "FINE \n THANK YOU" keeping the new line character
                    Remember you can't add or remove new lines. If you do then score will be deducted by 100.
                    Although you keep the new lines, you should summarise the subtitles along multiple lines, but keep the same number of lines.
                    If gloss is not available, use fingerspelling. You can only use the following gloss- """
                    +', '.join(gloss_dict.keys())},
                    {"role": "user", "content": subtitle_with_time["sentence"]}
                ]
                )
                if completion.choices[0].message:
                    gloss_message = completion.choices[0].message.content
                    yield f"data: {json.dumps({'time': subtitle_with_time['time'], 'gloss': gloss_message})}\n\n"
            '''


        if filename:
            from openai import OpenAI
            client = OpenAI()
            # get gloss dict from with open('SignMappings/words.json') as file:
            with open('SignMappings/updated_mappings.json') as file:
                gloss_dict = json.load(file)

            vtt_content = open(filename+'.en.vtt', 'r').read()
            
            subtitles_with_time = extract_sentences_with_time(vtt_content)

            if subtitles_with_time:
                # Wrap the generator with stream_with_context to keep the app context
                return Response(stream_with_context(generate(subtitles_with_time)), mimetype='text/event-stream')
        return 'No subtitles found'
    

if __name__ == '__main__':
    app.run()