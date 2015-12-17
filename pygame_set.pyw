from random import randint
from random import shuffle
from time import time, sleep
import pygame # http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
from global_vars import *
from set_card_data import *
import os

# Tõmbab pakist kaardid nii, et nende hulgas on vähemalt üks set
def draw_new_deck(amount=12,recursion=0):
    if(recursion>50):
        game_over()
        return True
        # input()
    global cards_on_table
    cards_on_table = []
    for i in range(amount):
        try:
            card_on_table(card_str(gamedeck[0]),card_pos(i))
        except:
            amount-=3
    if no_set_on_table():
        shuffle(gamedeck)
        draw_new_deck(amount,recursion+1)

# Tagastab kaardi väärtuse sõnena: (0,0,0,0) > '0000'
def card_str(t):
	return str(t[0])+str(t[1])+str(t[2])+str(t[3])

# Joonistab kaardi ekraanile
def card_on_table(card,location):
    # pakist ära võtta need mis lauale panna
    try:
        gamedeck.remove(card_repr(card))
        cards_on_table.append(card) # append paneb uued kaardid valele kohale

        # card_tuples_on_table=[]
        # for i in cards_on_table:
            # card_tuples_on_table.append(card_repr(i))
        gamescreen.blit(eval("card_"+card),location)
    except:
        if len(gamedeck) > 0:
            reset_table_state(9)
        else:
            game_over()

# Seti puudumisel tagastatakse laual olevad kaardid pakki, segatakse ning valitakse uued kaardid asemele
def reset_table_state(amount=12):
    # Ekraanile 2.2-ks sekundiks tekst, et kaardid segatakse uuesti
    sets_number_to_screen()
    text_loc_x = table_frame_width+card_width*2+card_spacing*2
    text_loc_y = table_frame_height+card_height*1.5+card_spacing
    pygame.draw.rect(gamescreen,green,(card_area)) # Joonistab üle mänguvälja
    message = font.render("NO AVAILABLE SETS. RESHUFFLING.",0,red)
    gamescreen.blit(message, (text_loc_x-248,text_loc_y-60))
    pygame.display.update()
    sleep(1)
    pygame.draw.rect(gamescreen,green,(card_area)) # Joonistab üle mänguvälja

    global cards_on_table
    for i in range(len(cards_on_table)-1,-1,-1):
        c = gamedeck.append(card_repr(cards_on_table[i]))

    if(draw_new_deck(amount)):
        return True

    global on_table_selected
    for i in range(12):
        gamescreen.blit(deselected_card,card_pos(i))
    on_table_selected = []

# Tagastab kaardi väärtuse ennikuna: '0000' > (0,0,0,0)
def card_repr(s):
	return (int(s[0]),int(s[1]),int(s[2]),int(s[3]))

# Tagastab kaardi asukoha laual
def card_pos(i):
	return eval("card"+str(i)+"_loc")

# Otsib kaartide hulgast seti
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
			needed = (needed[0], needed[1], needed[2], needed[3])
			if(needed in cards):
				r.add(tuple(sorted((i,j,needed))))
	return r

# Reageerib klikile mänguväljal
def screen_click(position):
    x = position[0]
    y = position[1]
    if x > card0_loc[0] and y > card0_loc[1] and x < card11_loc[0]+150 and y < card11_loc[1]+220:
        click_card(position)

# Reageerib klikile kaardiväljal, selekteerib kaardi
def click_card(position):
    x = position[0]
    y = position[1]
    width = 220
    height = 150
    if x > card0_loc[0] and x < card0_loc[0]+height:
        if y > card0_loc[1] and y < card0_loc[1]+width:
            select_card(card0_loc)
        if y > card4_loc[1] and y < card4_loc[1]+width:
            select_card(card4_loc)
        if y > card8_loc[1] and y < card8_loc[1]+width:
            select_card(card8_loc)
    if x > card1_loc[0] and x < card1_loc[0]+height:
        if y > card1_loc[1] and y < card1_loc[1]+width:
            select_card(card1_loc)
        if y > card5_loc[1] and y < card5_loc[1]+width:
            select_card(card5_loc)
        if y > card9_loc[1] and y < card9_loc[1]+width:
            select_card(card9_loc)
    if x > card2_loc[0] and x < card2_loc[0]+height:
        if y > card2_loc[1] and y < card2_loc[1]+width:
            select_card(card2_loc)
        if y > card6_loc[1] and y < card6_loc[1]+width:
            select_card(card6_loc)
        if y > card10_loc[1] and y < card10_loc[1]+width:
            select_card(card10_loc)
    if x > card3_loc[0] and x < card3_loc[0]+height:
        if y > card3_loc[1] and y < card3_loc[1]+width:
            select_card(card3_loc)
        if y > card7_loc[1] and y < card7_loc[1]+width:
            select_card(card7_loc)
        if y > card11_loc[1] and y < card11_loc[1]+width:
            select_card(card11_loc)

# Kontrollib, kas kaart on selekteeritud või mitte ning vastavalt sellele
# deselekteerib või selekteerib selle
def select_card(position):
    no_set_on_table()
    try:
        this_card = card_repr(cards_on_table[((position[0])//(card_width+card_spacing))+4*(position[1])//(card_height+card_spacing)])
    except:
        game_over()
        return
    if this_card in on_table_selected:
        # card_on_table(deselected_card,position)
        gamescreen.blit(deselected_card,position)
        on_table_selected.remove(this_card)
    else:
        if len(on_table_selected) > 2:
            # muutsin nii, et siis lihtsalt eemaldab vanima
            last_card = (on_table_selected[0])
            # deselect this
            gamescreen.blit(deselected_card,card_pos(cards_on_table.index(card_str(last_card))))
            on_table_selected.remove(last_card)
            # return
        gamescreen.blit(selected_card,position)
        on_table_selected.append(this_card)
        if(find_sets(on_table_selected)):
            # augud tekitada
            for i in range(len(on_table_selected)-1,-1,-1):
                
                gamescreen.blit(card_xxxx,card_pos(cards_on_table.index(card_str(on_table_selected[i]))))
                
                if(len(gamedeck)>0):
                    card_to_table(card_str(gamedeck[0]),(cards_on_table.index(card_str(on_table_selected[i]))))
                else:
                    game_over()
                
                cards_on_table.pop(cards_on_table.index(card_str(on_table_selected[i])))
                on_table_selected.pop()
            if(no_set_on_table()):
                success_events()
                if len(gamedeck) > 0:
                    reset_table_state()
                    sleep(0.6) # Vajalik, et reset_table_state ei jookseks kokku
                    if gamesounds == True:
                        drawcards.play()
                        sleep(0.6)
                else:
                    if len(gamedeck) == 0 and sets_available() == 0:
                        game_over()
                return
            # ja augud täita
            success_events()
            return
        else:
            if(len(on_table_selected) > 2):
                print("No sets in selection.",on_table_selected) # Siia lisada veateade - tekitan helifaili
                if gamesounds == True:
                    wontwork.play()
                return


# Tagastab True või False vastavalt kas laual leidub sette või mitte
def no_set_on_table():
    card_tuples_on_table=[]
    for i in cards_on_table:
        card_tuples_on_table.append(card_repr(i))
    return find_sets(card_tuples_on_table)==set()

# Paigutab uue kaardi kõrvaldatud kaardi asemele
def card_to_table(card,index):
    gamedeck.remove(card_repr(card))
    cards_on_table.insert(index,card)

    # card_tuples_on_table=[]
    # for i in cards_on_table:
        # card_tuples_on_table.append(card_repr(i))
    # siin on veel vara kontrollida, eelmist pole veel eemaldatud

    gamescreen.blit(eval("card_"+card),card_pos(index))

# Lõpetab mängu
def game_over():
    success_events()
    # finalise everything, stop accepting further card selections and all
    pygame.draw.rect(gamescreen,white,(card_area)) # Joonistab üle mänguvälja
    text_loc_x = table_frame_width+card_width*2+card_spacing*2
    text_loc_y = table_frame_height+card_height*1.5+card_spacing
    message_1 = font.render("NO MORE SETS AVAILABLE.",0,red)
    message_2 = font.render("GAME OVER!",0,red)
    message_3 = font.render("YOUR FINAL SCORE: "+str(score).rjust(6,"0"),0,green)
    gamescreen.blit(message_1, (text_loc_x-184,text_loc_y-100))
    gamescreen.blit(message_2, (text_loc_x-80,text_loc_y-60))
    gamescreen.blit(message_3, (text_loc_x-192,text_loc_y+20))
    pygame.display.update()
    input()
##    sleep(5)
    pygame.quit()
##    exec(open("pygame_set.py").read())
##    os.system("python pygame_set.py")
    quit()

# joonistab järelejäänud kaartidest koosneva kaardipaki
def deck_on_table():
    loc_x = table_frame_width+card_width*4+card_spacing*4
    loc_y = table_frame_height
    pygame.draw.rect(gamescreen,green,(loc_x,loc_y-14,card_width+14,card_height+14))
    for card in range((len(gamedeck)+3)//6):
        # +3 abil see näitab kui pakk on tühi õigel ajal
        # see on erinev tavalistest kaartidest
        gamescreen.blit(deck_card,(loc_x,loc_y))
        loc_x += 2
        loc_y -= 2
    counter = font.render(str(len(gamedeck)),0,violet)
    if len(gamedeck) > 0:
        gamescreen.blit(counter, [loc_x+25,loc_y+170])

# Toimingud seti edukal leidmisel
def success_events():
    stop_time = time()
    sets_number_to_screen()
    deck_on_table()
    reset_hints()
    # vaja muuta globaalseid muutujaid
    global start_time
    global score
    global penalty
    global bonus
    global hints
    global hint_counter
    global hint_counter_sets
    hints = create_hints()
    hint_counter = 0
    hint_counter_sets = 0
    score_time = int(stop_time-start_time)*10
    if score_time < 999:
        score += int(bonus)-penalty
    else:
        if score > penalty:
            score -= penalty
        else:
            score = 0
    penalty = 0
    score_display()
    penalty_display()
    if gamesounds == True:
        success.play()
    start_time = time()
    bonus = 999

# Tagastab võimalike settide hulga laual
def sets_available():
    sets_on_table = []
    for i in cards_on_table:
        sets_on_table.append(card_repr(i))
    return len(find_sets(sets_on_table))

# Joonistab ekraanile laual olevate kaartide hulgas oleva võimalike settide hulga
def sets_number_to_screen():
    pygame.draw.rect(gamescreen,green,(260,5,35,25)) # Joonistab üle settide hulga, arvestab kahekohalisi arve
    counter = font.render("SETS AVAILABLE: " + str(sets_available()),0,yellow)
    gamescreen.blit(counter, [5,0])

# Joonistab ekraanile seni kogutud punktide hulga
def score_display():
    pygame.draw.rect(gamescreen,green,(430,5,105,25)) # Joonistab üle skoori
    counter = font.render("SCORE: " + str(score).rjust(6,"0"),0,yellow)
    gamescreen.blit(counter, [320,0])

# Joonistab ekraanile saadava boonuse
def bonus_display():
    pygame.draw.rect(gamescreen,green,(685,5,55,25)) # Joonistab üle boonuse
    if bonus > 0:
        color = yellow
    else:
        color = red
    counter = font.render("BONUS: " + str(int(bonus)).rjust(3,"0"),0,color)
    gamescreen.blit(counter, [575,0])

# Joonistab ekraanile saadava karistuse
def penalty_display():
    pygame.draw.rect(gamescreen,green,(740,5,90,25)) # Joonistab üle penalty
    if penalty > 0:
        counter = font.render("-" + str(penalty).rjust(4,"0"),0,red)
        gamescreen.blit(counter, [740,0])

# Joonistab ekraanile klahvikombinatsioonid ja heli staatuse
def shortcut_display():
    short_loc_x = 650
    short_loc_y = 510
    pygame.draw.rect(gamescreen,green,(short_loc_x,short_loc_y,170,200))
    row_1 = font.render("For hints:",0,yellow)
    row_2 = font.render("RClick/'H'",0,yellow)
    row_3 = font.render("To toggle",0,yellow)
    row_4 = font.render("sound: 'S'",0,yellow)
    if gamesounds == True:
        row_5 = font.render("Sound: ON",0,yellow)
    else:
        row_5 = font.render("Sound: OFF",0,yellow)
    gamescreen.blit(row_1, [short_loc_x,short_loc_y])
    gamescreen.blit(row_2, [short_loc_x,short_loc_y+30])
    gamescreen.blit(row_3, [short_loc_x,short_loc_y+85])
    gamescreen.blit(row_4, [short_loc_x,short_loc_y+115])
    gamescreen.blit(row_5, [short_loc_x,short_loc_y+170])

# Joonistab ekraanile vihjeala
def reset_hints():
    gamescreen.blit(hint_card,(hint_loc_x,hint_loc_y))
    create_hints()

# Kogub vihjed ühele võimalikest settidest, võimalusel võtab ette järgmise seti (hint_counter_sets)
def create_hints():
    sets_on_table = []
    for i in cards_on_table:
        sets_on_table.append(card_repr(i))
    try:
        hint_list = list(find_sets(sets_on_table))[hint_counter_sets]
    except:
        try:
            hint_list = list(find_sets(sets_on_table))[0]
        except:
            return
    hint_dict = {}
    for attribute in range(4):
        value = 0
        for card in hint_list:
            value += card[attribute]**2
        hint_dict[attribute] = value
    ret_list = []
    for i in range(4):
        if hint_dict[i] == 5:
            ret_list.append((hint_col_0,eval("hint_row_"+str(i)),"hint_card_select_3"))
        if hint_dict[i] == 0:
            ret_list.append((hint_col_0,eval("hint_row_"+str(i)),"hint_card_select_1"))
        if hint_dict[i] == 3:
            ret_list.append((hint_col_1,eval("hint_row_"+str(i)),"hint_card_select_1"))
        if hint_dict[i] == 12:
            ret_list.append((hint_col_2,eval("hint_row_"+str(i)),"hint_card_select_1"))
    return ret_list

# Märgistab vihjekaardil vihjed, klaviatuurilt 'H' või paremklõps hiirega
def paint_hint():
    gamescreen.blit(eval(hints[hint_counter][2]),(hints[hint_counter][0],hints[hint_counter][1]))

# Manuaalne kaartide segamine, klaviatuurilt 'R'
def reset_table_state_manual(amount=12):
    sets_number_to_screen()
    text_loc_x = table_frame_width+card_width*2+card_spacing*2
    text_loc_y = table_frame_height+card_height*1.5+card_spacing
    pygame.draw.rect(gamescreen,green,(card_area)) # Joonistab üle mänguvälja
    message = font.render("RESHUFFLING.",0,red)
    gamescreen.blit(message, (text_loc_x-96,text_loc_y-60))
    pygame.display.update()
    pygame.draw.rect(gamescreen,green,(card_area)) # Joonistab üle mänguvälja
    global cards_on_table
    for i in range(len(cards_on_table)-1,-1,-1):
        c = gamedeck.append(card_repr(cards_on_table[i]))
    if(draw_new_deck(amount)):
        return True
    global on_table_selected
    for i in range(12):
        gamescreen.blit(deselected_card,card_pos(i))
    on_table_selected = []

# Manuaalne mängu lõpetamine, klaviatuurilt 'Q'
def game_over_manual():
    pygame.draw.rect(gamescreen,white,(card_area)) # Joonistab üle mänguvälja
    text_loc_x = table_frame_width+card_width*2+card_spacing*2
    text_loc_y = table_frame_height+card_height*1.5+card_spacing
    message_1 = font.render("GAME OVER!",0,red)
    message_2 = font.render("YOUR FINAL SCORE: "+str(score).rjust(6,"0"),0,green)
    gamescreen.blit(message_1, (text_loc_x-80,text_loc_y-80))
    gamescreen.blit(message_2, (text_loc_x-192,text_loc_y))
    pygame.display.update()
    input()
##    sleep(5)
    pygame.quit()
##    exec(open("pygame_set.py").read())
##    os.system("python pygame_set.py")
    quit()

# Käivitame mängu Pygame'is
pygame.init()

gamedeck = fulldeck[:]
shuffle(gamedeck)

gamescreen = pygame.display.set_mode((display_width, display_height)) # Akna suurus
gamescreen.fill(green) # Roheline laud
pygame.display.set_caption("Set (created by Lõhmus & Lään)") # Tiitliribale tekst
font = pygame.font.Font("FSEX300.ttf", 32) # Downloaded from http://www.fixedsysexcelsior.com/

clock = pygame.time.Clock()
score = 0
bonus = 999
penalty = 0

gamesounds = True # Kas mäng esitab helisid, klaviatuurilt 'S'; .ogg on Pygame'i puhul sobivaim formaat
welcome = pygame.mixer.Sound('Sounds//Welcome.ogg') # Employing the voice talents from http://onlinetonegenerator.com/voice-generator.html
success = pygame.mixer.Sound('Sounds//Success.ogg') # Set'i leidmise korral
wontwork = pygame.mixer.Sound('Sounds//WontWork.ogg') # Valesti valitud kaartide korral
drawcards = pygame.mixer.Sound('Sounds//DrawCards.ogg') # Reshuffle'i ajal.

if gamesounds == True:
    welcome.play()

# Joonistame kõik vajaliku mänguväljale
draw_new_deck() # Lahtised kaardid
sets_number_to_screen() # Leiduvate settide hulk
deck_on_table() # Avamata kaardid
score_display() # Punktid
bonus_display() # Boonus
shortcut_display() # Klahvikombinatsioonid

start_time = time()
hint_counter = 0
hint_counter_sets = 0
reset_hints()
hints = create_hints()


# Gameloop
while not closed:
    if bonus > 0:
        bonus -= clock.tick(30)/50
        bonus_display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            screen_click(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] or event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            penalty += 50
            penalty_display()
            if hint_counter < 4:
                paint_hint()
                hint_counter += 1
            else:
                reset_hints()
                hints = create_hints()
                hint_counter = 0
                if hint_counter_sets < sets_available()-1:
                    hint_counter_sets += 1
                else:
                    hint_counter_sets = 0
                paint_hint()
                hint_counter += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            gamesounds = abs(gamesounds - 1)
            shortcut_display()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_table_state_manual()
            sleep(0.6) # Vajalik, et reset_table_state ei jookseks kokku
            if gamesounds == True:
                drawcards.play()
                sleep(0.6)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            game_over_manual()
        if False:
            # not needed currently
            print(event)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()