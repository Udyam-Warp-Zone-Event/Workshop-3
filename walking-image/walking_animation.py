import os
import pygame
from pygame import *

pygame.init()
scr_size = (width,height) = (600,400)
FPS = 20
clock = pygame.time.Clock()
screen = pygame.display.set_mode(scr_size)
pygame.display.set_caption('Walking Animation')
black = (0,0,0)

def load_sprite_sheet(
        sheetname,
        x = -1,
        y = -1,
        sizex = -1,
        sizey = -1,
        scalex = -1,
        scaley = -1,
        colorkey = None,
        ):
    fullname = os.path.join('sprites',sheetname)
    sheet = pygame.image.load(fullname)
    sheet = sheet.convert()

    if x!=-1 or y!=-1 or sizex!=-1 or sizey!=-1:
        rect = pygame.Rect((x,y,sizex,sizey))
        image = pygame.Surface(rect.size)
        image = image.convert()

    else:
        image = sheet

    image.blit(sheet,(0,0),rect)
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)

    if scalex != -1 or scaley != -1:
        image = pygame.transform.scale(image,(scalex,scaley))

    return (image,image.get_rect())

class Guy(pygame.sprite.Sprite):
    def __init__(self):
        self.images = []
        for i in range(0,1472,184):
            self.image,self.rect = load_sprite_sheet('walking_guy.png',i,0,184,325,-1,-1,-1)
            self.images.append(self.image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect.top = 20
        self.rect.left = 10

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.rect.left += 10
        if self.rect.left > width:
            self.rect.left = -self.rect.width

    def draw(self):
        screen.blit(self.image,self.rect)

def main():
    guy = Guy()
    counter = 0
    Frame_delay = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        guy.draw()

        if counter % Frame_delay == 0:
            guy.update()

        counter += 1

        pygame.display.update()
        clock.tick(FPS)

main()
