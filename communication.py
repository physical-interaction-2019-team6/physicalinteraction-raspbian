import threading
import time

import bluetooth

IS_SERVER = 1
TARGET_BLUETOOTH_MAC_ADDRESS = "B8:27:EB:A8:D1:0A"
PORT = 1


class Communication:
    def __init__(self):
        if IS_SERVER:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((TARGET_BLUETOOTH_MAC_ADDRESS, PORT))
        else:
            self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.server_sock.bind(("", PORT))
            self.server_sock.listen(1)

            self.sock, address = self.server_sock.accept()
            print("Accepted connection from " + str(address))

        # start receive thread
        self.receive_data = "0"

        def receive_loop():
            while True:
                time.sleep(0.5)
                data = self.sock.recv(1024)

                if self.receive_data == "0":
                    self.receive_data = data

        self.thread_receive = threading.Thread(target=receive_loop)
        self.thread_receive.setDaemon(True)
        self.thread_receive.start()

    def send(self, data):
        self.sock.send(str(data))

    def receive(self):
        data = self.receive_data
        self.receive_data = "0"
        return data

    def close(self):
        self.sock.close()
        if not IS_SERVER:
            self.server_sock.close()
