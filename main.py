import time

from communication import Communication
from emotion_prediction import EmotionPrediction
from recorder import Recorder
from vibrator import Vibrator


def main():
    recorder = Recorder()
    vibrator = Vibrator()

    prediction = EmotionPrediction()
    prediction.load_model()

    com = Communication()

    recorder.start()
    try:
        while True:
            time.sleep(1)
            buf, rate = recorder.get_as_numpy_array()

            is_happy = prediction.predict(buf, rate)
            com.send(is_happy)

            is_target_happy = int(com.receive())

            print("is_happy: " + str(is_happy) + "is_target_happy: " + str(is_target_happy))

            if is_happy and is_target_happy:
                vibrator.vibrate()
    except KeyboardInterrupt:
        pass

    com.close()
    recorder.stop()


if __name__ == "__main__":
    main()
