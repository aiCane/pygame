import math
import pygame,sys
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("The Pie Game - Press The Keys")
myfont = pygame.font.Font(None, 100)

list = []
last_name1 = 0
last_name2 = 0
last_name3 = 0
last_name4 = 0
last_name_regame = 0
ticks_regame = 0
text1 = ""
text2 = ""
text3 = ""
text4 = ""

piece1 = False
piece2 = False
piece3 = False
piece4 = False

file = open("key_data", "r")
all_data = file.read()
for i in all_data:
    list.append(i)

count = 0
screen_color = (0,0,200)
color = 200,80,60
width = 4
x = 300
y = 250
radius = 200
position = x-radius, y-radius, radius*2, radius*2

def draw_arc(start_angle, end_angle):
    pygame.draw.arc(screen, color, position, math.radians(start_angle), math.radians(end_angle), width)

def draw_line(start_pos, end_pos):
    pygame.draw.line(screen, color, start_pos, end_pos, width)

def reset_game():
    last_name_regame = ticks_regame
    piece1 = False
    piece2 = False
    piece3 = False
    piece4 = False

reset_game()

class draw_circle:

    def up_right_circle(self):
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)

    def up_left_circle(self):
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)

    def down_left_circle(self):
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)

    def down_right_circle(self):
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)








while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == ord(text1):
                piece1 = True
            elif event.key == ord(text2):
                piece2 = True
            elif event.key == ord(text3):
                piece3 = True
            elif event.key == ord(text4):
                piece4 = True
            else:
                count += 1
                if count > 5:
                    count = 0
                    reset_game()
            ticks_regame = pygame.time.get_ticks()
            if ticks_regame > last_name_regame + 10000:
                reset_game()

    screen.fill(screen_color)

    ticks1 = pygame.time.get_ticks()
    if ticks1 > last_name1 + random.randint(1500, 2000) and not piece1:
        text1 = random.choice(list)
        last_name1 = ticks1
    ticks2 = pygame.time.get_ticks()
    if ticks2 > last_name2 + random.randint(1500, 2000) and not piece2:
        text2 = random.choice(list)
        last_name2 = ticks2
    ticks3 = pygame.time.get_ticks()
    if ticks3 > last_name3 + random.randint(1500, 2000) and not piece3:
        text3 = random.choice(list)
        last_name3 = ticks3
    ticks4 = pygame.time.get_ticks()
    if ticks4 > last_name4 + random.randint(1500, 2000) and not piece4:
        text4 = random.choice(list)
        last_name4 = ticks4


    textImg1 = myfont.render(text1, True, color)
    screen.blit(textImg1, (x+radius/2-20, y-radius/2))
    textImg2 = myfont.render(text2, True, color)
    screen.blit(textImg2, (x-radius/2, y-radius/2))
    textImg3 = myfont.render(text3, True, color)
    screen.blit(textImg3, (x-radius/2, y+radius/2-20))
    textImg4 = myfont.render(text4, True, color)
    screen.blit(textImg4, (x+radius/2-20, y+radius/2-20))


    if piece1:
        draw_circle().up_right_circle()
    if piece2:
        draw_circle().up_left_circle()
    if piece3:
        draw_circle().down_left_circle()
    if piece4:
        draw_circle().down_right_circle()

    if piece1 and piece2 and piece3 and piece4:
        color = 0,255,0

    pygame.display.update()
