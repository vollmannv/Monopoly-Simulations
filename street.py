class Street:
    def __init__(self, pos):
        self.pos = pos
        self.price = 0
        self.house_price = 0
        self.houses = 0

        if self.pos == 2:
            self.price = 60
            self.house_price = 50
            self.name = 'Braun 1'
        elif self.pos == 4:
            self.price = 60
            self.house_price = 50
            self.name = 'Braun 2'
        elif self.pos == 7:
            self.price = 100
            self.house_price = 50
            self.name = 'Hellblau 1'
        elif self.pos == 9:
            self.price = 100
            self.house_price = 50
            self.name = 'Hellblau 2'
        elif self.pos == 10:
            self.price = 120
            self.house_price = 50
            self.name = 'Hellblau 3'
        elif self.pos == 12:
            self.price = 140
            self.house_price = 100
            self.name = 'Pink 1'
        elif self.pos == 14:
            self.price = 140
            self.house_price = 100
            self.name = 'Pink 2'
        elif self.pos == 15:
            self.price = 160
            self.house_price = 100
            self.name = 'Pink 3'
        elif self.pos == 17:
            self.price = 180
            self.house_price = 100
            self.name = 'Orange 1'
        elif self.pos == 19:
            self.price = 180
            self.house_price = 100
            self.name = 'Orange 2'
        elif self.pos == 20:
            self.price = 200
            self.house_price = 100
            self.name = 'Orange 3'
        elif self.pos == 22:
            self.price = 220
            self.house_price = 150
            self.name = 'Rot 1'
        elif self.pos == 24:
            self.price = 220
            self.house_price = 150
            self.name = 'Rot 2'
        elif self.pos == 25:
            self.price = 240
            self.house_price = 150
            self.name = 'Rot 3'
        elif self.pos == 27:
            self.price = 260
            self.house_price = 150
            self.name = 'Gelb 1'
        elif self.pos == 28:
            self.price = 260
            self.house_price = 150
            self.name = 'Gelb 2'
        elif self.pos == 30:
            self.price = 280
            self.house_price = 150
            self.name = 'Gelb 3'
        elif self.pos == 32:
            self.price = 300
            self.house_price = 200
            self.name = 'Gruen 1'
        elif self.pos == 33:
            self.price = 300
            self.house_price = 200
            self.name = 'Gruen 2'
        elif self.pos == 35:
            self.price = 320
            self.house_price = 200
            self.name = 'Gruen 3'
        elif self.pos == 38:
            self.price = 350
            self.house_price = 200
            self.name = 'Dunkelblau 1'
        elif self.pos == 40:
            self.price = 400
            self.house_price = 200
            self.name = 'Dunkelblau 2'

    def checkRent(self, name):

        if name == 'Braun 1':
            if self.houses == 0:
                self.rent = 2
            elif self.houses == 1:
                self.rent = 10
            elif self.houses == 2:
                self.rent = 30
            elif self.houses == 3:
                self.rent = 90
            elif self.houses == 4:
                self.rent = 160
            elif self.houses == 5:
                self.rent = 250
        elif name == 'Braun 2':
            if self.houses == 0:
                self.rent = 4
            elif self.houses == 1:
                self.rent = 20
            elif self.houses == 2:
                self.rent = 60
            elif self.houses == 3:
                self.rent = 180
            elif self.houses == 4:
                self.rent = 320
            elif self.houses == 5:
                self.rent = 450
        elif name == 'Hellblau 1' or name == 'Hellblau 2':
            if self.houses == 0:
                self.rent = 6
            elif self.houses == 1:
                self.rent = 30
            elif self.houses == 2:
                self.rent = 90
            elif self.houses == 3:
                self.rent = 270
            elif self.houses == 4:
                self.rent = 400
            elif self.houses == 5:
                self.rent = 550
        elif name == 'Hellblau 3':
            if self.houses == 0:
                self.rent = 8
            elif self.houses == 1:
                self.rent = 40
            elif self.houses == 2:
                self.rent = 100
            elif self.houses == 3:
                self.rent = 300
            elif self.houses == 4:
                self.rent = 450
            elif self.houses == 5:
                self.rent = 600
        elif name == 'Pink 1' or name == 'Pink 2':
            if self.houses == 0:
                self.rent = 10
            elif self.houses == 1:
                self.rent = 50
            elif self.houses == 2:
                self.rent = 150
            elif self.houses == 3:
                self.rent = 450
            elif self.houses == 4:
                self.rent = 625
            elif self.houses == 5:
                self.rent = 750
        elif name == 'Pink 3':
            if self.houses == 0:
                self.rent = 12
            elif self.houses == 1:
                self.rent = 60
            elif self.houses == 2:
                self.rent = 180
            elif self.houses == 3:
                self.rent = 500
            elif self.houses == 4:
                self.rent = 700
            elif self.houses == 5:
                self.rent = 900
        elif name == 'Orange 1' or name == 'Orange 2':
            if self.houses == 0:
                self.rent = 14
            elif self.houses == 1:
                self.rent = 70
            elif self.houses == 2:
                self.rent = 200
            elif self.houses == 3:
                self.rent = 550
            elif self.houses == 4:
                self.rent = 750
            elif self.houses == 5:
                self.rent = 950
        elif name == 'Orange 3':
            if self.houses == 0:
                self.rent = 16
            elif self.houses == 1:
                self.rent = 80
            elif self.houses == 2:
                self.rent = 220
            elif self.houses == 3:
                self.rent = 600
            elif self.houses == 4:
                self.rent = 800
            elif self.houses == 5:
                self.rent = 1000
        elif name == 'Rot 1' or name == 'Rot 2':
            if self.houses == 0:
                self.rent = 18
            elif self.houses == 1:
                self.rent = 90
            elif self.houses == 2:
                self.rent = 250
            elif self.houses == 3:
                self.rent = 700
            elif self.houses == 4:
                self.rent = 875
            elif self.houses == 5:
                self.rent = 1050
        elif name == 'Rot 3':
            if self.houses == 0:
                self.rent = 20
            elif self.houses == 1:
                self.rent = 100
            elif self.houses == 2:
                self.rent = 300
            elif self.houses == 3:
                self.rent = 750
            elif self.houses == 4:
                self.rent = 925
            elif self.houses == 5:
                self.rent = 1100
        elif name == 'Gelb 1' or name == 'Gelb 2':
            if self.houses == 0:
                self.rent = 22
            elif self.houses == 1:
                self.rent = 110
            elif self.houses == 2:
                self.rent = 330
            elif self.houses == 3:
                self.rent = 800
            elif self.houses == 4:
                self.rent = 975
            elif self.houses == 5:
                self.rent = 1150
        elif name == 'Gelb 3':
            if self.houses == 0:
                self.rent = 24
            elif self.houses == 1:
                self.rent = 120
            elif self.houses == 2:
                self.rent = 360
            elif self.houses == 3:
                self.rent = 850
            elif self.houses == 4:
                self.rent = 1025
            elif self.houses == 5:
                self.rent = 1200
        elif name == 'Gruen 1' or name == 'Gruen 2':
            if self.houses == 0:
                self.rent = 26
            elif self.houses == 1:
                self.rent = 130
            elif self.houses == 2:
                self.rent = 390
            elif self.houses == 3:
                self.rent = 900
            elif self.houses == 4:
                self.rent = 1100
            elif self.houses == 5:
                self.rent = 1275
        elif name == 'Gruen 3':
            if self.houses == 0:
                self.rent = 28
            elif self.houses == 1:
                self.rent = 150
            elif self.houses == 2:
                self.rent = 450
            elif self.houses == 3:
                self.rent = 1000
            elif self.houses == 4:
                self.rent = 1200
            elif self.houses == 5:
                self.rent = 1400
        elif name == 'Dunkelblau 1':
            if self.houses == 0:
                self.rent = 35
            elif self.houses == 1:
                self.rent = 175
            elif self.houses == 2:
                self.rent = 500
            elif self.houses == 3:
                self.rent = 1100
            elif self.houses == 4:
                self.rent = 1300
            elif self.houses == 5:
                self.rent = 1500
        elif name == 'Dunkelblau 2':
            if self.houses == 0:
                self.rent = 50
            elif self.houses == 1:
                self.rent = 200
            elif self.houses == 2:
                self.rent = 600
            elif self.houses == 3:
                self.rent = 1400
            elif self.houses == 4:
                self.rent = 1700
            elif self.houses == 5:
                self.rent = 2000
