import yt_dlp

def download_subtitles(url):
    ydl_opts = {
        'writesubtitles': True,
        'subtitleslangs': ['en'],  # Specify the language code for the subtitles you want to download
        'skip_download': True,  # Skip downloading the video
        'writeautomaticsub': True,  # Write the automatically generated subtitle file
        'outtmpl': 'subtitles/%(id)s.%(ext)s',#save to subtitles folder
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_id = info_dict.get('id', None)
        if video_id:
            ydl.download([video_id])
            filename = ydl.prepare_filename(info_dict).split('.')[0]
            return filename + '.en.vtt'
        return None


# call the function
url = input("Enter File url")#'https://www.youtube.com/watch?v=OMbNoo4mCcI'
filename= download_subtitles(url)
if filename:
    print(f'Subtitles file saved as {filename}')


