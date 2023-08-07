import random as r


class Game:
    def __init__(self):
        self.offense = Team()
        self.defense = Team()
        self.field = Field()
        self.round = None
        self.play = None

    def start_round(self):
        self.round = 1
        self.play = 1
        for o in self.offense.players:
            o.draw()
        for d in self.defense.players:
            d.draw()

    def run_play(self):
        if self.play == 3:
            self.play = 1
            self.round += 1
        else:
            self.play += 1


class Team:
    def __init__(self):
        self.players = [Player(self) for x in range(11)]


class Player:
    def __init__(self, team):
        self.deck = [Card(team, 'Strength') for x in range(4)] + \
            [Card(team, 'Agility') for x in range(4)] + \
            [Card(team, 'Focus') for x in range(4)]
        self.hand = []

    def draw(self):
        for i in range(3):
            self.hand.append(self.deck.pop())


class Card:
    types = ['Strength', 'Agility', 'Focus']

    def __init__(self, team, type):
        self.team = team
        self.low = 0
        self.high = 2
        self.value = 0
        if type in self.types:
            self.type = type
        else:
            raise ValueError('Not a valid card type.')

    def roll(self):
        if self.type == 'Agility':
            self.value = r.choice(range(self.low, self.high + 1))


class Field:
    def __init__(self):
        self.grid = [
            [[],[],[]],
            [[],[],[]],
            [[],[],[]],
            [[],'X',[]],
        ]
    
    def play(self, c, z):
        if z == 'X':
            return False
        else:
            z.append(c)
            return True