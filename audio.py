import pyaudio
import wave
import sys

CHUNK=256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 11025

def audio_setup():
    
    try:
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=CHUNK,
                        )
    except:
        print("Микрофон или наушники не подключены.")
        return None
    return stream



