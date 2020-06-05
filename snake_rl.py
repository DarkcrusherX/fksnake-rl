import pygame
import random


pygame.init()
screen = pygame.display.set_mode((640, 480))
class snakeconnection():

    def __init__(self):
        self.x_snake = 100
        self.y_snake = 100
        self.mode= ''
        self.count = 0
        self.points = 0
        self.x_pos = random.randint(30, 610)
        self.y_pos = random.randint(30, 450)

    def snake(self,mode):
        def snakeControl(self,screen,color_snake,color_pos,radius):

            color =(0,0,0)

            if self.mode == 'up':
                if self.y_snake < 20:
                    #print("Out of constrain")
                    self.count = self.count +1
                else:
                    pygame.draw.circle(screen, color, (self.x_snake, self.y_snake), radius)
                    self.y_snake= self.y_snake -10
                    pygame.draw.circle(screen, color_snake, (self.x_snake, self.y_snake), radius)
            elif self.mode == 'down':
                if self.y_snake > 460:
                    #print("Out of constrain")
                    self.count = self.count +1
                else:
                    pygame.draw.circle(screen, color, (self.x_snake, self.y_snake), radius)
                    self.y_snake= self.y_snake +10
                    pygame.draw.circle(screen, color_snake, (self.x_snake, self.y_snake), radius)
            elif self.mode == 'right':
                if self.x_snake > 620:
                    #print("Out of constrain")
                    self.count = self.count +1
                else:
                    pygame.draw.circle(screen, color, (self.x_snake, self.y_snake), radius)
                    self.x_snake= self.x_snake +10
                    pygame.draw.circle(screen, color_snake, (self.x_snake, self.y_snake), radius)
            elif self.mode == 'left':
                if self.x_snake < 20:
                    #print("Out of constrain")
                    self.count = self.count +1
                else:
                    pygame.draw.circle(screen, color, (self.x_snake, self.y_snake), radius)
                    self.x_snake= self.x_snake -10
                    pygame.draw.circle(screen, color_snake, (self.x_snake, self.y_snake), radius)



        xs = self.x_snake
        ys = self.y_snake
        xp = self.x_pos
        yp = self.y_pos
        self.mode =mode
        clock = pygame.time.Clock()
        pressed = pygame.key.get_pressed()
        screen.fill((0, 0, 0))
        width =610
        height = 450
        radius = 10
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

        color_snake = (0,255,255)
        color_pos = (255,0,0)
        pygame.draw.circle(screen, color_snake, (xs,ys), radius)
        pygame.draw.circle(screen, color_pos, (xp,yp), radius)

        snakeControl(self,screen,color_snake,color_pos,radius)

        if self.x_pos-10<= self.x_snake <=self.x_pos+10:
            if self.y_pos-10<= self.y_snake <=self.y_pos+10:
                self.points=self.points+1
                print(" self.points: {} ".format(self.points))
                pygame.draw.circle(screen, (0,0,0), (self.x_pos, self.y_pos), radius)
                self.x_pos = random.randint(50, width-50)
                self.y_pos = random.randint(50, height-50)


        pygame.display.flip()

        #clock.tick(60)

        return self.x_pos,self.y_pos , self.x_snake,self.y_snake, self.count

    def respawn(self):
        self.x_snake = 100
        self.y_snake = 100
        self.count=0