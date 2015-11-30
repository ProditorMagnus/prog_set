import pygame # http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame

# joonistab kaardi ekraanile
def card_on_table(card,location):
    gamescreen.blit(card,location)

# joonistab järelejäänud kaartidest koosneva kaardipaki
def deck_on_table():
    location_x = table_frame_width+card_width*4+card_spacing*4
    location_y = table_frame_height
    for card in range((81-12)//6):
        card_on_table(deck_card,(location_x,location_y))
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
    if position in on_table_selected:
        card_on_table(deselected_card,position)
        on_table_selected.remove(position)
    else:
        card_on_table(selected_card,position)
        on_table_selected.append(position)

pygame.init()
display_width = 1024
display_height = 768
gamescreen = pygame.display.set_mode((display_width, display_height)) # Akna suurus
gamescreen.fill((0, 128, 0)) # Roheline laud
pygame.display.set_caption("Set") # Tiitliribale tekst

clock = pygame.time.Clock()

# Kaartide pildifailide suurused
card_width = 151
card_height = 221

# Kaartide paigutuse määratlus ja asukohad laual
card_spacing = 5
table_frame_width = 20
table_frame_height = 50

card0_loc = (table_frame_width,table_frame_height)
card1_loc = (table_frame_width+card_spacing+card_width,table_frame_height)
card2_loc = (table_frame_width+card_spacing*2+card_width*2,table_frame_height)
card3_loc = (table_frame_width+card_spacing*3+card_width*3,table_frame_height)
card4_loc = (table_frame_width,table_frame_height+card_spacing+card_height)
card5_loc = (table_frame_width+card_spacing+card_width,table_frame_height+card_spacing+card_height)
card6_loc = (table_frame_width+card_spacing*2+card_width*2,table_frame_height+card_spacing+card_height)
card7_loc = (table_frame_width+card_spacing*3+card_width*3,table_frame_height+card_spacing+card_height)
card8_loc = (table_frame_width,table_frame_height+card_spacing*2+card_height*2)
card9_loc = (table_frame_width+card_spacing+card_width,table_frame_height+card_spacing*2+card_height*2)
card10_loc = (table_frame_width+card_spacing*2+card_width*2,table_frame_height+card_spacing*2+card_height*2)
card11_loc = (table_frame_width+card_spacing*3+card_width*3,table_frame_height+card_spacing*2+card_height*2)

# Pygame toetab graafikal alpha-kanalit (transparency), kõik kaardid kasutavad seda
# Kaardifailid 151*221 pikslit, igas servas 10 pikslit transparency't, mida kasutab ära 'selected_card.png'
# Laeme kaardid
card_0000 = pygame.image.load('Cards//0000.png')
card_0010 = pygame.image.load('Cards//0010.png')
card_0020 = pygame.image.load('Cards//0020.png')
card_0100 = pygame.image.load('Cards//0100.png')
card_0110 = pygame.image.load('Cards//0110.png')
card_0120 = pygame.image.load('Cards//0120.png')
card_0200 = pygame.image.load('Cards//0200.png')
card_0210 = pygame.image.load('Cards//0210.png')
card_0220 = pygame.image.load('Cards//0220.png')
card_0001 = pygame.image.load('Cards//0001.png')
card_0011 = pygame.image.load('Cards//0011.png')
card_0021 = pygame.image.load('Cards//0021.png')
card_0101 = pygame.image.load('Cards//0101.png')
card_0111 = pygame.image.load('Cards//0111.png')
card_0121 = pygame.image.load('Cards//0121.png')
card_0201 = pygame.image.load('Cards//0201.png')
card_0211 = pygame.image.load('Cards//0211.png')
card_0221 = pygame.image.load('Cards//0221.png')
card_0002 = pygame.image.load('Cards//0002.png')
card_0012 = pygame.image.load('Cards//0012.png')
card_0022 = pygame.image.load('Cards//0022.png')
card_0102 = pygame.image.load('Cards//0102.png')
card_0112 = pygame.image.load('Cards//0112.png')
card_0122 = pygame.image.load('Cards//0122.png')
card_0202 = pygame.image.load('Cards//0202.png')
card_0212 = pygame.image.load('Cards//0212.png')
card_0222 = pygame.image.load('Cards//0222.png')
card_1000 = pygame.image.load('Cards//1000.png')
card_1010 = pygame.image.load('Cards//1010.png')
card_1020 = pygame.image.load('Cards//1020.png')
card_1100 = pygame.image.load('Cards//1100.png')
card_1110 = pygame.image.load('Cards//1110.png')
card_1120 = pygame.image.load('Cards//1120.png')
card_1200 = pygame.image.load('Cards//1200.png')
card_1210 = pygame.image.load('Cards//1210.png')
card_1220 = pygame.image.load('Cards//1220.png')
card_1001 = pygame.image.load('Cards//1001.png')
card_1011 = pygame.image.load('Cards//1011.png')
card_1021 = pygame.image.load('Cards//1021.png')
card_1101 = pygame.image.load('Cards//1101.png')
card_1111 = pygame.image.load('Cards//1111.png')
card_1121 = pygame.image.load('Cards//1121.png')
card_1201 = pygame.image.load('Cards//1201.png')
card_1211 = pygame.image.load('Cards//1211.png')
card_1221 = pygame.image.load('Cards//1221.png')
card_1002 = pygame.image.load('Cards//1002.png')
card_1012 = pygame.image.load('Cards//1012.png')
card_1022 = pygame.image.load('Cards//1022.png')
card_1102 = pygame.image.load('Cards//1102.png')
card_1112 = pygame.image.load('Cards//1112.png')
card_1122 = pygame.image.load('Cards//1122.png')
card_1202 = pygame.image.load('Cards//1202.png')
card_1212 = pygame.image.load('Cards//1212.png')
card_1222 = pygame.image.load('Cards//1222.png')
card_2000 = pygame.image.load('Cards//2000.png')
card_2010 = pygame.image.load('Cards//2010.png')
card_2020 = pygame.image.load('Cards//2020.png')
card_2100 = pygame.image.load('Cards//2100.png')
card_2110 = pygame.image.load('Cards//2110.png')
card_2120 = pygame.image.load('Cards//2120.png')
card_2200 = pygame.image.load('Cards//2200.png')
card_2210 = pygame.image.load('Cards//2210.png')
card_2220 = pygame.image.load('Cards//2220.png')
card_2001 = pygame.image.load('Cards//2001.png')
card_2011 = pygame.image.load('Cards//2011.png')
card_2021 = pygame.image.load('Cards//2021.png')
card_2101 = pygame.image.load('Cards//2101.png')
card_2111 = pygame.image.load('Cards//2111.png')
card_2121 = pygame.image.load('Cards//2121.png')
card_2201 = pygame.image.load('Cards//2201.png')
card_2211 = pygame.image.load('Cards//2211.png')
card_2221 = pygame.image.load('Cards//2221.png')
card_2002 = pygame.image.load('Cards//2002.png')
card_2012 = pygame.image.load('Cards//2012.png')
card_2022 = pygame.image.load('Cards//2022.png')
card_2102 = pygame.image.load('Cards//2102.png')
card_2112 = pygame.image.load('Cards//2112.png')
card_2122 = pygame.image.load('Cards//2122.png')
card_2202 = pygame.image.load('Cards//2202.png')
card_2212 = pygame.image.load('Cards//2212.png')
card_2222 = pygame.image.load('Cards//2222.png')
selected_card = pygame.image.load('Cards//selected_card.png')
deselected_card = pygame.image.load('Cards//deselected_card.png')
deck_card = pygame.image.load('Cards//deck_card.png')

card_on_table(card_0000,card0_loc)
card_on_table(card_0200,card1_loc)
card_on_table(card_1000,card2_loc)
card_on_table(card_0010,card3_loc)
card_on_table(card_2000,card4_loc)
card_on_table(card_0110,card5_loc)
card_on_table(card_1111,card6_loc)
card_on_table(card_0020,card7_loc)
card_on_table(card_0011,card8_loc)
card_on_table(card_0220,card9_loc)
card_on_table(card_2100,card10_loc)
card_on_table(card_0222,card11_loc)

# selekteeritud kaardid
on_table_selected = []

closed = False

while not closed:
    deck_on_table()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen_click(event.pos)
        print(event)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()