## A python chess client

A simple client to get started with coding a chess-ai in python. This client
talks to the chess server running on waltersmuts.com, playing against the Greedy
algorithm, by default. There is also a `Random` opponent for if you're struggling.

Take a look at the `example.py` file and you will see how to use the
`chessclient` module. Per default it currently outputs the board state in
[Forsyth–Edwards Notation]( https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation)
but if you want to write a nicer frontend, pull-requests are welcome.

This is just the start... Much more to come :D

### Dependencies
* python3
* chess
* random

### Running
```
# Install dependencies first
git clone https://github.com/WalterSmuts/python-chess-client.git
cd python-chess-client
python3 example.py
# Maybe on some systems python3 is aliased to just `python`:
# python example.py
```
