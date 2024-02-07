from flask import Flask, send_file
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route('/convertToMp3', methods=['GET'])
def convert_to_mp3():
    video_url = "https://www.youtube.com/watch?v=LCCPL8rduL4&list=PL5ESsgnHGfa8d3EetmuUA8quawtJjEiH4&index=2"

    # Descarga el archivo de video y convierte a audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'input.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Envia el archivo de mp3
    return send_file('input.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# from flask import Flask, send_file
# from yt_dlp import YoutubeDL

# app = Flask(__name__)

# @app.route('/convertToMp3', methods=['GET'])
# def download_video():
#     video_url = "https://www.youtube.com/watch?v=-KwhLzNg9Wk"

#     # Descarga el archivo de video
#     ydl_opts = {
#         'format': 'bestvideo+bestaudio',
#         'outtmpl': 'video.%(ext)s',
#     }
#     with YoutubeDL(ydl_opts) as ydl:
#         ydl.download([video_url])

#     # Encuentra la extensión del archivo descargado
#     info_dict = YoutubeDL(ydl_opts).extract_info(video_url, download=False)
#     ext = info_dict.get('ext', 'mp4')

#     # Envia el archivo de video
#     return send_file(f'video.{ext}', as_attachment=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)