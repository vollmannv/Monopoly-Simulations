class Bahnhof:

    def __init__(self, pos, name):
        self.pos = pos
        self.rent = 0
        self.price = 200
        self.name = name

    def getRent(self, owner):
        if len(owner.bahnhofArr) == 1:
            self.rent = 25
        elif len(owner.bahnhofArr) == 2:
            self.rent = 50
        elif len(owner.bahnhofArr) == 3:
            self.rent == 100
        elif len(owner.bahnhofArr) == 4:
            self.rent == 200
