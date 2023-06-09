import pygame
pygame.init()


GAME_NAME = "Topcho's Bizzare Adventure"

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#define FONT_BIG
FONT_BIG = pygame.font.SysFont('Lucida Sans', 70)
FONT_MID = pygame.font.SysFont('Lucida Sans', 35, True)

FONT_SMALL = pygame.font.SysFont('Lucida Sans', 20, True)


#define game variables
TILE_SIZE = 50
game_over = 0
main_menu = True

level = 1
MAX_LEVELS = 4
LIVES = 3
score = 0
is_music_playing = True
fade_counter = 0

#define colours
WHITE = (255, 255, 255)
BLUE_DARK = (26, 32, 44)
BLUE_LIGHT = (142, 166, 254)
PINK = (234, 110, 161)


