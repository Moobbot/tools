import subprocess
import os


def mp4_to_mp3(mp4_path, mp3_path=None):
    if not mp3_path:
        mp3_path = os.path.splitext(mp4_path)[0] + ".mp3"
    command = [
        "ffmpeg_711/bin/ffmpeg.exe",
        "-i",
        mp4_path,
        "-vn",  # no video
        "-ab",
        "192k",  # audio bitrate
        "-ar",
        "44100",  # audio sampling rate
        "-y",  # overwrite output file if it exists
        mp3_path,
    ]
    subprocess.run(command, check=True)
    print(f"Converted {mp4_path} to {mp3_path}")


# Example usage:
mp4_to_mp3("video.mp4")
