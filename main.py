from audio_capture import start_stream, capture_audio
from transcription_api import get_transcription
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

stream, audio = start_stream()

while True:
    audio_data = capture_audio(stream, audio)
    print(get_transcription(audio_data))

stream.stop_stream()
stream.close()
audio.terminate()
