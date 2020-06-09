from tqdm import tqdm
import player as pl
import street
import ereignis
import gemeinschaft
import werk
import bahnhof
import random
import steuer

print('STARTING SIM')

outF = open('GameSimOut2.txt', 'w')
player1Wins = 0
player2Wins = 0
player3Wins = 0
player4Wins = 0

games = 1000000

for i in tqdm(range(games)):
    player = pl.Player(1, 'Player 1', 400, 1.5, 0.40)
    player2 = pl.Player(1.5, 'Player 2', 600, 1.5, 0.40)
    player3 = pl.Player(2, 'Player 3', 0, 1.5, 0.40)
    player4 = pl.Player(2.5, 'Player 4', 0, 1.5, 0.40)
    streets = []
    ereignisFelder = []
    gemeinschaftsFelder = []
    bahnhoefe = []
    werke = []
    steuern = []

    ereignisKarten = ['GoTo15', '+200', '+300', 'JailFree', 'GoTo1', '+100', 'GoTo40', 'GoTo22', 'GoBack3', 'House-50Hotel-200', 'House-80Hotel-230', '-40', '-30', 'Jail', '-50']
    random.shuffle(ereignisKarten)
    gemeinschaftsKarten = ['+200*player', '+100', '+200', '+200', '+50', 'GoTo1', 'JailFree', '+400', '+200', '+50', 'GoTo4', '-200', 'Jail', '-200', '-100', '-50']
    random.shuffle(gemeinschaftsKarten)

    braun1 = street.Street(2)
    gemeinschaft1 = gemeinschaft.Gemeinschaft(3)
    braun2 = street.Street(4)
    steuer1 = steuer.Steuer(5, 'Einkommenssteuer', 200)
    bahnhof1 = bahnhof.Bahnhof(6, 'Bahnhof 1')
    hellblau1 = street.Street(7)
    ereignis1 = ereignis.Ereignis(8)
    hellblau2 = street.Street(9)
    hellblau3 = street.Street(10)
    pink1 = street.Street(12)
    werk1 = werk.Werk(13, 'Elektrizitätswerk')
    pink2 = street.Street(14)
    pink3 = street.Street(15)
    bahnhof2 = bahnhof.Bahnhof(16, 'Bahnhof 2')
    orange1 = street.Street(17)
    gemeinschaft2 = gemeinschaft.Gemeinschaft(18)
    orange2 = street.Street(19)
    orange3 = street.Street(20)
    rot1 = street.Street(22)
    ereignis2 = ereignis.Ereignis(23)
    rot2 = street.Street(24)
    rot3 = street.Street(25)
    bahnhof3 = bahnhof.Bahnhof(26, 'Bahnhof 3')
    gelb1 = street.Street(27)
    gelb2 = street.Street(28)
    werk2 = werk.Werk(29, 'Wasserwerk')
    gelb3 = street.Street(30)
    gruen1 = street.Street(32)
    gruen2 = street.Street(33)
    gemeinschaft3 = gemeinschaft.Gemeinschaft(34)
    gruen3 = street.Street(35)
    bahnhof4 = bahnhof.Bahnhof(36, 'Bahnhof 4')
    ereignis3 = ereignis.Ereignis(37)
    dunkelblau1 = street.Street(38)
    steuer2 = steuer.Steuer(39, 'Zusatzsteuer', 100)
    dunkelblau2 = street.Street(40)

    braun = [braun1, braun2]
    hellblau = [hellblau1, hellblau2, hellblau3]
    pink = [pink1, pink2, pink3]
    orange = [orange1, orange2, orange3]
    rot = [rot1, rot2, rot3]
    gelb = [gelb1, gelb2, gelb3]
    gruen = [gruen1, gruen2, gruen3]
    dunkelblau = [dunkelblau1, dunkelblau2]

    players = [player, player2, player3, player4]

    streets.extend((braun1,braun2,hellblau1,hellblau2,hellblau3,pink1,pink2,pink3,orange1,orange2,orange3,rot1,rot2,rot3,gelb1,gelb2,gelb3,gruen1,gruen2,gruen3,dunkelblau1,dunkelblau2))
    ereignisFelder.extend((ereignis1,ereignis2,ereignis3))
    gemeinschaftsFelder.extend((gemeinschaft1,gemeinschaft2,gemeinschaft3))
    bahnhoefe.extend((bahnhof1, bahnhof2, bahnhof3, bahnhof4))
    werke.extend((werk1, werk2))
    steuern.extend((steuer1, steuer2))

    def checkIfAv(street, players):
        for p in players:
            for s in p.streetsOwned:
                if street == s:
                    return False
        return True

    def checkIfAvBahnhof(bahnhof, players):
        for p in players:
            for b in p.bahnhofArr:
                if b == bahnhof:
                    return False
        return True

    def checkIfAvWerk(werk, players):
        for p in players:
            for w in p.werkArr:
                if w == werk:
                    return False
        return True

    def getOwner(street, players):
        for p in players:
            for s in p.streetsOwned:
                if street == s:
                    return p.name

    def getOwnerBahnhof(bahnhof, players):
        for p in players:
            for b in p.bahnhofArr:
                if b == bahnhof:
                    return p

    def getOwnerWerk(werk, players):
        for p in players:
            for w in p.werkArr:
                if w == werk:
                    return p

    def trade(owner, buyer, s, price):
        owner.streetsOwned.remove(s)
        buyer.streetsOwned.append(s)
        owner.cash += price
        buyer.cash -= price

        # print(buyer.name + ' bought ' + s.name + ' from ' + owner.name + ' for ', price, '.')

    def findOwner(players, buyer, streets):
        missingStreetName = ''
        for c in buyer.allColors:
            if len(c) < 3 and len(c) > 0:
                color = c[0].name.split()[0]
                if len(c) == 2:
                    if '1' in c[0].name or '2' in c[1].name:
                        missingStreetName = color + ' 3'
                    elif '1' in c[1].name and '2' in c[0].name:
                        missingStreetName = color + ' 3'
                    elif '2' in c[1].name and '3' in c[0].name:
                        missingStreetName = color + ' 1'
                    elif '2' in c[0].name and '3' in c[1].name:
                        missingStreetName = color + ' 1'
                    elif '1' in c[1].name and '3' in c[0].name:
                        missingStreetName = color + ' 2'
                    elif '1' in c[0].name and '3' in c[1].name:
                        missingStreetName = color + ' 2'
                elif len(c) == 1:
                    if '1' in c[0].name:
                        missingStreetName = color + ' 2'
                    elif '2' in c[0].name:
                        missingStreetName = color + ' 3'
                    elif '3' in c[0].name:
                        missingStreetName = color + ' 1'
        if missingStreetName:
            for p in players:
                for s in p.streetsOwned:
                    if s.name == missingStreetName:
                        makeOffer(buyer, p, s)

    def makeOffer(buyer, owner, street):
        price = random.randint((street.price * 1.5),(buyer.tradeRate * street.price))
        # print(buyer.name + ' offered ', price, ' to buy ' + street.name + ' from ' + owner.name)
        answerOffer(buyer, owner, street, price)

    def answerOffer(buyer, owner, street, price):
        if random.random() <= owner.answerRate:
            # print(owner.name + ' accepted the offer.')
            trade(owner, buyer, street, price)
        #else:
            # print(owner.name + ' declined the offer.')

    turns = 0
    player.turn = True

    while turns < 10000:
        for pla in players:
            if pla.turn and pla.inGame:
                pla.move()
                for stre in streets:
                    if pla.pos == stre.pos:
                        if checkIfAv(stre, players):
                            if stre not in pla.streetsOwned:
                                pla.buyStreet(stre)
                        if pla.checkOwnedHouses(stre):
                            pla.buyHouse(stre)
                        else:
                            stre.checkRent(stre.name)
                            for p in players:
                                if p.name == getOwner(stre, players):
                                    p.cash += stre.rent
                            pla.cash -= stre.rent
                            # print(pla.name + ' paid ', stre.rent, ' to ', getOwner(stre, players))
                            pla.setNetWorth()
                            pla.sellHouse()
                for ereignisFeld in ereignisFelder:
                    if ereignisFeld.pos == pla.pos:
                        ereignisFeld.draw_card(ereignisKarten, pla, streets)
                        ereignisKarten.pop(0)
                        if len(ereignisKarten) == 0:
                            ereignisKarten = ['GoTo15', '+200', '+300', 'JailFree', 'GoTo1', '+100', 'GoTo40', 'GoTo22', 'GoBack3', 'House-50Hotel-200', 'House-80Hotel-230', '-40', '-30', 'Jail', '-50']
                            random.shuffle(ereignisKarten)
                        pla.setNetWorth()
                        pla.sellHouse()
                for gemeinschaftsFeld in gemeinschaftsFelder:
                    if gemeinschaftsFeld.pos == pla.pos:
                        gemeinschaftsFeld.landed_on += 1
                        gemeinschaftsFeld.draw_card(gemeinschaftsKarten, pla, players, streets)
                        gemeinschaftsKarten.pop(0)
                        if len(gemeinschaftsKarten) == 0:
                            gemeinschaftsKarten = ['+200*player', '+100', '+200', '+200', '+50', 'GoTo1', 'JailFree', '+400', '+200', '+50', 'GoTo4', '-200', 'Jail', '-200', '-100', '-50']
                            random.shuffle(gemeinschaftsKarten)
                        pla.setNetWorth()
                        pla.sellHouse()
                for bahn in bahnhoefe:
                    if bahn.pos == pla.pos:
                        if not checkIfAvBahnhof(bahn, players):
                            bahn.getRent(getOwnerBahnhof(bahn, players))
                            pla.cash -= bahn.rent
                            getOwnerBahnhof(bahn, players).cash += bahn.rent
                            # print(pla.name + ' paid ', bahn.rent, ' to ', getOwnerBahnhof(bahn, players).name)
                            pla.setNetWorth()
                            pla.sellHouse()
                        else:
                            pla.buyBahnhof(bahn)
                for we in werke:
                    if we.pos == pla.pos:
                        if not checkIfAvWerk(we, players):
                            we.getRent(getOwnerWerk(we, players), pla)
                            pla.cash -= we.rent
                            getOwnerWerk(we, players).cash += we.rent
                            # print(pla.name + ' paid ', we.rent, ' to ', getOwnerWerk(we, players).name)
                            pla.setNetWorth()
                            pla.sellHouse()
                        else:
                            pla.buyWerk(we)
                for st in steuern:
                    if st.pos == pla.pos:
                        pla.cash -= st.price
                        # print(pla.name + ' had to pay ', st.price, ' because he stepped on ' + st.name)
                        pla.setNetWorth()
                        pla.sellHouse()

                if pla.pos == 31:
                    pla.pos == 11
                    if pla.jailFree == False:
                        # print(pla.name + ' went to Jail and had to pay 50')
                        pla.cash -= 50
                        pla.setNetWorth()
                        pla.sellHouse()
                    # else:
                        # print(pla.name + ' went to Jail but had a Jail Free Card')

                findOwner(players, pla, streets)

                # if pla.name == 'Player 2':
                #     pla.buffer += 0.5
                if pla.name == 'Player 3':
                    pla.buffer += 1
                elif pla.name == 'Player 4':
                    pla.buffer += 1.5

                if pla.inGame and pla.cash < 0:
                    pla.sellHouse()

                for p in players:
                    if p.inGame == False:
                        players.remove(p)
                if len(players) == 1:
                    # print('Ended in ', turns, ' turns.')
                    # print('The Game is over!')
                    turns = 10000000
                    # print(players[0].name + ' won the Game!')
                    if players[0].name == 'Player 1':
                        player1Wins += 1
                    elif players[0].name == 'Player 2':
                        player2Wins += 1
                    elif players[0].name == 'Player 3':
                        player3Wins += 1
                    elif players[0].name == 'Player 4':
                        player4Wins += 1

                if pla.pos == 1:
                    pla.cash += 200
                pla.turn = False
            else:
                pla.turn = True
        turns += 1

outF.write('Player 1 won ' + str(player1Wins) + ' Games.\n')
outF.write('Player 2 won ' + str(player2Wins) + ' Games.\n')
outF.write('Player 3 won ' + str(player3Wins) + ' Games.\n')
outF.write('Player 4 won ' + str(player4Wins) + ' Games.\n')

print('SIM COMPLETED')
