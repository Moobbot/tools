import os
from yt_dlp import YoutubeDL


def download_youtube_mp3(youtube_url, output_folder="downloaded_mp3s"):
    """
    Download audio from a YouTube link and convert it to MP3.

    Args:
        youtube_url (str): The YouTube video URL.
        output_folder (str): The folder to save the MP3 file.
    """
    try:
        # Ensure the output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Define path to local ffmpeg
        ffmpeg_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "ffmpeg_711", "bin"
        )

        # yt-dlp options for audio extraction
        ydl_opts = {
            "ffmpeg_location": ffmpeg_path,
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "postprocessor_args": None,
            "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        }

        with YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading and converting: {youtube_url}")
            ydl.download([youtube_url])

        print("Download and conversion completed.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    youtube_link = input("Enter the YouTube link: ")
    download_youtube_mp3(youtube_link)
