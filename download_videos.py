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

    # yt-dlp options for optimal quality
    ydl_opts = {
        "outtmpl": os.path.join(
            output_folder, "%(title)s.%(ext)s"
        ),  # Save as title.extension
        "format": "bestvideo[height<=1080]+bestaudio/best",  # Prefer 1080p, fallback to best available
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
        "https://www.youtube.com/watch?v=goyxrroH--Q",  # Example YouTube video
        # "https://www.tiktok.com/@user/video/1234567890",  # Example TikTok video
        "https://vtv.vn/video/cong-nghe-doi-song-khi-nguoi-tre-lam-khoa-hoc-93481.htm?gidzl=4RL_EsGYtnOMgdirPpdP6HUeVJvxRTXE2FyfFozWZHW9f7bkBpFRJbYcUJWiDebFMAHvR6H2ffKKOIFR5m",  # Direct video link
        "https://vtv.vn/video/cong-nghe-doi-song-co-che-dac-thu-khuyen-khich-doanh-nghiep-doi-moi-sang-tao-98733.htm?gidzl=GflSLu12o455XDXPWrdEJaI6s5EV3SaOMz6CKii0d4vQYjm3orFA60k8t5N8LfWP2uhS0MJrw24lXKFCG0",
    ]

    # Folder to save videos
    output_directory = "download/videos"

    # Start downloading videos
    batch_download(video_urls, output_directory)
