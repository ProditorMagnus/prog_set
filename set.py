# Version 0.01

from random import randint
from random import shuffle
# from copy import deepcopy

# Cards: quantity (1, 2, 3), color (r, b, g), fill (e(mpty), s(triped), f(ull)), shape (s, o, d)
# create fulldeck

# konvertisin, \[([0-9]), ([0-9]), ([0-9]), ([0-9])\] -> \(\1, \2, \3, \4\) ning muutsin 1,2,3 -> 0,1,2 - nii saab jääkide abil leida kahe kaardi järgi kolmandat

# fulldeck = [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 2, 1], [1, 1, 2, 2], [1, 1, 2, 3], [1, 1, 3, 1], [1, 1, 3, 2], [1, 1, 3, 3], [1, 2, 1, 1], [1, 2, 1, 2], [1, 2, 1, 3], [1, 2, 2, 1], [1, 2, 2, 2], [1, 2, 2, 3], [1, 2, 3, 1], [1, 2, 3, 2], [1, 2, 3, 3], [1, 3, 1, 1], [1, 3, 1, 2], [1, 3, 1, 3], [1, 3, 2, 1], [1, 3, 2, 2], [1, 3, 2, 3], [1, 3, 3, 1], [1, 3, 3, 2], [1, 3, 3, 3], [2, 1, 1, 1], [2, 1, 1, 2], [2, 1, 1, 3], [2, 1, 2, 1], [2, 1, 2, 2], [2, 1, 2, 3], [2, 1, 3, 1], [2, 1, 3, 2], [2, 1, 3, 3], [2, 2, 1, 1], [2, 2, 1, 2], [2, 2, 1, 3], [2, 2, 2, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 1], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 1, 1], [2, 3, 1, 2], [2, 3, 1, 3], [2, 3, 2, 1], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 1], [2, 3, 3, 2], [2, 3, 3, 3], [3, 1, 1, 1], [3, 1, 1, 2], [3, 1, 1, 3], [3, 1, 2, 1], [3, 1, 2, 2], [3, 1, 2, 3], [3, 1, 3, 1], [3, 1, 3, 2], [3, 1, 3, 3], [3, 2, 1, 1], [3, 2, 1, 2], [3, 2, 1, 3], [3, 2, 2, 1], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 1], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 1, 1], [3, 3, 1, 2], [3, 3, 1, 3], [3, 3, 2, 1], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 1], [3, 3, 3, 2], [3, 3, 3, 3]]
fulldeck = [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 0, 2), (0, 0, 1, 0), (0, 0, 1, 1), (0, 0, 1, 2), (0, 0, 2, 0), (0, 0, 2, 1), (0, 0, 2, 2), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 0, 2), (0, 1, 1, 0), (0, 1, 1, 1), (0, 1, 1, 2), (0, 1, 2, 0), (0, 1, 2, 1), (0, 1, 2, 2), (0, 2, 0, 0), (0, 2, 0, 1), (0, 2, 0, 2), (0, 2, 1, 0), (0, 2, 1, 1), (0, 2, 1, 2), (0, 2, 2, 0), (0, 2, 2, 1), (0, 2, 2, 2), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 0, 2), (1, 0, 1, 0), (1, 0, 1, 1), (1, 0, 1, 2), (1, 0, 2, 0), (1, 0, 2, 1), (1, 0, 2, 2), (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 0, 2), (1, 1, 1, 0), (1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 2, 0), (1, 1, 2, 1), (1, 1, 2, 2), (1, 2, 0, 0), (1, 2, 0, 1), (1, 2, 0, 2), (1, 2, 1, 0), (1, 2, 1, 1), (1, 2, 1, 2), (1, 2, 2, 0), (1, 2, 2, 1), (1, 2, 2, 2), (2, 0, 0, 0), (2, 0, 0, 1), (2, 0, 0, 2), (2, 0, 1, 0), (2, 0, 1, 1), (2, 0, 1, 2), (2, 0, 2, 0), (2, 0, 2, 1), (2, 0, 2, 2), (2, 1, 0, 0), (2, 1, 0, 1), (2, 1, 0, 2), (2, 1, 1, 0), (2, 1, 1, 1), (2, 1, 1, 2), (2, 1, 2, 0), (2, 1, 2, 1), (2, 1, 2, 2), (2, 2, 0, 0), (2, 2, 0, 1), (2, 2, 0, 2), (2, 2, 1, 0), (2, 2, 1, 1), (2, 2, 1, 2), (2, 2, 2, 0), (2, 2, 2, 1), (2, 2, 2, 2)]
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

def find_sets(cards):
	# iga kahese grupi kohta, kas eksisteerib kindel kolmas kaart
	# result r
	# r = []
	r = set()
	# peaks olema keerukusega NlogN
	for a in range(len(cards)):
		i=cards[a]
		for b in range(a+1,len(cards)):
			j=cards[b]
			if(i==j):
				continue
			# print(i,j)
			needed = []
			# on parem, kui võimalikud väärtused on 0,1,2 mitte 1,2,3
			# saab olla 0,1,2
			# kui on 0,1, vaja 2
			# kui on 0,2, vaja 1
			# kui on 1,2, vaja 0
			# (-a-b)%3
			for atr in range(4):
				if(i[atr]==j[atr]):
					needed.append(i[atr])
				else:
					
					needed.append((-i[atr]-j[atr])%3)
			# print(needed)
			needed = (needed[0], needed[1], needed[2], needed[3])
			if(needed in cards):
				# r.append(tuple(sorted((i,j,needed))))
				# print(tuple(sorted((i,j,needed))))
				# input()
				r.add(tuple(sorted((i,j,needed))))
			# probleemiks on, et list on järjestatud seega a,b,c ja a,c,b ja b,c,a on kõik võimalikud, ning loetakse erinevaks
			# seetõttu muutsin gamedeck -> tuple - nüüd saab siin r olla set(), ning kuna kolmik sorteeritakse siis korduvaid ei jää
			# input()
	return r

#checkifset([1,1,1,1],[2,2,2,2],[3,3,3,3])
""" - paistis et seda pole vaja. Muide, need card1, card2, card3 võivad siin ka kõik samad olla
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
"""

def do_draw(amount=12):
	one_draw = []
	for i in range(amount):
		one_draw.append(gamedeck.pop())

	tmp = find_sets(one_draw)
	print("Kaardid")
	for i in one_draw:
		print(i)
	print("Setid")
	for i in tmp:
		print(i)

do_draw()


# input on mul lihtsalt selle jaoks vaja et programm kohe kinni ei läheks - kasutan shell execute current file mitte mõnda pythoni asja
input()
