from flask import Flask, render_template, request
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = 'mero-download'  # Define the download folder

# Ensure the download folder exists
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_urls = request.form['urls'].split(',')  # Allow multiple URLs (comma-separated)
    quality = request.form['quality']
    messages = []

    for video_url in video_urls:
        video_url = video_url.strip()  # Strip any extra spaces
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]',
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'quiet': True,  # Suppress output for user-friendly response
            'extract_flat': True,  # Get metadata without downloading
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=False)
                title = info_dict.get('title', 'Unknown')
                thumbnail = info_dict.get('thumbnail', None)

                # Handling duplicate file names
                file_name = f"{title}.mp3"
                i = 1
                while os.path.exists(os.path.join(DOWNLOAD_FOLDER, file_name)):
                    file_name = f"{title}_{i}.mp3"
                    i += 1

                # Now download the video
                ydl_opts['outtmpl'] = os.path.join(DOWNLOAD_FOLDER, file_name)
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])

            messages.append(f"Downloaded: {title}")
        except Exception as e:
            messages.append(f"Error downloading {video_url}: {str(e)}")

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
