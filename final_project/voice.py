
from vosk import Model, KaldiRecognizer
from pyaudio import PyAudio, paInt16
from pathlib import Path
from final_project.interfaces import InputInterface
from final_project.handler import config

class VoiceInput(InputInterface):
    def __init__(self):
        self.microphone = PyAudio()
        self.__model = None
        self.model = config["recognization_model"]
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        if Path(model).exists():
            self.__model = Model(model)
            self.recognizer = KaldiRecognizer(self.__model, 16000)

    def data_input(self):
        stream = self.microphone.open(
            format=paInt16, 
            channels=1, 
            rate=16000, 
            input=True, 
            frames_per_buffer=16000
        )
        stream.start_stream()

        while True:
            data = stream.read(4000)
            if len(data) == 0:
                break
            
            if self.recognizer.AcceptWaveform(data):
                break
        data = self.recognizer.FinalResult().split(":")[1][1:-1]
        return data