from time import sleep

from Recorder import Recorder


def main():
    recorder = Recorder()
    recorder.start()
    sleep(5)
    recorder.save()
    recorder.stop()

    # vibrator = Vibrator()
    # vibrator.vibrate()


if __name__ == "__main__":
    main()
