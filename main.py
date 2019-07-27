from time import sleep

from emotion_prediction import EmotionPrediction
from recorder import Recorder


def main():
    recorder = Recorder()
    recorder.start()

    prediction = EmotionPrediction()

    while True:
        sleep(1)
        buf, rate = recorder.get_as_numpy_array()
        is_happy = prediction.predict(buf, rate)
        print(is_happy)

    recorder.stop()


if __name__ == "__main__":
    main()
