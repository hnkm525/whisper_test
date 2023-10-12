import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = int(RATE / 10)

def start_stream():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    return stream, audio

def capture_audio(stream, audio, duration=5):
    frames = []
    for _ in range(0, int(RATE / CHUNK * duration)):
        try:
            data = stream.read(CHUNK, exception_on_overflow=False) 
            frames.append(data)
        except IOError as e:
            print("Warning: Input buffer overflowed. Restarting stream...")
            stream.start_stream()
    return b''.join(frames)

