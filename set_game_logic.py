from random import randint
from random import shuffle
# from time import time
# from copy import deepcopy

# see peaks set.py üle võtma sobival kujul, hetkel on siit kasutuses vaid card_repr ja find_sets

# create fulldeck

def card_repr(s):
	return (int(s[0]),int(s[1]),int(s[2]),int(s[3]))

def card_str(t):
	return str(t[0])+str(t[1])+str(t[2])+str(t[3])

# gamedeck = fulldeck[:]
# shuffle(gamedeck)

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

def do_draw(amount=12): # märkides amountiks 81, tagastab find_sets(on_table) kõik 1080 võimalikku setti.
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
    temp_table = on_table[:]
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


# input on mul lihtsalt selle jaoks vaja et programm kohe kinni ei läheks - kasutan shell execute current file mitte mõnda pythoni asja
# input()