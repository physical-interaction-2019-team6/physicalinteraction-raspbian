from time import sleep

from emotion_prediction import EmotionPrediction
from recorder import Recorder


def main():
    recorder = Recorder()
    recorder.start()
    sleep(3)
    buf, rate = recorder.get_as_numpy_array()
    recorder.stop()

    m = EmotionPrediction()

    m.predict(buf, rate)

    print(buf.shape)
    # vibrator = Vibrator()
    # vibrator.vibrate()


if __name__ == "__main__":
    main()
