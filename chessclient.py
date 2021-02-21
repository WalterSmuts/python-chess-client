import socket

ENDIANNESS = "big"

class ChessClient:
    def __init__(self, player, opponent = "Random", server = "chess.waltersmuts.com", port = 3333):
        self.player = player
        self.opponent = opponent
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server, port))
        print("Connected to server: {} at port {}".format(server, port))

    def send_lenth_prefixed(self, data):
        self.socket.send(len(data).to_bytes(1, ENDIANNESS))
        self.socket.send(data)

    def recv_lenth_prefixed(self):
        length = int.from_bytes(self.socket.recv(1), ENDIANNESS)
        return self.socket.recv(length)

    def run(self):
        self.send_lenth_prefixed(str(self.opponent).encode('utf-8'))
        if self.opponent == "Network":
            print("Waiting for another network opponent to  connect...")
        while True:
            data = self.recv_lenth_prefixed().decode("utf-8")
            if len(data) == 1:
                break
            print(data)

            move = self.player.get_move(data)
            self.send_lenth_prefixed(str(move).encode('utf-8'))

        result = data
        data = self.recv_lenth_prefixed().decode("utf-8")

        print(data)
        if result == "W":
            print("You win!")
        elif result == "L":
            print("You lose!")
        elif result == "D":
            print("It's a draw...")
        else:
            print("Unknown control message.")

        url = self.recv_lenth_prefixed().decode("utf-8")
        print("Find your game at:");
        print(url);
