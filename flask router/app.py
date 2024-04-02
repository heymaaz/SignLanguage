from flask import Flask
from flask import jsonify
import json
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

app = Flask(__name__)

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
        if video_id:
            ydl.download([video_id])
            filename = ydl.prepare_filename(info_dict).split('.')[0]

        if filename:
            from openai import OpenAI
            client = OpenAI()
            # get gloss dict from with open('SignMappings/words.json') as file:
            with open('SignMappings/updated_mappings.json') as file:
                gloss_dict = json.load(file)

            vtt_content = open(filename+'.en.vtt', 'r').read()
            
            subtitles = extract_sentences(vtt_content)
            if subtitles:
                subtitle = ' '.join(subtitles)
                completion = client.chat.completions.create(
                #model="gpt-4",
                #model="gpt-4-turbo-preview",
                model="ft:gpt-3.5-turbo-0125:personal:gloss-2:99E2oJOT",
                messages=[
                    {"role": "system", "content": "You are a sign language translator, skilled in translating English to BSL GLOSS. You should respond to the prompts only with the BSL GLOSS after conversion. Don't worry about punctuation. If gloss is not available, use fingerspelling. You can only use the following gloss- "+', '.join(gloss_dict.keys())},
                    #{"role": "system", "content": "You are a sign language translator, skilled in translating English to BSL GLOSS. You should respond to the following prompts only with the BSL GLOSS after convertion. Don't worry about punctuation. GLOSS can only be from these words: "+', '.join(gloss_dict.keys())+". If gloss is not available, use fingerspelling. For example, if the prompt is 'Hello, how are you?', you should respond with 'hello how you'. if the prompt is 'I am good', you should respond with 'good'. if good is not available, you should respond with 'g o o d'. If machine is not available, you should respond with 'm a c h i n e'."},
                    {"role": "user", "content": "Here are the subtitles for the video: "+subtitle}
                ]
                )

                #return(completion.choices[0].message.content)
                # for each word in the completion, check if it is in the gloss_dict and return the gloss
                # if not, return the word as fingerspelling
                gloss = []
                for word in completion.choices[0].message.content.split():
                    if word.lower() in gloss_dict:
                        gloss.append(gloss_dict[word.lower()])
                    else:
                        # fingerspelling, but only for alphabetic characters
                        for letter in word:
                            if letter.isalpha():  # Check if the character is alphabetic
                                gloss.append(gloss_dict[letter.lower()])
                
                #return ' '.join(gloss)
                # return the gloss as a response in json format with index
                return jsonify({i+1: gloss[i] for i in range(len(gloss))})

                

                #return f'Subtitles file saved as {filename}.en.vtt'
            else: return 'file not found'
        return 'No subtitles found'
    

if __name__ == '__main__':
    app.run()