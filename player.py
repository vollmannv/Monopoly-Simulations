import random

class Player:

    def __init__(self, maxSpendQuotient, name, buffer, tradeRate, answerRate, stratMode=0, buysBahn=True, buysWerk=False):
        self.pos = 1
        self.cash = 1500
        self.answerRate = answerRate
        self.tradeRate = tradeRate
        self.buffer = buffer
        self.maxSpendQuotient = maxSpendQuotient
        self.streetsOwned = []
        self.name = name
        self.jailFree = False
        self.netWorth = 0
        self.turn = False
        self.inGame = True
        self.bahnhofArr = []
        self.werkArr = []
        self.updateArrays()
        self.paschNum = 0
        self.stratMode = stratMode
        self.setNumber = 0
        self.buysBahn = buysBahn
        self.buysWerk = buysWerk

    def move(self):
        self.dice1 = random.randrange(1,7)
        self.dice2 = random.randrange(1,7)
        self.pos += self.dice1 + self.dice2
        if self.dice1 == self.dice2:
            self.pasch = True
        else:
            self.pasch = False

        if self.pasch:
            self.paschNum += 1
        else:
            self.paschNum = 0

        if self.paschNum == 3:
            self.paschNum = 0
            self.pos = 11

        if self.pos > 40:
            self.pos -= 40
            self.cash += 200
            # print(self.name + ' went over Los ' + 'he now has ' + str(self.cash))
        # print(self.name + ' rolled a ' + str(self.dice1) + ' and a ' + str(self.dice2) + '. He moved to ' + str(self.pos))

    def buyStreet(self, street):

        if self.stratMode == 0:
            self.maxSpend = self.cash/self.maxSpendQuotient
            if street.price < self.maxSpend and self.cash > self.buffer:
                self.cash -= street.price
                self.streetsOwned.append(street)
                # print(self.name + ' bought ' + street.name + ' for ' + str(street.price))
                # print(self.name + ' has ' + str(self.cash) + ' left.')
            # else:
                # print(self.name + ' didnt buy ' + street.name + '.')
                # print(self.name + ' has ' + str(self.cash) + ' left.')

        self.updateArrays()

    def buyBahnhof(self, bahnhof):
        if self.buysBahn:
            if self.stratMode == 0:
                self.maxSpend = self.cash/self.maxSpendQuotient
                if bahnhof.price < self.maxSpend and self.cash > self.buffer:
                    self.cash -= bahnhof.price
                    self.bahnhofArr.append(bahnhof)
                    # print(self.name + ' bought ' + bahnhof.name + ' for ' + str(bahnhof.price))
                    # print(self.name + ' has ' + str(self.cash) + ' left.')
                # else:
                    # print(self.name + ' didnt buy ' + bahnhof.name + '.')
                    # print(self.name + ' has ' + str(self.cash) + ' left.')

    def buyWerk(self, werk):
        if self.buysWerk:
            if self.stratMode == 0:
                self.maxSpend = self.cash/self.maxSpendQuotient
                if werk.price < self.maxSpend and self.cash > self.buffer:
                    self.cash -= werk.price
                    self.werkArr.append(werk)
                    # print(self.name + ' bought ' + werk.name + ' for ' + str(werk.price))
                    # print(self.name + ' has ' + str(self.cash) + ' left.')
                # else:
                    # print(self.name + ' didnt buy ' + werk.name + '.')
                    # print(self.name + ' has ' + str(self.cash) + ' left.')

    def checkOwnedHouses(self, street):
        streetColor = street.name.split()[0]
        counter = 0
        if streetColor == 'Dunkelblau' or streetColor == 'Braun':
            for el in self.streetsOwned:
                if streetColor in el.name:
                    counter+=1
            if counter == 2:
                return True
            else:
                return False
        else:
            for el in self.streetsOwned:
                if streetColor in el.name:
                    counter += 1
            if counter == 3:
                return True
            else:
                return False

    def buyHouse(self, street):

        if self.stratMode == 0:
            self.maxSpend = self.cash/self.maxSpendQuotient
            streetColor = street.name.split()[0]
            streets = []
            houses = 0
            maxBuyHouses = 0
            for el in self.streetsOwned:
                if el.name == streetColor + ' 1':
                    streets.append(el)
                elif el.name == streetColor + ' 2':
                    streets.append(el)
                elif el.name == streetColor + ' 3':
                    streets.append(el)
            if len(streets) == 3:
                for s in streets:
                    houses += s.houses
                maxBuyHouses = 15 - houses
            if 'Dunkelblau' in street.name or 'Braun' in street.name:
                if len(streets) == 2:
                    for s in streets:
                        houses += s.houses
                    maxBuyHouses = 10 - houses
            boughtHouses = (self.maxSpend-self.buffer) // street.house_price
            if boughtHouses > maxBuyHouses:
                boughtHouses = maxBuyHouses

            if boughtHouses > 0:
                 self.cash -= boughtHouses*street.house_price
                 # print(self.name + ' bought ', boughtHouses, ' houses for ', (boughtHouses*street.house_price))
                 # print(self.name + ' has ', self.cash, ' left.')
                 for s in streets:
                     if s.houses < 5:
                         s.houses += boughtHouses // len(streets)
                         if s.houses > 5:
                             s.houses = 5
                 street.houses += boughtHouses % len(streets)
                 for s in streets:
                     if s.houses > 5:
                         s.houses = 5
                     # print(s.name + ' now has ', s.houses, ' houses.')

        self.updateArrays()

    def setNetWorth(self):
        for street in self.streetsOwned:
            self.netWorth += street.houses * (street.house_price/2)

    def sellHouse(self):
        if self.cash < 0:
            for street in self.streetsOwned:
                if self.cash < 0 and street.houses > 0:
                    self.cash += street.house_price/2
                    street.houses -= 1
                    self.netWorth -= street.house_price/2
                    # print(self.name + ' sold a house on ' + street.name + ' for ' + str(street.house_price/2))
        # print(self.name, ' has ', self.cash, ' left.')

        if self.cash < 0:
            # print(self.name + ' lost the game.')
            self.inGame = False

        self.updateArrays()

    def updateArrays(self):
        self.hellblau = []
        self.pink = []
        self.orange = []
        self.rot = []
        self.gelb = []
        self.gruen = []

        for s in self.streetsOwned:
            if 'Hellblau' in s.name:
                self.hellblau.append(s)
            elif 'Pink' in s.name:
                self.pink.append(s)
            elif 'Orange' in s.name:
                self.orange.append(s)
            elif 'Rot' in s.name:
                self.rot.append(s)
            elif 'Gelb' in s.name:
                self.orange.append(s)
            elif 'Gruen' in s.name:
                self.orange.append(s)

        self.allColors = []
        self.allColors.extend((self.hellblau, self.pink, self.orange, self.rot, self.gelb, self.gruen))
