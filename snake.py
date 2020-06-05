import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    x_snake = 100
    y_snake = 100
    mode= ''
    count = 0
    points = 0
    radius = 10
    width =640
    height = 480
    x_pos = random.randint(1, width-1)
    y_pos = random.randint(1, height-1)
    screen.fill((0, 0, 0))

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_w:
                    mode = 'up'
                elif event.key == pygame.K_s:
                    mode = 'down'
                elif event.key == pygame.K_d:
                    mode = 'right'
                elif event.key == pygame.K_a:
                    mode = 'left'
        #screen.set_at((x_snake, y_snake), (0, 255, 255))
        #screen.set_at((x_pos, y_pos), (255, 0, 0))
        color_snake = (0,255,255)
        color_pos = (255,0,0)   
        pygame.draw.circle(screen, color_snake, (x_snake, y_snake), radius)
        pygame.draw.circle(screen, color_pos, (x_pos, y_pos), radius)
        
        x_snake ,y_snake = snakeControl(screen,x_snake,y_snake,mode,count,color_snake,color_pos,radius)

        if x_pos-10<= x_snake <=x_pos+10:
            if y_pos-10<= y_snake <=y_pos+10:
                points=points+1
                print(" Points: {} ".format(points))
                pygame.draw.circle(screen, (0,0,0), (x_pos, y_pos), radius)
                x_pos = random.randint(50, width-50)
                y_pos = random.randint(50, height-50)
                

        pygame.display.flip()
        
        clock.tick(60)

def snakeControl(screen,x_snake,y_snake,mode,count,color_snake,color_pos,radius):

    color =(0,0,0)

    if mode == 'up':
        if y_snake < 0:
            print("Out of constrain")
            count = count +1 
        else:    
            pygame.draw.circle(screen, color, (x_snake, y_snake), radius)
            y_snake= y_snake -3
            pygame.draw.circle(screen, color_snake, (x_snake, y_snake), radius)
    elif mode == 'down':
        if y_snake > 480:
            print("Out of constrain")
            count = count +1                 
        else:
            pygame.draw.circle(screen, color, (x_snake, y_snake), radius)
            y_snake= y_snake +3
            pygame.draw.circle(screen, color_snake, (x_snake, y_snake), radius)
    elif mode == 'right':
        if x_snake > 640:
            print("Out of constrain")
            count = count +1
        else:                 
            pygame.draw.circle(screen, color, (x_snake, y_snake), radius)
            x_snake= x_snake +3
            pygame.draw.circle(screen, color_snake, (x_snake, y_snake), radius)
    elif mode == 'left':
        if x_snake < 0:
            print("Out of constrain")
            count = count +1 
        else:       
            pygame.draw.circle(screen, color, (x_snake, y_snake), radius)
            x_snake= x_snake -3
            pygame.draw.circle(screen, color_snake, (x_snake, y_snake), radius)       

    return x_snake , y_snake





main()
