## A python chess client

A simple client to get started with coding a chess-ai in python. This client
talks to the chess server running on
[chess.waltersmuts.com](https://chess.waltersmuts.com), playing against the
`Random` opponent, by default. These are all the opponent options:
* `Random`
* `Greedy`
* `Network`

Take a look at the `example.py` file and you will see how to use the
`chessclient` module. It currently outputs the board state in [Forsyth–Edwards
Notation]( https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) but
if you want to write a nicer frontend, pull-requests are welcome.

### Dependencies
* python3
* pip3
* python modules in `requirements.txt`

### Running
On some systems python version 3 and pip is aliased to `pip` and `python` so
please change commands accordingly.
```
git clone https://github.com/WalterSmuts/python-chess-client.git
cd python-chess-client
pip3 install -r requirements.txt
python3 example.py
```

If you're interested in what's happening behind the curtains, check out
[chess-server](https://github.com/WalterSmuts/chess-server). If you want, you
can clone it and run it locally, pointing the client towards the local
endpoint.
