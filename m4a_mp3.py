import os

# Define path to local ffmpeg and add to PATH BEFORE importing pydub
ffmpeg_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "ffmpeg_711", "bin"
)
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ.get("PATH", "")

from pydub import AudioSegment

AudioSegment.converter = os.path.join(ffmpeg_path, "ffmpeg.exe")
AudioSegment.ffprobe = os.path.join(ffmpeg_path, "ffprobe.exe")

print("ffmpeg path:", AudioSegment.converter)
print("ffprobe path:", AudioSegment.ffprobe)

input_file = "test.m4a"
output_file = "test.mp3"

audio = AudioSegment.from_file(input_file, format="m4a")
audio.export(output_file, format="mp3")
print(f"Converted {input_file} to {output_file}")
