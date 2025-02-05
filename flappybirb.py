import pygame 
from pygame.locals import *
import os
pygame.font.init()
pygame.mixer.init()
WIDTH,HEIGHT = 865,935
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("flappy birb")

fps = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont("pacifico", 10)
ground_scroll = 0
scroll_speed = 4
flying = False
pipe_gap = 150
gameover = False
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0 
pass_pipe = False

#images

bg = pygame.image.load("images/background.png")
ground = pygame.image.load("images/platform.png")
restart = pygame.image.load("images/restart.png")

def draw_text(text, font, text_col, x, y):
    ing = font.render(text, True, text_col)
    SCREEN.blit(ing, (x, y))

def reset_game():
    pipe_group.empty()
    birb.rect.x = 100
    birb.rect.y = int(HEIGHT / 2)
    score = 0
    return score
    
