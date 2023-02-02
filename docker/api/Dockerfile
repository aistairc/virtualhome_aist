FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

RUN apt-get update
RUN apt install -y ffmpeg

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./simulation/ ./simulation/
COPY ./docker/api/main.py ./
