from random import randint
from random import shuffle
from time import time
import pygame # http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
from global_vars import *
from set_card_data import *
from set_game_logic import *

# joonistab kaardi ekraanile
def card_on_table(card,location):
    # print(card)
    global cards_on_table
    cards_on_table.append(card)

    gamescreen.blit(eval("card_"+card),location)

# joonistab järelejäänud kaartidest koosneva kaardipaki
def deck_on_table():
    location_x = table_frame_width+card_width*4+card_spacing*4
    location_y = table_frame_height
    for card in range((81-12)//6):
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
    this_card = card_repr(cards_on_table[((position[0])//156)+4*(position[1])//226])
    if this_card in on_table_selected:
        # card_on_table(deselected_card,position)
        gamescreen.blit(deselected_card,position)
        on_table_selected.remove(this_card)
    else:
        if len(on_table_selected) > 2:
            print("3 kaarti on juba valitud. Seda ei tohiks tegelikult vist juhtuda.")
            return
        gamescreen.blit(selected_card,position)
        on_table_selected.append(this_card)
    print("Selected",on_table_selected)
    print("Laual",cards_on_table)
    if(find_sets(on_table_selected)):
        print("Sets in selection:",find_sets(on_table_selected))
        # augud täita


pygame.init()

gamescreen = pygame.display.set_mode((display_width, display_height)) # Akna suurus
gamescreen.fill((0, 128, 0)) # Roheline laud
pygame.display.set_caption("Set") # Tiitliribale tekst
gamesounds = False # Kas mäng esitab helisid
welcome = pygame.mixer.Sound('Sounds//Welcome.ogg') # Ogg on Pygame'i puhul sobivaim formaat

clock = pygame.time.Clock()

if gamesounds == True:
    welcome.play()

card_on_table("0000",card0_loc)
card_on_table("0200",card1_loc)
card_on_table("1000",card2_loc)
card_on_table("0010",card3_loc)
card_on_table("2000",card4_loc)
card_on_table("0110",card5_loc)
card_on_table("1111",card6_loc)
card_on_table("0020",card7_loc)
card_on_table("0011",card8_loc)
card_on_table("0220",card9_loc)
card_on_table("2100",card10_loc)
card_on_table("0222",card11_loc)



while not closed:
    deck_on_table()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen_click(event.pos)
        if event.type != 4:
            # avoid printing mousemove events
            print(event)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()