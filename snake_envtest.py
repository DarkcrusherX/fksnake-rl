import pygame
from snake_rl import snakeconnection



control = snakeconnection()
pygame.init()
mode = ''

while True:
        
    pressed = pygame.key.get_pressed()
        
        
    for event in pygame.event.get():
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mode = 'up'
                snakeconnection.main(mode,0)
            elif event.key == pygame.K_s:
                mode = 'down'
                snakeconnection.main(mode,0)    
            elif event.key == pygame.K_d:
                mode = 'right'
                snakeconnection.main(mode,0)    
            elif event.key == pygame.K_a:
                mode = 'left'
                snakeconnection.main(mode,0)    


