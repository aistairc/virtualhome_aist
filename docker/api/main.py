from os import environ
from datetime import datetime
from typing import List, Union
from uuid import uuid4
import subprocess

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from simulation.unity_simulator.comm_unity import UnityCommunication


app = FastAPI()

if environ.get('ALLOW_CORS') == 'true':
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.mount("/static", StaticFiles(directory="/Output"), name="static")


@app.get("/")
def read_root():
    return {"Hello": "VirtualHome"}


class PositionItem(BaseModel):
    x: int
    y: int
    z: int


class CharacterItem(BaseModel):
    resource: str = "Chars/Male1"
    position: Union[PositionItem, None] = None
    initial_room: str = ""


class VideoItem(BaseModel):
    script: List[str]
    scene: int
    characters: List[CharacterItem] = []


@app.post("/generate_video")
def generate_video(video_item: VideoItem):
    video_dict = video_item.dict()
    comm = UnityCommunication(url="unity")

    try:
        comm.reset(video_dict["scene"])

        if not video_dict["characters"]:
            comm.add_character("Chars/Male1")
        for character in video_dict["characters"]:
            position = [character["position"]["x"], character["position"]["y"], character["position"]["z"]] if character["position"] else None
            comm.add_character(character["resource"], position, character["initial_room"])

        now = datetime.utcnow()
        output_folder = f"Output/{now:%Y%m}/"
        file_name_prefix = f"{uuid4()}"
        success, message = comm.render_script(
            video_dict["script"],
            recording=True,
            find_solution=True,
            output_folder=output_folder,
            file_name_prefix=file_name_prefix
        )
        if not success:
            raise ValueError(message)

        # mp4に変換
        video_path = f"{now:%Y%m}/{file_name_prefix}/0/video.mp4"
        command_set = [
            "ffmpeg",
            "-framerate", "5",
            "-i", f"/{output_folder}{file_name_prefix}/0/Action_%04d_0_normal.png",
            "-pix_fmt", "yuv420p",
            f"/Output/{video_path}",
        ]
        subprocess.call(command_set)
    except Exception as e:
        return {"ok": False, "message": str(e)}

    video_path = f"/static/{video_path}"
    return {"ok": True, "video_path": video_path}
