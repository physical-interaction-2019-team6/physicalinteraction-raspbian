from time import sleep

from emotion_prediction import EmotionPrediction
from recorder import Recorder
#import test_code


def main():
    recorder = Recorder()
    recorder.start()
    sleep(3)
    buf, rate = recorder.get_as_numpy_array()
    recorder.stop()
    #buf, rate = test_code.read("./anshin.wav")

    m = EmotionPrediction()

    m.load_model()
    result = m.predict(buf, rate)
    print(result)
    exit()
    print(buf.shape)
    # vibrator = Vibrator()
    # vibrator.vibrate()


if __name__ == "__main__":
    main()
