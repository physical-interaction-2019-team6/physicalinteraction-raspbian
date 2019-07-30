import time
import communication

from emotion_prediction import EmotionPrediction
from recorder import Recorder
from vibrator import Vibrator


def main():
    recorder = Recorder()
    vibrator = Vibrator()

    prediction = EmotionPrediction()
    prediction.load_model()

    com = communication.Communication()

    recorder.start()
    try:
        while True:
            time.sleep(1.0)
            buf, rate = recorder.get_as_numpy_array()

            is_happy = prediction.predict(buf, rate)

            if communication.IS_SERVER:
                is_target_happy = int(com.receive())

                print("is_happy: " + str(is_happy) + ", is_target_happy: " + str(is_target_happy))

                is_vibrate = int(is_happy == 1 and is_target_happy == 1)
                com.send(is_vibrate)
            else:
                is_vibrate = com.receive()
                com.send(is_happy)

            if is_vibrate == 1:
                vibrator.vibrate()
    except KeyboardInterrupt:
        pass

    com.close()
    recorder.stop()


if __name__ == "__main__":
    main()
