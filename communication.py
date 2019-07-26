import bluetooth

IS_CLIENT = 1
TARGET_BLUETOOTH_MAC_ADDRESS = ""
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

    def send(self, data):
        self.sock.send(str(data))

    def receive(self):
        return self.sock.recv(1024)

    def close(self):
        self.sock.close()
        if IS_CLIENT:
            self.server_sock.close()
