from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


import aiofiles

app = FastAPI()


in_file_path="./files/in_file.mp3"
out_file_path="./files/out_file.mp4"

origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Server working!"}

@app.post("/api/upload/song")
async def save_upload_song(in_file: UploadFile=File(...)):
    # ...
    async with aiofiles.open(in_file_path, 'wb') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)  # async write

    return {"Result": "OK"}

@app.get("/api/download/video")
def get_download_video():
    return FileResponse(path=out_file_path, filename=out_file_path, media_type='video/mp4')