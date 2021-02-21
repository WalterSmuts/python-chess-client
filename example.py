from chessclient import ChessClient
import chess
import random

def random_decision_function(fen_string):
    legal_moves = list(chess.Board(fen_string).legal_moves)
    selected_move = random.choice(legal_moves)
    print(selected_move)
    return selected_move

class Player:
    def __init__(self, decision_function):
        self.decision_function = decision_function

    def get_move(self,fen):
        return self.decision_function(fen)


# Default (Random)
ChessClient(Player(random_decision_function)).run()

# Opponent options
#ChessClient(Player(random_decision_function), "Random").run()  # Easy
#ChessClient(Player(random_decision_function), "Greedy").run()  # Harder
#ChessClient(Player(random_decision_function), "Network").run() # Another network player
