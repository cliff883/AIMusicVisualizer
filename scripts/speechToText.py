from torch import seed
import whisper
import subprocess
from moviepy.editor import *
import moviepy.editor as mpe
from time_it import *
import json
import random
import math
import os
import sys
conf_path = os.getcwd()
sys.path.append(conf_path)

def combine_audio(vidname, audname, outname, fps=60): 
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

def main():
    list = time_it()
    print(list)
    model = whisper.load_model("medium")
    audio = model.transcribe("../server/files/in_file.mp3")
    phrases = audio["text"].split('.')
    print(audio)
    f = open("subtitles.srt", "a")
    f.truncate(0)
    
    f.write(str(1))
    f.write("\n")
    f.write("00:" + "%02d" % (list[0][0] / 60)+":"+"%02d" %(list[0][0] % 60)+",00" + " --> 00:" + "%02d" % (list[0][1] / 60)+":"+"%02d" %(list[0][1] % 60)+",00")
    f.write("\n")
    f.write(str(list[0][2]).strip())
    f.write("\n\n")
    
    for i in range(2, len(list) + 1):
        f.write(str(i))
        f.write("\n")
        f.write("00:" + "%02d" % (list[i-2][1] / 60)+":"+"%02d" %(list[i-2][1] % 60)+",00" + " --> 00:" + "%02d" % (list[i-1][1] / 60)+":"+"%02d" %(list[i-1][1] % 60)+",00")
        f.write("\n")
        f.write(str(list[i - 1][2]).strip())
        f.write("\n\n")
    f.close()
    
    n_animation_prompts = {}
    for i in range(len(list)):
        n_animation_prompts[str(math.floor(list[i][0] * 15))] = list[i][2]
    n_max_frames = math.floor(list[len(list)-1][1] * 15)
    n_seed = random.randint(10000000,99999999)
    
    # with open("settingsTemplate.json") as j:
    #     settingsData = json.load(j)
    #     settingsData["animation_prompts"] = n_animation_prompts
    #     settingsData["max_frames"] = n_max_frames
    #     settingsData["seed"] = n_seed
    #     with open("./runSettings.txt", "a") as jw:
    #         jw.write(json.dumps(settingsData))
                
    
    # subprocess.run(["ffmpeg", "-i", "./output/22-10/TaskName/*.mp4", "-vf", "subtitles=subtitles.srt", "temp-output.mp4"])
    # combine_audio("temp-output.mp4", "../server/files/in_file.mp3", "../server/files/out_file.mp4")
main()