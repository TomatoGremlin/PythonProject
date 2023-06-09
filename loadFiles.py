import pygame
from pygame import mixer
from globalVars import TILE_SIZE, SCREEN_WIDTH , SCREEN_HEIGHT
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

#IMAGES
bg_img = pygame.transform.scale(pygame.image.load('assets/sky.png') , (SCREEN_WIDTH, SCREEN_HEIGHT))

dirt_img = pygame.transform.scale( pygame.image.load('assets/dirt.png'), (TILE_SIZE, TILE_SIZE) )
grass_img = pygame.transform.scale( pygame.image.load('assets/grass.png'), (TILE_SIZE, TILE_SIZE) )
cave_img = pygame.transform.scale( pygame.image.load('assets/cave.png'), (TILE_SIZE, TILE_SIZE) )

obstacle_image =  pygame.transform.scale ( pygame.image.load('assets/crystal.png'), (TILE_SIZE , TILE_SIZE ) )
platform_img = pygame.transform.scale( pygame.image.load('assets/platform.png'), (TILE_SIZE, TILE_SIZE // 2) )
lava_img = pygame.transform.scale( pygame.image.load('assets/lava.png'), (TILE_SIZE, TILE_SIZE // 2) )
lava2_img = pygame.transform.scale( pygame.image.load('assets/lava2.png'), (TILE_SIZE, TILE_SIZE) )

fish_img = pygame.transform.scale ( pygame.image.load('assets/fish.png'), (TILE_SIZE // 1.5, TILE_SIZE // 1.5) )
exit_level_img = pygame.transform.scale ( pygame.image.load('assets/exit.png'), (TILE_SIZE, int(TILE_SIZE * 1.5))  )

ghost_img = pygame.transform.scale( pygame.image.load('assets/ghost.png'), (40,40) )


# heart
heart_scale = 30       

full_img = pygame.transform.scale( pygame.image.load('assets/heart_full.png'), (heart_scale + 5, heart_scale  ) )  
half_img = pygame.transform.scale(pygame.image.load('assets/heart_half.png'), (heart_scale + 5, heart_scale))
empty_img = pygame.transform.scale( pygame.image.load('assets/heart_empty.png'), (heart_scale + 5, heart_scale) )


# buttons
start_img = pygame.transform.scale(pygame.image.load('assets/start_btn.png') , (120, TILE_SIZE))
exit_img = pygame.transform.scale(pygame.image.load('assets/exit_btn.png') , (150, TILE_SIZE)) 
restart_img = pygame.transform.scale(pygame.image.load('assets/restart_btn.png') , (150, TILE_SIZE))
go_img = pygame.transform.scale(pygame.image.load('assets/go_btn.png') , ( TILE_SIZE+20 , TILE_SIZE - 20 ))
music_on_img = pygame.transform.scale(pygame.image.load('assets/musicOn.png') , (TILE_SIZE - 20, TILE_SIZE - 20))
music_off_img = pygame.transform.scale(pygame.image.load('assets/musicOff.png') , (TILE_SIZE - 20, TILE_SIZE - 20))



#SOUNDS
volume = 0.2

pygame.mixer.music.load('assets/music/background/my-little-garden-of-eden-112845.mp3')
pygame.mixer.music.set_volume( volume - 0.1 )
pygame.mixer.music.play(-1, 0.0, 5000)
fish_fx = pygame.mixer.Sound('assets/music/reward.mp3')
fish_fx.set_volume(volume)
jump_fx = pygame.mixer.Sound('assets/music/jump.mp3')
jump_fx.set_volume(volume - 0.1)
game_over_fx = pygame.mixer.Sound('assets/music/beefmow.mp3')
game_over_fx.set_volume(volume)
victory_fx =  pygame.mixer.Sound('assets/music/winsquare-6993.mp3')
victory_fx.set_volume(volume)
click_fx = pygame.mixer.Sound('assets/music/mixkit-quick-win-video-game-notification-269.wav')
click_fx.set_volume(volume/2)
