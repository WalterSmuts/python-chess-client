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
            if len(data) == 1:
                break
            print(data)

            move = self.player.get_move(data)
            self.socket.send(str(move).encode('utf-8'))

        result = data
        data = self.socket.recv(92).decode("utf-8")

        print(data)
        if result == "W":
            print("You win!")
        elif result == "L":
            print("You lose!")
        elif result == "D":
            print("It's a draw...")
        else:
            print("Unknown control message.")

        url = self.socket.recv(92).decode("utf-8")
        print("Find your game at:");
        print(url);
