from flask import Flask
import json

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
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_id = info_dict.get('id', None)
        if video_id:
            ydl.download([video_id])
            filename = ydl.prepare_filename(info_dict).split('.')[0]
            #return filename + '.en.vtt'
        #return None
        if filename:
            from openai import OpenAI
            client = OpenAI()
            # get gloss dict from with open('SignMappings/words.json') as file:
            with open('SignMappings/updated_mappings.json') as file:
                gloss_dict = json.load(file)

            subtitle = open(filename+'.en.vtt', 'r').read()
            if subtitle:
                completion = client.chat.completions.create(
                #model="gpt-4",
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": "You are a sign language translator, skilled in translating English to BSL GLOSS. You should respond to the following prompts only with the BSL GLOSS after convertion. Don't worry about punctuation. GLOSS can only be from these words: "+', '.join(gloss_dict.keys())+". If gloss is not available, use fingerspelling. For example, if the prompt is 'Hello, how are you?', you should respond with 'hello how you'. if the prompt is 'I am good', you should respond with 'good'. if good is not available, you should respond with 'g o o d'. If machine is not available, you should respond with 'm a c h i n e'."},
                    {"role": "user", "content": "Here are the subtitles for the video: "+subtitle}
                ]
                )

                return(completion.choices[0].message.content)
                #return f'Subtitles file saved as {filename}.en.vtt'
            else: return 'file not found'
        return 'No subtitles found'
    

if __name__ == '__main__':
    app.run()