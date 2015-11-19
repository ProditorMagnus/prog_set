# Version 0.01

from random import randint

# Cards: quantity (1, 2, 3), color (r, b, g), fill (e(mpty), s(triped), f(ull)), shape (s, o, d)
# create fulldeck
fulldeck = [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 2, 1], [1, 1, 2, 2], [1, 1, 2, 3], [1, 1, 3, 1], [1, 1, 3, 2], [1, 1, 3, 3], [1, 2, 1, 1], [1, 2, 1, 2], [1, 2, 1, 3], [1, 2, 2, 1], [1, 2, 2, 2], [1, 2, 2, 3], [1, 2, 3, 1], [1, 2, 3, 2], [1, 2, 3, 3], [1, 3, 1, 1], [1, 3, 1, 2], [1, 3, 1, 3], [1, 3, 2, 1], [1, 3, 2, 2], [1, 3, 2, 3], [1, 3, 3, 1], [1, 3, 3, 2], [1, 3, 3, 3], [2, 1, 1, 1], [2, 1, 1, 2], [2, 1, 1, 3], [2, 1, 2, 1], [2, 1, 2, 2], [2, 1, 2, 3], [2, 1, 3, 1], [2, 1, 3, 2], [2, 1, 3, 3], [2, 2, 1, 1], [2, 2, 1, 2], [2, 2, 1, 3], [2, 2, 2, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 1], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 1, 1], [2, 3, 1, 2], [2, 3, 1, 3], [2, 3, 2, 1], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 1], [2, 3, 3, 2], [2, 3, 3, 3], [3, 1, 1, 1], [3, 1, 1, 2], [3, 1, 1, 3], [3, 1, 2, 1], [3, 1, 2, 2], [3, 1, 2, 3], [3, 1, 3, 1], [3, 1, 3, 2], [3, 1, 3, 3], [3, 2, 1, 1], [3, 2, 1, 2], [3, 2, 1, 3], [3, 2, 2, 1], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 1], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 1, 1], [3, 3, 1, 2], [3, 3, 1, 3], [3, 3, 2, 1], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 1], [3, 3, 3, 2], [3, 3, 3, 3]]
gamedeck = fulldeck[:]
shuffle(gamedeck)

def checkifset(card1,card2,card3):
    set = 0
    for i in range(4):
        if card1[i] == card2[i] and card1[i] == card3[i]:
            set += 1
        elif card1[i] != card2[i] and card1[i] != card3[i] and card2[i] != card3[i]:
            set += 1
        else:
            return False
    if set == 4:
        return True

#checkifset([1,1,1,1],[2,2,2,2],[3,3,3,3])
true = []
false = []
for i in range(81):
    card1 = fulldeck[randint(0,80)]
    card2 = fulldeck[randint(0,80)]
    card3 = fulldeck[randint(0,80)]
    if checkifset(card1,card2,card3) == True:
        true.append(card1)
        true.append(card2)
        true.append(card3)
        true.append(i)
    else:
        false.append(card1)
        false.append(card2)
        false.append(card3)
        false.append(i)

print("True: " + str(true))
print("False: " + str(false))
