import whisper
from stable_whisper import modify_model
import json

model = whisper.load_model('base')
modify_model(model)
# modified model should run just like the regular model but with additional hyperparameters and extra data in results
results = model.transcribe('../../Fly_Me_to_the_Moon.wav')
stab_segments = results['segments']
first_segment_word_timestamps = stab_segments[0]['whole_word_timestamps']

# or to get token timestamps that adhere more to the top prediction
from stable_whisper import stabilize_timestamps
stab_segments = stabilize_timestamps(results, top_focus=True)

for i in range(len(stab_segments)):
    print(stab_segments[i]['text'])
    print(stab_segments[i]['start'])
    print(stab_segments[i]['end'])