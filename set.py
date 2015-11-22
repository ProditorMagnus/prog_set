from random import randint
from random import shuffle
from time import time
# from copy import deepcopy

# Cards: quantity (1, 2, 3), color (r, b, g), fill (e(mpty), s(triped), f(ull)), shape (s, o, d)
# create fulldeck

fulldeck = [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 0, 2), (0, 0, 1, 0), (0, 0, 1, 1), (0, 0, 1, 2), (0, 0, 2, 0), (0, 0, 2, 1), (0, 0, 2, 2), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 0, 2), (0, 1, 1, 0), (0, 1, 1, 1), (0, 1, 1, 2), (0, 1, 2, 0), (0, 1, 2, 1), (0, 1, 2, 2), (0, 2, 0, 0), (0, 2, 0, 1), (0, 2, 0, 2), (0, 2, 1, 0), (0, 2, 1, 1), (0, 2, 1, 2), (0, 2, 2, 0), (0, 2, 2, 1), (0, 2, 2, 2), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 0, 2), (1, 0, 1, 0), (1, 0, 1, 1), (1, 0, 1, 2), (1, 0, 2, 0), (1, 0, 2, 1), (1, 0, 2, 2), (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 0, 2), (1, 1, 1, 0), (1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 2, 0), (1, 1, 2, 1), (1, 1, 2, 2), (1, 2, 0, 0), (1, 2, 0, 1), (1, 2, 0, 2), (1, 2, 1, 0), (1, 2, 1, 1), (1, 2, 1, 2), (1, 2, 2, 0), (1, 2, 2, 1), (1, 2, 2, 2), (2, 0, 0, 0), (2, 0, 0, 1), (2, 0, 0, 2), (2, 0, 1, 0), (2, 0, 1, 1), (2, 0, 1, 2), (2, 0, 2, 0), (2, 0, 2, 1), (2, 0, 2, 2), (2, 1, 0, 0), (2, 1, 0, 1), (2, 1, 0, 2), (2, 1, 1, 0), (2, 1, 1, 1), (2, 1, 1, 2), (2, 1, 2, 0), (2, 1, 2, 1), (2, 1, 2, 2), (2, 2, 0, 0), (2, 2, 0, 1), (2, 2, 0, 2), (2, 2, 1, 0), (2, 2, 1, 1), (2, 2, 1, 2), (2, 2, 2, 0), (2, 2, 2, 1), (2, 2, 2, 2)]
gamedeck = fulldeck[:]
shuffle(gamedeck)

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

def do_draw(amount=12): # märkides amountiks 81, tagastab funktsioon find_sets(ontable) kõik 1080 võimalikku setti.
    for i in range(amount):
            on_table.append(gamedeck.pop())

# Tegin järgnevate jaoks eraldi funktsioonid
"""
	tmp = find_sets(on_table)
	print("Kaardid")
	for i in on_table:
		print(i)
	print("Setid")
	for i in tmp:
		print(i)
"""

def remove_set(selection):
    # ei kontrolli, kas valitakse kaart, mida pole laual - graafiline liides peaks välistama võimaluse
    # praegusel kujul tuleb sisend sõnena
    # laual olevate kaartide järjekorranumbrid
    sel = selection.replace(' ','').split(',')

    # loob enniku kaartidest vastavalt kasutaja sisestatud järjekorranumbritele
    cards = on_table[int(sel[0])-1],on_table[int(sel[1])-1],on_table[int(sel[2])-1]

    # sorteerib kaardid, et kontrollida, kas need on set
    sorted_cards = tuple(sorted(cards))
    if sorted_cards in find_sets(cards):
        for card in range(3):
            # asendab kaardid pakist võetud uutega, nii et laual järjekord ei muutu
            on_table[int(sel[card])-1] = gamedeck.pop()

def print_table():
    row = 1
    print("\nKaardid")
    for i in on_table:
        print(str(row) + ".", str(i))
        row += 1
    print("Laual on", str(len(find_sets(on_table))), "setti:")
    print(str(find_sets(on_table)))
    print("Pakis on veel", len(gamedeck), "kaarti.")

on_table = []
score = 0

# Mängu alguses tõmmatakse 12 kaarti
do_draw()

# Mäng ei oska praegu arvestada 12 kaardi piiranguga, st valib pakist viimased kaardid ja ei arvesta, et 12 kaardi seas PEAB olema set
while len(gamedeck) > 0:
    print_table()
    time_start = time()
    sets = len(find_sets(on_table))
    if sets > 0:
        selection = input("Vali kaardid (kujul: 1,10,6): ")
        remove_set(selection)
        time_stop = time()
        score += round(time_stop - time_start)//sets # Mida rohkem sette laual, seda vähem punkte
    else:
        # seti puudumisel tõmbab täiendavad 3 kaarti; praegu jääb sellisel kujul mängu lõpuni 3 kaarti rohkem, kuna valitud kaardid asendatakse
        # poleks vaja, kui programm tõmbaks kaardid alati nii, et leiduks ka set
        do_draw(3)

# Lõpetab mängu ka siis, kui laual on veel mõni set
print("Mäng on läbi. Sinu punktisumma on:", str(score))

# input on mul lihtsalt selle jaoks vaja et programm kohe kinni ei läheks - kasutan shell execute current file mitte mõnda pythoni asja
# input()