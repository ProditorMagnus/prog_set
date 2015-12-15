from random import randint
from random import shuffle
from time import time, sleep
import pygame # http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
from global_vars import *
from set_card_data import *
from set_game_logic import *

gamedeck = fulldeck[:]
shuffle(gamedeck)



def draw_new_deck(amount=12,recursion=0):
    if(recursion>50):
        print("50 iterations say no more sets left")
        input()
    global cards_on_table
    cards_on_table = []
    for i in range(amount):
        try:
            card_on_table(card_str(gamedeck[0]),card_pos(i))
        except:
            print("no more deck, end game")
            amount-=3
    if no_set_on_table():
        shuffle(gamedeck)
        draw_new_deck(amount,recursion+1)


def reset_table_state(amount=12):
    # siis kui ei leidu set
    # Ekraanile 2.2-ks sekundiks tekst, et kaardid segatakse uuesti
    sets_number_to_screen()
    pygame.draw.rect(gamescreen,green,(card_area)) # Joonistab üle mänguvälja
    message = font.render("NO AVAILABLE SETS. RESHUFFLING.",0,yellow)
    gamescreen.blit(message, [table_frame_width+card_width*0.5+card_spacing,table_frame_height+card_height*1.5+card_spacing])
    pygame.display.update()
    sleep(1)
    pygame.draw.rect(gamescreen,green,(card_area)) # Joonistab üle mänguvälja

    global cards_on_table
    for i in range(len(cards_on_table)-1,-1,-1):
        c = gamedeck.append(card_repr(cards_on_table[i]))
    
    draw_new_deck(amount)
    
    global on_table_selected
    for i in range(12):
        gamescreen.blit(deselected_card,card_pos(i))
    on_table_selected = []

def no_set_on_table():
    card_tuples_on_table=[]
    for i in cards_on_table:
        card_tuples_on_table.append(card_repr(i))
    print("sets on table",find_sets(card_tuples_on_table))
    return find_sets(card_tuples_on_table)==set()
        
# joonistab kaardi ekraanile
def card_on_table(card,location):
    print(card_repr(card))
    # pole vist vaja et oleks global, kui kasutada muteerumist mitte omistamist
    # global cards_on_table
    # pakist ära võtta need mis lauale panna
    # print(gamedeck)
    gamedeck.remove(card_repr(card))
    print("adding",card)
    cards_on_table.append(card) # append paneb uued kaardid valele kohale

    # card_tuples_on_table=[]
    # for i in cards_on_table:
        # card_tuples_on_table.append(card_repr(i))
    # print("sets on table",find_sets(card_tuples_on_table))

    gamescreen.blit(eval("card_"+card),location)
    
def card_to_table(card,index):
    gamedeck.remove(card_repr(card))
    print("adding1",card,index)
    cards_on_table.insert(index,card)
    
    # card_tuples_on_table=[]
    # for i in cards_on_table:
        # card_tuples_on_table.append(card_repr(i))
    # print("sets on table",find_sets(card_tuples_on_table))
    # siin on veel vara kontrollida, eelmist pole veel eemaldatud
    
    gamescreen.blit(eval("card_"+card),card_pos(index))

# joonistab järelejäänud kaartidest koosneva kaardipaki
def deck_on_table():
    location_x = table_frame_width+card_width*4+card_spacing*4
    location_y = table_frame_height
    pygame.draw.rect(gamescreen,green,(location_x,location_y-14,card_width+14,card_height+14))
    for card in range((len(gamedeck)+3)//6):
        # +3 abil see näitab kui pakk on tühi õigel ajal
        # see on erinev tavalistest kaartidest
        gamescreen.blit(deck_card,(location_x,location_y))
        location_x += 2
        location_y -= 2

# reageerib klikile mänguväljal
def screen_click(position):
    x = position[0]
    y = position[1]
    if x > card0_loc[0] and y > card0_loc[1] and x < card11_loc[0]+150 and y < card11_loc[1]+220:
        click_card(position)

# reageerib klikile kaardiväljal, selekteerib kaardi
def click_card(position):
    x = position[0]
    y = position[1]
    if x > card0_loc[0] and x < card0_loc[0]+150:
        if y > card0_loc[1] and y < card0_loc[1]+220:
            select_card(card0_loc)
        if y > card4_loc[1] and y < card4_loc[1]+220:
            select_card(card4_loc)
        if y > card8_loc[1] and y < card8_loc[1]+220:
            select_card(card8_loc)
    if x > card1_loc[0] and x < card1_loc[0]+150:
        if y > card1_loc[1] and y < card1_loc[1]+220:
            select_card(card1_loc)
        if y > card5_loc[1] and y < card5_loc[1]+220:
            select_card(card5_loc)
        if y > card9_loc[1] and y < card9_loc[1]+220:
            select_card(card9_loc)
    if x > card2_loc[0] and x < card2_loc[0]+150:
        if y > card2_loc[1] and y < card2_loc[1]+220:
            select_card(card2_loc)
        if y > card6_loc[1] and y < card6_loc[1]+220:
            select_card(card6_loc)
        if y > card10_loc[1] and y < card10_loc[1]+220:
            select_card(card10_loc)
    if x > card3_loc[0] and x < card3_loc[0]+150:
        if y > card3_loc[1] and y < card3_loc[1]+220:
            select_card(card3_loc)
        if y > card7_loc[1] and y < card7_loc[1]+220:
            select_card(card7_loc)
        if y > card11_loc[1] and y < card11_loc[1]+220:
            select_card(card11_loc)

# kontrollib, kas kaart on selekteeritud või mitte ning vastavalt sellele
# deselekteerib või selekteerib selle
def select_card(position):
    no_set_on_table()
    try:
        this_card = card_repr(cards_on_table[((position[0])//156)+4*(position[1])//226])
    except:
        print("indeksid on vigased, edasi ei saa hetkel - teha game over?")
        return
        # lahendus võiks olla näiteks kontroll, kas cards_on_table on selles kohas None - ning see None panna õigesse kohta
    if this_card in on_table_selected:
        # card_on_table(deselected_card,position)
        gamescreen.blit(deselected_card,position)
        on_table_selected.remove(this_card)
    else:
        if len(on_table_selected) > 2:
            # print("Siin saab öelda, et üle 3 ei või korraga valida. Sobiks lühike ning mitte liiga häiriv heli.") - muutsin nii, et siis lihtsalt eemaldab vanima
            last_card = (on_table_selected[0])
            # print(last_card)
            # deselect this
            gamescreen.blit(deselected_card,card_pos(cards_on_table.index(card_str(last_card))))
            on_table_selected.remove(last_card)
            # return
        gamescreen.blit(selected_card,position)
        on_table_selected.append(this_card)
        if(find_sets(on_table_selected)):
            print("Sets in selection:",find_sets(on_table_selected))
            # augud tekitada
            for i in range(len(on_table_selected)-1,-1,-1):
                print("Removing",cards_on_table.index(card_str(on_table_selected[i])))
                
                gamescreen.blit(tmp_removed_card,card_pos(cards_on_table.index(card_str(on_table_selected[i]))))
                
                if(len(gamedeck)>0):
                    print(gamedeck[0],"added, shape,fill,quantity,color")
                    card_to_table(card_str(gamedeck[0]),(cards_on_table.index(card_str(on_table_selected[i]))))
                else:
                    if sets_available() > 0:
                        reset_last_cards()
                    print("deck is empty, what now !!! see rikub kõik indeksid hetkel ära")
                
                cards_on_table.pop(cards_on_table.index(card_str(on_table_selected[i])))
                on_table_selected.pop()
                if(no_set_on_table()):
                    print("No sets on table")
                    if gamesounds == True:
                        success.play()
                    reset_table_state()
                    sleep(1.2) # Vajalik, et reset_table_state ei jookseks kokku
                    deck_on_table()
                    reset_hints()
                    hints = create_hints()
                    hint_counter = hint_counter_sets = 0
                    print("counter:", hint_counter)
                    return
            # ja augud täita
            sets_number_to_screen()
            deck_on_table()
            reset_hints()
            hints = create_hints()
            hint_counter = hint_counter_sets = 0
            print("counter:", hint_counter)
            if gamesounds == True:
                success.play()
            return
        else:
            if(len(on_table_selected) > 2):
                print("No sets in selection.",on_table_selected) # Siia lisada veateade - tekitan helifaili
                if gamesounds == True:
                    wontwork.play()
                return
    print("Selected",on_table_selected)
    print("Laual",cards_on_table)

# Laob kaardid uuesti ekraanile, veel testimata.
def reset_last_cards():
    global cards_on_table
    pygame.draw.rect(gamescreen,green,(card_area)) # Joonistab üle mänguvälja
    cards = []
    for i in range(len(cards_on_table)):
        cards.append(cards_on_table.pop())
    cards_on_table = cards[:]
    shuffle(cards_on_table)
    for j in range(len(cards_on_table)):
        card_on_table(card_str(cards[0]),card_pos(j))
    

# Joonistab ekraanile laual olevate kaartide hulgas oleva võimalike settide hulga
def sets_available():
    sets_on_table = []
    for i in cards_on_table:
        sets_on_table.append(card_repr(i))
    return len(find_sets(sets_on_table))

def sets_number_to_screen():
    pygame.draw.rect(gamescreen,green,(260,5,35,25)) # Joonistab üle settide hulga, arvestab kahekohalisi arve
    counter = font.render("SETS AVAILABLE: " + str(sets_available()),0,yellow)
    gamescreen.blit(counter, [5,0])

# Joonistab ekraanile vihjeala
def reset_hints():
    gamescreen.blit(hint_card,(hint_loc_x,hint_loc_y))
    print("hints have been reset")
    create_hints()

# Kogub vihjed ühele võimalikest setidest, võimalusel võtab ette järgmise seti (hint_counter_sets)
def create_hints():
    sets_on_table = []
    for i in cards_on_table:
        sets_on_table.append(card_repr(i))
    hint_list = list(find_sets(sets_on_table))[hint_counter_sets]
    print("hint list", hint_list)
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
    print("hints have been created")
    return ret_list

def paint_hint():
    gamescreen.blit(eval(hints[hint_counter][2]),(hints[hint_counter][0],hints[hint_counter][1]))

# Joonistab ekraanile seni kogutud punktide hulga
# Work in progress...
def score_display():
    pygame.draw.rect(gamescreen,green,(260,5,35,25)) # Joonistab üle skoori
    counter = font.render("SCORE: " + str(score).rjust(6,"0"),0,yellow)
    gamescreen.blit(counter, [5,0])

pygame.init()

yellow = (200,200,0) # Teksti värv
green = (0,128,0) # Mängulaua värv
gamescreen = pygame.display.set_mode((display_width, display_height)) # Akna suurus
gamescreen.fill(green) # Roheline laud
card_area = (table_frame_width,table_frame_height,card_width*4+card_spacing*3,card_height*3+card_spacing*2)
pygame.display.set_caption("Set") # Tiitliribale tekst
font = pygame.font.Font("FSEX300.ttf", 32) # Downloaded from http://www.fixedsysexcelsior.com/

gamesounds = True # Kas mäng esitab helisid; .ogg on Pygame'i puhul sobivaim formaat
welcome = pygame.mixer.Sound('Sounds//Welcome.ogg') # Employing the voice talents from http://onlinetonegenerator.com/voice-generator.html
success = pygame.mixer.Sound('Sounds//Success.ogg') # Set'i leidmise korral
wontwork = pygame.mixer.Sound('Sounds//WontWork.ogg') # Valesti valitud kaartide korral
clock = pygame.time.Clock()

# Hint variables
hint_loc_x = table_frame_width+card_width*4+card_spacing*4
hint_loc_y = table_frame_height+card_height+card_spacing
hint_row_0 = hint_loc_y+5
hint_row_1 = hint_loc_y+58
hint_row_2 = hint_loc_y+110
hint_row_3 = hint_loc_y+162
hint_col_0 = hint_loc_x
hint_col_1 = hint_loc_x+48
hint_col_2 = hint_loc_x+96


if gamesounds == True:
    welcome.play()

# selle jaoks ka while not has_set
draw_new_deck()
sets_number_to_screen()
deck_on_table()

hint_counter = 0
hint_counter_sets = 0
reset_hints()
hints = create_hints()

while not closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            screen_click(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] or event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            if hint_counter < 4:
                paint_hint()
                hint_counter += 1
##                print("counter:", hint_counter, "hint counter sets:", hint_counter_sets)
##                print(hints)
            else:
                reset_hints()
                hints = create_hints()
                hint_counter = 0
                if hint_counter_sets < sets_available()-1:
                    hint_counter_sets += 1
                if hint_counter_sets == sets_available()-1:
                    hint_counter_sets = 0
##                print("counter:", hint_counter, "hint counter sets:", hint_counter_sets)
##                print(hints)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            gamesounds = abs(gamesounds - 1)
        if False:
            # not needed currently
            print(event)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()