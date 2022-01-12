# syntax=docker/dockerfile:1

FROM python:3.8-slim
WORKDIR /evo
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app app
CMD [ "python3", "app/main.py"]
