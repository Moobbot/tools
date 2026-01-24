from pydub import AudioSegment

AudioSegment.converter = r"D:\Work\Clients\tools\ffmpeg_711\bin\ffmpeg.exe"
AudioSegment.ffprobe   = r"D:\Work\Clients\tools\ffmpeg_711\bin\ffprobe.exe"

print("ffmpeg path:", AudioSegment.converter)
print("ffprobe path:", AudioSegment.ffprobe)

input_file = "p11.m4a"
output_file = "p11.mp3"

audio = AudioSegment.from_file(input_file, format="m4a")
audio.export(output_file, format="mp3")
print(f"Converted {input_file} to {output_file}")