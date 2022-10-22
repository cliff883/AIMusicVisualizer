import wave
import json
from vosk import Model, KaldiRecognizer

class Word:
    def __init__(self, dict):
        self.conf = dict["conf"]
        self.end = dict["end"]
        self.start = dict["start"]
        self.word = dict["word"]

    def to_string(self):
        ''' Returns a string describing this instance '''
        return "{:20} from {:.2f} sec to {:.2f} sec, confidence is {:.2f}%".format(
            self.word, self.start, self.end, self.conf*100)
            

wf = wave.open('../Fly_Me_to_the_moon.wav', "rb")
model = Model('../vosk-model-en-us-0.22')
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)


results = []
# recognize speech using vosk model
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        part_result = json.loads(rec.Result())
        results.append(part_result)

part_result = json.loads(rec.FinalResult())
results.append(part_result)

# forming a final string from the words
text = ''
for r in results:
    text += r['text'] + ' '
print(results)
print(f"Vosk thinks you said:\n {text}")

with open('json_lyrics.json', 'w') as outfile:
    json.dump(results, outfile)
