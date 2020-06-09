class Werk:

    def __init__(self, pos, name):
        self.pos = pos
        self.name = name
        self.price = 150

    def getRent(self, owner, player):
        if len(owner.werkArr) == 1:
            self.rent = (player.dice1+player.dice2)*4
        else:
            self.rent = (player.dice1+player.dice2)*10
