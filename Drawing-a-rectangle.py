#importing pygame module
import pygame
from pygame import * #importing everything else from pygame like constants, classes, etc

pygame.init() #initializing pygame

scr_size = (width,height) = (600,400) #setting a sceen size
FPS = 20 #setting the number of frames per second or FPS
black = (0,0,0) #defining color constants in RGB format
red = (255,0,0)

screen = pygame.display.set_mode(scr_size) #creating a screen object using pygame.display class
clock = pygame.time.Clock() #creating a clock object, used to provide delay to the objects

def main(): # our main function
    gameOver = False #making game over condition to be False
    myRectangle = pygame.Surface((100,50)) #creating an empty rectangular surface with width 100 pixels and height 50 pixels
    myRectangle_rect = myRectangle.get_rect() #gathering the rect coordinates of our rectangle

    myRectangle_rect.left = 150 #defining the position of leftmost corner of our rectangle on the screen in pixels
    myRectangle_rect.top = 130 #defining the position of topmost corner of our rectangle on the screen in pixels

    myRectangle.fill(red) #filling our rectangle with red color!

    while not gameOver: #running our game loop
        for event in pygame.event.get(): #getting all the events like keypress, mouse movement,etc using pygame.event.get()
            if event.type == pygame.QUIT: #if close button(X) is pressed, then quit the program
                quit()

        screen.fill(black) #filling the entire screen with black so that to erase everything and redraw them later on
        screen.blit(myRectangle,myRectangle_rect) #blitting or pasting our rectangle on the screen using its rect coordinates

        pygame.display.update() #updating the display for any changes on the screen
        clock.tick(FPS) #providing a delay of 1/FPS seconds

    pygame.quit() #quitting from pygame
    quit() #quitting the program

main() #running our main function
