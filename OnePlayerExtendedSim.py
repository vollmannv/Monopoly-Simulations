import player
import street
import ereignis
import gemeinschaft
import random

player = player.Player(1)
streets = []
ereignisFelder = []
gemeinschaftsFelder = []
outF = open('OnePlayerExtendedSimOut.txt', 'w')

ereignisKarten = ['GoTo15', '+200', '+300', 'JailFree', 'GoTo1', '+100', 'GoTo40', 'GoTo22', 'GoBack3', 'House-50Hotel-200', 'House-80Hotel-230', '-40', '-30', 'Jail', '-50']
random.shuffle(ereignisKarten)
gemeinschaftsKarten = ['+200*player', '+100', '+200', '+200', '+50', 'GoTo1', 'JailFree', '+400', '+200', '+50', 'GoTo4', '-200', 'Jail', '-200', '-100', '-50']

braun1 = street.Street(2)
gemeinschaft1 = gemeinschaft.Gemeinschaft(3)
braun2 = street.Street(4)
hellblau1 = street.Street(7)
ereignis1 = ereignis.Ereignis(8)
hellblau2 = street.Street(9)
hellblau3 = street.Street(10)
pink1 = street.Street(12)
pink2 = street.Street(14)
pink3 = street.Street(15)
orange1 = street.Street(17)
gemeinschaft2 = gemeinschaft.Gemeinschaft(18)
orange2 = street.Street(19)
orange3 = street.Street(20)
rot1 = street.Street(22)
ereignis2 = ereignis.Ereignis(23)
rot2 = street.Street(24)
rot3 = street.Street(25)
gelb1 = street.Street(27)
gelb2 = street.Street(28)
gelb3 = street.Street(30)
gruen1 = street.Street(32)
gruen2 = street.Street(33)
gemeinschaft3 = gemeinschaft.Gemeinschaft(34)
gruen3 = street.Street(35)
ereignis3 = ereignis.Ereignis(37)
dunkelblau1 = street.Street(38)
dunkelblau2 = street.Street(40)

streets.extend((braun1,braun2,hellblau1,hellblau2,hellblau3,pink1,pink2,pink3,orange1,orange2,orange3,rot1,rot2,rot3,gelb1,gelb2,gelb3,gruen1,gruen2,gruen3,dunkelblau1,dunkelblau2))
ereignisFelder.extend((ereignis1,ereignis2,ereignis3))
gemeinschaftsFelder.extend((gemeinschaft1,gemeinschaft2,gemeinschaft3))

counter = 0
totalLands = 0
jailCount = 0

while counter < 10000000:
    player.move()
    for street in streets:
        if street.pos == player.pos:
            street.landed_on += 1
    for ereignisFeld in ereignisFelder:
        if ereignisFeld.pos == player.pos:
            ereignisFeld.landed_on += 1
            ereignisFeld.draw_card(ereignisKarten, player)
            ereignisKarten.pop(0)
            if len(ereignisKarten) == 0:
                ereignisKarten = ['GoTo15', '+200', '+300', 'JailFree', 'GoTo1', '+100', 'GoTo40', 'GoTo22', 'GoBack3', 'House-50Hotel-200', 'House-80Hotel-230', '-40', '-30', 'Jail', '-50']
                random.shuffle(ereignisKarten)
    for gemeinschaftsFeld in gemeinschaftsFelder:
        if gemeinschaftsFeld.pos == player.pos:
            gemeinschaftsFeld.landed_on += 1
            gemeinschaftsFeld.draw_card(gemeinschaftsKarten, player)
            gemeinschaftsKarten.pop(0)
            if len(gemeinschaftsKarten) == 0:
                gemeinschaftsKarten = ['+200*player', '+100', '+200', '+200', '+50', 'GoTo1', 'JailFree', '+400', '+200', '+50', 'GoTo4', '-200', 'Jail', '-200', '-100', '-50']
                random.shuffle(gemeinschaftsKarten)
    if player.pos == 11:
        jailCount += 1
    counter += 1
    print((counter / 100000), ' percent complete', end= "\r")

for street in streets:
    totalLands += street.landed_on
for ereignisFeld in ereignisFelder:
    totalLands += ereignisFeld.landed_on
for gemeinschaftsFeld in gemeinschaftsFelder:
    totalLands += gemeinschaftsFeld.landed_on
totalLands += jailCount

for street in streets:
    outF.write(street.name + ': ' + str((street.landed_on/totalLands)*100) + '%\n' + str(street.landed_on) + '\n\n')
for ereignisFeld in ereignisFelder:
    outF.write('Ereignis Feld' + str(ereignisFelder.index(ereignisFeld)) + ':' + str((ereignisFeld.landed_on/totalLands)*100) + '%\n' + str(ereignisFeld.landed_on) + '\n\n')
for gemeinschaftsFeld in gemeinschaftsFelder:
    outF.write('Gemeinschafts Feld' + str(gemeinschaftsFelder.index(gemeinschaftsFeld)) + ':' + str((gemeinschaftsFeld.landed_on/totalLands)*100) + '%\n' + str(gemeinschaftsFeld.landed_on) + '\n\n')
outF.write('Gefaengnis: ' + str((jailCount/totalLands)*100) + '%\n' + str(jailCount))
print('COMPLETED')
outF.close()
