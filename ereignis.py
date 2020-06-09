class Ereignis:
    def __init__(self,pos):
        self.pos = pos

    def draw_card(self,cards,player,streets):
        # print(player.name + ' drew a Ereignis Karte')
        if cards[0] == 'Jail':
            player.pos = 11
            if player.jailFree == False:
                # print(player.name + ' went to Jail and had to pay 50')
                player.cash -= 50
                player.setNetWorth()
                player.sellHouse()
            # else:
                # print(player.name + ' went to Jail but had a Jail Free Card')
        elif cards[0] == 'GoTo40':
            player.pos = 40
            # print(player.name + ' went to Dunkelblau 2')
        elif cards[0] == 'GoTo1':
            player.pos = 1
            # print(player.name + ' went to Los')
        elif cards[0] == 'GoTo15':
            player.pos = 15
            # print(player.name + ' went to Pink 3')
        elif cards[0] == 'GoTo22':
            player.pos = 22
            # print(player.name + ' went to Rot 1')
        elif cards[0] == 'GoBack3':
            player.pos -= 3
            # print(player.name + ' went back 3 spots')
        elif cards[0] == '+200':
            player.cash += 200
            # print(player.name + ' earned 200.')
        elif cards[0] == '+100':
            player.cash += 100
            # print(player.name + ' earned 100.')
        elif cards[0] == '+300':
            player.cash += 300
            # print(player.name + ' earned 300.')
        elif cards[0] == 'House-50Hotel-200':
            counterHouse = 0
            counterHotel = 0
            for el in player.streetsOwned:
                if el.houses > 4:
                    player.cash -= 200
                    counterHotel += 1
                else:
                    player.cash -= 50 * el.houses
                    counterHouse += el.houses
            # print(player.name + ' has to pay ' + str(counterHotel * 200) + ' for his hotels and ' + str(counterHouse*50) + ' for his houses.')
        elif cards[0] == 'House-80Hotel-230':
            counterHouse = 0
            counterHotel = 0
            for el in player.streetsOwned:
                if el.houses > 4:
                    player.cash -= 230
                    counterHotel += 1
                else:
                    player.cash -= 80 * el.houses
                    counterHouse += el.houses
            # print(player.name + ' has to pay ' + str(counterHotel * 230) + ' for his hotels and ' + str(counterHouse*80) + ' for his houses.')
        elif cards[0] == '-40':
            player.cash -= 40
            # print(player.name + ' lost 40.')
        elif cards[0] == '-30':
            player.cash -= 30
            # print(player.name + ' lost 30.')
        elif cards[0] == '-50':
            player.cash -= 50
            # print(player.name + ' lost 5 0.')
