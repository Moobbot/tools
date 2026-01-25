import os
from yt_dlp import YoutubeDL


def download_video(url, output_folder="downloads"):
    """
    Download a video from a given URL.

    Args:
        url (str): The URL of the video.
        output_folder (str): The folder to save the downloaded video.
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define path to local ffmpeg
    ffmpeg_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "ffmpeg_711", "bin"
    )

    # yt-dlp options for optimal quality
    ydl_opts = {
        "ffmpeg_location": ffmpeg_path,
        "outtmpl": os.path.join(
            output_folder, "%(title)s.%(ext)s"
        ),  # Save as title.extension
        "format": "bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio/best",  # Download highest quality video and audio (prefer m4a for compatibility)
        "quiet": False,  # Show download progress
        "merge_output_format": "mp4",  # Merge video and audio as MP4
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
        print(f"Download completed: {url}")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")


def batch_download(urls, output_folder="downloads"):
    """
    Download multiple videos from a list of URLs.

    Args:
        urls (list): A list of video URLs.
        output_folder (str): The folder to save the downloaded videos.
    """
    for url in urls:
        download_video(url, output_folder)


if __name__ == "__main__":
    # git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
    # List of video URLs
    video_urls = [
        "https://www.youtube.com/watch?v=QFwIWcc5OmA",
    ]

    # Folder to save videos
    output_directory = "download/videos"

    # Start downloading videos
    batch_download(video_urls, output_directory)
