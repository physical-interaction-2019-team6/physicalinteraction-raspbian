import threading
import time

import bluetooth

IS_CLIENT = 0
TARGET_BLUETOOTH_MAC_ADDRESS = "B8:27:EB:A8:D1:0A"
PORT = 1


class Communication:
    def __init__(self):
        if IS_CLIENT:
            self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.server_sock.bind(("", PORT))
            self.server_sock.listen(1)

            self.sock, address = self.server_sock.accept()
            print("Accepted connection from " + str(address))
        else:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((TARGET_BLUETOOTH_MAC_ADDRESS, PORT))

        # start receive thread
        self.receive_data = ""

        def receive_loop():
            while True:
                time.sleep(0.5)
                self.receive_data = self.sock.recv(1024)

        self.thread_receive = threading.Thread(target=receive_loop)
        self.thread_receive.setDaemon(True)
        self.thread_receive.start()

    def send(self, data):
        self.sock.send(str(data))

    def receive(self):
        return self.receive_data

    def close(self):
        self.sock.close()
        if IS_CLIENT:
            self.server_sock.close()
