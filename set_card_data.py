import pygame

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

card_xxxx = pygame.image.load('Cards//xxxx.png')

selected_card = pygame.image.load('Cards//selected_card.png')
deselected_card = pygame.image.load('Cards//deselected_card.png')
deck_card = pygame.image.load('Cards//deck_card.png')

# Kaartide pildifailide suurused
card_width = 151
card_height = 221

# Kaartide paigutuse määratlus ja asukohad laual
card_spacing = 5
table_frame_width = 20
table_frame_height = 50
card_area = (table_frame_width,table_frame_height,card_width*4+card_spacing*3,card_height*3+card_spacing*2)

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

# Vihjekaart ja märgistus
hint_card = pygame.image.load('Cards//hint_card.png')
hint_card_select_1 = pygame.image.load('Cards//hint_card_select_1.png')
hint_card_select_3 = pygame.image.load('Cards//hint_card_select_3.png')

# Vihjekaardi ja märgistuse paigutus
hint_loc_x = table_frame_width+card_width*4+card_spacing*4
hint_loc_y = table_frame_height+card_height+card_spacing

hint_row_0 = hint_loc_y+5
hint_row_1 = hint_loc_y+58
hint_row_2 = hint_loc_y+110
hint_row_3 = hint_loc_y+162
hint_col_0 = hint_loc_x
hint_col_1 = hint_loc_x+48
hint_col_2 = hint_loc_x+96
