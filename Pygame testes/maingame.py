import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Corredor")
clock = pygame.time.Clock()
test_font = pygame.font.Font('C:/Users/u23623/Documents/GitHub/Python-and-HTLM/python/Pygame testes/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('C:/Users/u23623/Documents/GitHub/Python-and-HTLM/python/Pygame testes/graphics/Sky.png').convert()
ground_surface = pygame.image.load('C:/Users/u23623/Documents/GitHub/Python-and-HTLM/python/Pygame testes/graphics/ground.png').convert()
text_surface = test_font.render('Meu Jogo', False, 'Black')

snail_surface = pygame.image.load('C:/Users/u23623/Documents/GitHub/Python-and-HTLM/python/Pygame testes/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surface = pygame.image.load('C:/Users/u23623/Documents/GitHub/Python-and-HTLM/python/Pygame testes/graphics/Player/player_walk_1.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 4
    if snail_x_pos < -100: 
        snail_x_pos = 800     
    screen.blit(snail_surface,(snail_x_pos,250))
    screen.blit(player_surface,(80,200))

    pygame.display.update()
    clock.tick(60)