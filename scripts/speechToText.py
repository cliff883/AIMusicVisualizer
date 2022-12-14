import whisper
import json
import re
import subprocess
from moviepy.editor import *
import moviepy.editor as mpe
import numpy as np
import cv2
from time_it import *
from textToImage import textToImage

def combine_audio(vidname, audname, outname, fps=60): 
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

def main():
    list = time_it()
    print(list)
    model = whisper.load_model("base")
    audio = model.transcribe("../server/files/in_file.mp3")
    phrases = re.split(r"[,.]", audio["text"])
    phrases1 = audio["text"].split('.')
    print(audio)
    print(phrases1)
    f = open("subtitles.srt", "a")
    f.truncate(0)

    f.write(str(1))
    f.write("\n")
    f.write("00:" + "%02d" % (list[0][0] / 60)+":"+"%02d" %(list[0][0] % 60)+",00" + " --> 00:" + "%02d" % (list[0][1] / 60)+":"+"%02d" %(list[0][1] % 60)+",00")
    f.write("\n")
    f.write(str(phrases1[0]).strip())
    f.write("\n\n")
    
    for i in range(2, len(phrases1)):
        f.write(str(i))
        f.write("\n")
        f.write("00:" + "%02d" % (list[i-2][1] / 60)+":"+"%02d" %(list[i-2][1] % 60)+",00" + " --> 00:" + "%02d" % (list[i-1][1] / 60)+":"+"%02d" %(list[i-1][1] % 60)+",00")
        f.write("\n")
        f.write(str(phrases1[i - 1]).strip())
        f.write("\n\n")
    f.close()
    
    #subprocess.run(["ffmpeg", "-loop", "1", "-r", "1", "-i", "sampleimage.png", "-i", "Fly_Me_to_the_Moon.mp3", "-c:a", "copy","-shortest",
     #               "-c:v", "libx264", "output.mp4"])
    subprocess.run(["ffmpeg", "-i", "output.mp4", "-vf", "subtitles=subtitles.srt", "output1.mp4"])
    combine_audio("output1.mp4", "Fly_Me_to_the_Moon.mp3", "final_output.mp4")
main()