##FROM python:3.11-bullseye
FROM python:3.9

##pip install pipwin 
##pipwin install pyaudio

WORKDIR /final_project

COPY . .

RUN apt-get update
#neded for pyaudio on ubuntu
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y

RUN pip install -e .

ENTRYPOINT ["bot-cli"]





