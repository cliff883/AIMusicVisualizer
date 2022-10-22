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
    #subprocess.run(["python3", "timestamp.py"])
    list = time_it()
    print(list)
    model = whisper.load_model("base")
    audio = model.transcribe("Fly_Me_to_the_Moon.mp3")
    phrases = re.split(r"[,.]", audio["text"])
    phrases1 = audio["text"].split('.')
    f = open("subtitles.srt", "a")
    f.truncate(0)
    time = open("timestamp.json")
    time_data = json.load(time)
    for i in range(1, len(phrases1)):
        f.write(str(i))
        f.write("\n")
        f.write("00:" + "%02d" % (list[i-1][0] / 60)+":"+"%02d" %(list[i-1][0] % 60)+",00" + " --> 00:" + "%02d" % (list[i-1][1] / 60)+":"+"%02d" %(list[i-1][1] % 60)+",00")
        f.write("\n")
        f.write(str(phrases1[i - 1]).strip())
        f.write("\n\n")
    f.close()
    
    #subprocess.run(["ffmpeg", "-loop", "1", "-r", "1", "-i", "sampleimage.png", "-i", "Fly_Me_to_the_Moon.mp3", "-c:a", "copy","-shortest",
     #               "-c:v", "libx264", "output.mp4"])
    subprocess.run(["ffmpeg", "-i", "output.mp4", "-vf", "subtitles=subtitles.srt", "output1.mp4"])
    combine_audio("output1.mp4", "Fly_Me_to_the_Moon.mp3", "final_output.mp4")

    ''' start_time = 6

    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture('output.mp4')
    while (cap.isOpened()):
            # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            fps = cap.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frame_count / fps

            print('fps = ' + str(fps))
            print('number of frames = ' + str(frame_count))
            print('duration (S) = ' + str(duration))
            minutes = int(duration / 60)
            seconds = duration % 60
            print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))
            # Display the resulting frame
            frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            image = cv2.putText(frame, text='EKO', org=(int(frameWidth / 2 - 20), int(frameHeight / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=3,
                        color=(0, 255, 0))
            cv2.imshow('sampleimage', image)
        else:
            break
    cap.release()
    cv2.destroyAllWindows() '''
main()