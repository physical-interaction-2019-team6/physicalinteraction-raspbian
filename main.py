from time import sleep

from communication import Communication


def main():
    com = Communication()
    while True:
        com.send("Hello")
        print(com.receive())
        sleep(1)


if __name__ == "__main__":
    main()
