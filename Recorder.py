import copy
import wave

import pyaudio

WAVE_FILE = "audio.wav"

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2 ** 12
RECORD_SECONDS = 1
DEVICE_INDEX = 1


class Recorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.frames = []

        def callback(in_data, frame_count, time_info, status):
            self.frames.append(in_data)
            return None, pyaudio.paContinue

        self.stream = self.audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK,
            input_device_index=DEVICE_INDEX,
            start=False,
            stream_callback=callback
        )

        # Device index
        # for x in range(0, self.audio.get_device_count()):
        #     print(self.audio.get_device_info_by_index(x))

    def start(self):
        print("Recording start")
        self.stream.start_stream()

    def stop(self):
        print("Recording stop")
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def save(self):
        _frames = copy.copy(self.frames)
        self.frames.clear()

        wf = wave.open(WAVE_FILE, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(_frames))
        wf.close()
