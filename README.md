# AIMusicVisualizer
## Requirements:
- 10-12 GB VRAM
- Non-ARM based system
- ~20GB of free space
## Setup
Setup an anaconda enviornment, then follow the instructions at the respective Githubs to setup the AI models.
### Whisper Setup:
https://github.com/openai/whisper
### Deforum Stable Fusion Setup:
https://github.com/HelixNGC7293/DeforumStableDiffusionLocal
Then to setup the web application:
### Server:
Navigate inside the `/client/` directory and run `pip install uvicorn`.
Then to start the client run `python main.py`.
### Client:
Navigate inside the `/server/` directory and run `npm install`.
Then to start the server run `npm run dev`.
