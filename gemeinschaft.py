class Gemeinschaft:
    def __init__(self, pos):
        self.pos = pos
        self.landed_on = 0

    def draw_card(self, cards, player, players, streets):
        # print(player.name + ' drew a Gemeinschafts Karte.')
        if cards[0] == 'GoTo1':
            player.pos = 1
            # print(player.name + ' went to Los.')
        elif cards[0] == 'GoTo4':
            player.pos = 4
            # print(player.name + ' went to Braun 2.')
        elif cards[0] == 'Jail':
            player.pos = 11
            if player.jailFree == False:
                # print(player.name + ' went to Jail and had to pay 50')
                player.cash -= 50
                player.setNetWorth()
                player.sellHouse()
            # else:
                # print(player.name + ' went to Jail but had a Jail Free Card')
        elif cards[0] == '+200*player':
            player.cash += 200*(len(players)-1)
            for el in players:
                if el != player:
                    el.cash -= 200
            # print(player.name + ' earned 200 from every Player.')
        elif cards[0] == '+100':
            player.cash += 100
            # print(player.name + ' earned 100.')
        elif cards[0] == '+200':
            player.cash += 200
            # print(player.name + ' earned 200.')
        elif cards[0] == '+50':
            player.cash += 50
            # print(player.name + ' earned 50.')
        elif cards[0] == 'JailFree':
            player.jailFree = True
            # print(player.name + ' drew a Jail Free Card.')
        elif cards[0] == '+400':
            player.cash += 400
            # print(player.name + ' earned 400.')
        elif cards[0] == '-200':
            player.cash -= 200
            # print(player.name + ' lost 200.')
        elif cards[0] == '-100':
            player.cash -= 100
            # print(player.name + ' lost 100.')
        elif cards[0] == '-50':
            player.cash -= 50
            # print(player.name + ' lost 50.')
