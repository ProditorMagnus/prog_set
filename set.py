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

def convert_selection(selection):
    # praegusel kujul tuleb sisend sõnena
    # laual olevate kaartide järjekorranumbrid
    sel = selection.replace(' ','').split(',')

    # loob enniku kaartidest vastavalt kasutaja sisestatud järjekorranumbritele
    cards = on_table[int(sel[0])-1],on_table[int(sel[1])-1],on_table[int(sel[2])-1]

    # sorteerib kaardid, et kontrollida, kas need on set
    sorted_cards = tuple(sorted(cards))
    if sorted_cards in find_sets(sorted_cards):
        return sorted_cards

# funktsioon otsib valitud kaartide asemele sobivad, et garanteerida laual vähemalt üks set
def pick_set_cards(selected_cards):
    required = []
    temp_table = []

    # loob koopia laual olevatest kaartidest
    for a in on_table:
        temp_table.append(a)
    # võtab koopiast välja eemaldatavad kaardid
    for b in selected_cards:
        temp_table.remove(b)

    # võtab järelejäänud kaartidest 2 kaarti ja otsib neile gamedeckist kolmanda, et moodustada set
    while len(find_sets(temp_table)) == 0:
        for c in range(len(temp_table)):
            i=temp_table[c]
            for d in range(c+1,len(temp_table)):
                j=temp_table[d]
                needed = []
                for atr in range(4):
                    if(i[atr]==j[atr]):
                        needed.append(i[atr])
                    else:
                        needed.append((-i[atr]-j[atr])%3)
                needed = (needed[0], needed[1], needed[2], needed[3])
                if(needed in gamedeck):
                    required.append(gamedeck.pop(gamedeck.index(needed)))

                    # kui üks kaart olemas, lisatakse gamedeckist suvalised juurde
                    while len(temp_table) + len(required) < len(on_table):
                        required.append(gamedeck.pop())
                    return required
                else:
                    print("-------------------------------------------------------------------")
                    continue
    # kui järelejäänute hulgas on set olemas, lisatakse lihtsalt vajalik hulk kaarte
    while len(temp_table) + len(required) < len(on_table):
        required.append(gamedeck.pop())
    return required


#funktsioon vahetab valitud kaartide asemele uued
def replace_set(selection):
    # ei kontrolli, kas valitakse kaart, mida pole laual - graafiline liides peaks välistama võimaluse
    sel = selection.replace(' ','').split(',')
    for card in range(3):
        # asendab kaardid pakist võetud uutega, nii et laual järjekord ei muutu
        on_table[int(sel[card])-1] = replace.pop()


# programm valib laualt ise kaardid
def set_index(set_values):
    temp = list(set_values)
    ret = str(on_table.index(temp[0][0])+1) + "," + str(on_table.index(temp[0][1])+1) + "," + str(on_table.index(temp[0][2])+1)
    return ret


def print_table():
    row = 1
    print("\nKaardid")
    for i in on_table:
        print(str(row) + ".", str(i))
        row += 1
    print("Laual on", str(len(find_sets(on_table))), "setti:")
    print(str(find_sets(on_table)))
    print("Pakis on veel", len(gamedeck), "kaarti. Punktid:", str(score))

on_table = []
score = 0

# Mängu alguses tõmmatakse 12 kaarti
do_draw(12)
    
# Alati ei jää viimaste kaartide hulka seti.
while len(gamedeck) > 0:
    print_table()
    time_start = time()
    sets = len(find_sets(on_table))
    if sets > 0:
        selection = set_index(find_sets(on_table)) #input("Vali kaardid (kujul: 1,10,6): ")
        selected_cards = convert_selection(selection)
        replace = pick_set_cards(selected_cards)
        replace_set(selection)
        time_stop = time()
        score += round(120 - (time_stop - time_start)//sets) # Mida rohkem sette laual, seda vähem punkte; praegu läheb ka miinusesse
    else:
        # seti puudumisel tõmbab täiendavad 3 kaarti; praegu jääb sellisel kujul mängu lõpuni 3 kaarti rohkem, kuna valitud kaardid asendatakse
        # poleks vaja, kui programm tõmbaks kaardid alati nii, et leiduks ka set
        do_draw(3)

# Lõpetab mängu ka siis, kui laual on veel mõni set
print("Mäng on läbi. Sinu punktisumma on:", str(score))

# input on mul lihtsalt selle jaoks vaja et programm kohe kinni ei läheks - kasutan shell execute current file mitte mõnda pythoni asja
# input()