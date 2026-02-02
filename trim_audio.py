"""
Audio File Splitter

This script splits a long audio file into smaller chunks of specified duration.
It uses the pydub library to handle audio processing and requires ffmpeg to be installed.

Dependencies:
    - pydub: For audio processing
    - ffmpeg: Required by pydub for audio operations

Installation:
    1. Install pydub:
        pip install pydub

    2. Install ffmpeg:
        - Windows: Download from https://ffmpeg.org/download.html and add to PATH
        - Linux/macOS: sudo apt install ffmpeg

Usage:
    Place your audio file in the same directory as this script and update the filename
    in the code. The script will create an 'output_chunks' directory and save the
    split audio files there.

Output:
    - Creates an 'output_chunks' directory
    - Saves individual audio chunks as WAV/MP3 files named 'recording_part_X.mp3'
    where X is the chunk number
"""

import os

# Define path to local ffmpeg and add to PATH BEFORE importing pydub
ffmpeg_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "ffmpeg_711", "bin"
)
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ.get("PATH", "")

from pydub import AudioSegment

AudioSegment.converter = os.path.join(ffmpeg_path, "ffmpeg.exe")
AudioSegment.ffprobe = os.path.join(ffmpeg_path, "ffprobe.exe")
import math

# Load the input audio file
audio = AudioSegment.from_file("test.m4a")

# Define chunk duration (30 minutes in milliseconds)
chunk_length_ms = 60 * 60 * 1000  # 30 minutes = 1800 seconds

# Calculate total duration of the audio file
total_length_ms = len(audio)

# Calculate number of chunks needed
num_chunks = math.ceil(total_length_ms / chunk_length_ms)

# Create output directory if it doesn't exist
os.makedirs("output_chunks", exist_ok=True)

# Split audio into chunks and save each chunk
for i in range(num_chunks):
    # Calculate start and end times for current chunk
    start = i * chunk_length_ms
    end = min((i + 1) * chunk_length_ms, total_length_ms)

    # Extract the chunk
    chunk = audio[start:end]

    # Save the chunk as MP3 file
    chunk.export(f"output_chunks/test_{i+1}.mp3", format="mp3")
    print(f"Đã xuất: test_{i+1}.mp3")

print("✅ Đã hoàn tất chia nhỏ file ghi âm.")
