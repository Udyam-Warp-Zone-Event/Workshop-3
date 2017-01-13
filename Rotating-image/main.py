import pygame
import os
from math import *
from pygame import *

pygame.init()

scr_size = (width, height) = (900, 600)
FPS = 25
black = (0,0,0)

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()

def load_image(
    name,
    sizex=-1,
    sizey=-1,
    colorkey=None,
    ):

    fullname = os.path.join('Sprites', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self,x,y,sizex,sizey):
        self.image,self.rect = load_image('fighter1_scale.png',80,80,-1)
        self.orig_image,self.orig_rect = load_image('fighter1_scale.png',80,80,-1)
        self.rect.centerx = x
        self.rect.centery = y
        self.centerx = x
        self.centery = y
        self.rotate = 0
        self.angle = 0
        self.movement = [0,0]
        self.boosters = False
        self.speed = 10

    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self):
        if self.rotate != 0:
            if self.rotate == 1:
                self.angle = self.angle - 10

            if self.rotate == -1:
                self.angle = self.angle + 10

            if self.angle > 359 or self.angle < -359:
                self.angle = 0

            self.image = pygame.transform.rotozoom(self.orig_image,self.angle,1)
            self.centerx = self.rect.centerx
            self.centery = self.rect.centery
            self.rect = self.image.get_rect()
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery
        else:
            pass

        if self.boosters == True:
            self.movement = [-1*self.speed*sin(radians(self.angle)),-1*self.speed*cos(radians(self.angle))]
        else:
            self.movement = [0,0]

        self.rect = self.rect.move(self.movement)

def main():
    gameOver = False
    myShip = PlayerShip(width/2,height/2,197,174)

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    myShip.rotate = -1

                if event.key == pygame.K_RIGHT:
                    myShip.rotate = 1

                if event.key == pygame.K_UP:
                    myShip.boosters = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    myShip.rotate = 0

                if event.key == pygame.K_UP:
                    myShip.boosters = False

        myShip.update()

        screen.fill(black)
        myShip.draw()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

main()
