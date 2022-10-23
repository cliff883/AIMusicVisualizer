#!/usr/bin/zsh

conda activate dsd

rm -rf runSettings.txt

python speechToText.py

python run.py --enable_animation_mode --settings "./runSettings.txt"

ffmpeg -i ./output/22-10/TaskName2/*.mp4 -i ../server/files/in_file.mp3 -vf subtitles=subtitles.srt final_output.mp4