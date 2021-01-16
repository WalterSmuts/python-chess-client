import socket

class ChessClient:
    def __init__(self, player, opponent = "Greedy", server = "waltersmuts.com", port = 3333):
        self.player = player
        self.opponent = opponent
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server, port))
        print("Connected to server: {} at port {}".format(server, port))

    def run(self):
        self.socket.send(str(self.opponent).encode('utf-8'))
        while True:
            data = self.socket.recv(92).decode("utf-8")
            print(data)
            if len(data) == 1:
                break

            move = self.player.get_move(data)
            self.socket.send(str(move).encode('utf-8'))

        if data == "W":
            print("You win!")
        elif data == "L":
            print("You lose!")
        elif data == "D":
            print("It's a draw...")
        else:
            print("Unknown control message.")
