import street

braun1 = street.Street(2)
braun2 = street.Street(4)
hellblau1 = street.Street(7)
hellblau2 = street.Street(9)
hellblau3 = street.Street(10)
pink1 = street.Street(12)
pink2 = street.Street(14)
pink3 = street.Street(15)
orange1 = street.Street(17)
orange2 = street.Street(19)
orange3 = street.Street(20)
rot1 = street.Street(22)
rot2 = street.Street(24)
rot3 = street.Street(25)
gelb1 = street.Street(27)
gelb2 = street.Street(28)
gelb3 = street.Street(30)
gruen1 = street.Street(32)
gruen2 = street.Street(33)
gruen3 = street.Street(35)
dunkelblau1 = street.Street(38)
dunkelblau2 = street.Street(40)

streets = [braun1, braun2, hellblau1, hellblau2, hellblau3, pink1, pink2, pink3, orange1, orange2, orange3, rot1, rot2, rot3, gelb1, gelb2, gelb3, gruen1, gruen2, gruen3, dunkelblau1, dunkelblau2]

def checkBreakEven(s):
    totalSpent = s.price
    rent = 0
    s.checkRent(s.name)
    if s.rent < totalSpent:
        s.houses += 1
        totalSpent += s.house_price
        s.checkRent(s.name)
    if s.rent < totalSpent:
        s.houses += 1
        totalSpent += s.house_price
        s.checkRent(s.name)
    if s.rent < totalSpent:
        s.houses += 1
        totalSpent += s.house_price
        s.checkRent(s.name)
    if s.rent < totalSpent:
        s.houses += 1
        totalSpent += s.house_price
        s.checkRent(s.name)
    if s.rent < totalSpent:
        s.houses += 1
        totalSpent += s.house_price
        s.checkRent(s.name)
    print(s.name, ' has to have ', s.houses, ' houses, to break even.')

for s in streets:
    checkBreakEven(s)
