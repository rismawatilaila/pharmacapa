"""
Render PharmaCAPA_AI_Video_Tutorial.mp4 dengan mengekstrak 533 frames langsung via Pillow
dan mem-piping raw RGB ke ffmpeg bersama audio narasi bahasa Indonesia.
"""

import subprocess
import imageio_ffmpeg
import os
from PIL import Image

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
webp_path = "PharmaCAPA_AI_Video_Tutorial.webp"
audio_path = "narasi_tutorial.mp3"
output_mp4 = "PharmaCAPA_AI_Video_Tutorial.mp4"

im = Image.open(webp_path)
n_frames = getattr(im, "n_frames", 1)
w, h = im.size
print(f"Opening {webp_path}: {n_frames} frames, {w}x{h}")

duration_audio = 278.11  # 4m 38s
input_fps = n_frames / duration_audio
print(f"Calculated Input FPS: {input_fps:.4f} (Durasi total video: {duration_audio:.2f} detik)")

cmd = [
    ffmpeg_exe,
    "-y",
    "-f", "rawvideo",
    "-pix_fmt", "rgb24",
    "-s", f"{w}x{h}",
    "-r", f"{input_fps:.6f}",
    "-i", "pipe:0",
    "-i", audio_path,
    "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2,fps=25,format=yuv420p",
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "21",
    "-c:a", "aac",
    "-b:a", "128k",
    "-movflags", "+faststart",
    "-shortest",
    output_mp4
]

print("Launching ffmpeg pipe process...")
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for i in range(n_frames):
    im.seek(i)
    rgb_frame = im.convert("RGB")
    proc.stdin.write(rgb_frame.tobytes())
    if (i + 1) % 100 == 0 or i == n_frames - 1:
        print(f"Processed frame {i + 1}/{n_frames}...")

proc.stdin.close()
out, err = proc.communicate()

if proc.returncode == 0:
    size_mb = os.path.getsize(output_mp4) / (1024 * 1024)
    print(f"CONGRATULATIONS: Video MP4 successfully created as '{output_mp4}' ({size_mb:.2f} MB)")
else:
    print("FFmpeg error:", err.decode("utf-8", errors="ignore")[-1200:])
