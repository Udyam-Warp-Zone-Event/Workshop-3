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

class Rectangle(): #creating our rectangle class
    def __init__(self,x,y,sizex,sizey,color): #defining the init function which runs while creating our object from the class by passing several parameters like x,y,sizex etc
        self.image = pygame.Surface((sizex,sizey)) #defining our image
        self.rect = self.image.get_rect() #getting the rect coordinates

        self.rect.left = x #setting our left and top coordinates of our rect
        self.rect.top = y

        self.image.fill(color) #filling our rectangle with the desired color
        self.movement = [0,0] #defining the number of pixels our rectangle will move in [x,y] direction

    def draw(self): #defining our draw function
        screen.blit(self.image,self.rect) #drawing our rectangle to the screen

    def update(self): #defining the update function which updates the rect coordinates of our rectangle based on its movement
        self.rect = self.rect.move(self.movement)


def main(): # our main function
    gameOver = False #making game over condition to be False

    myRectangle = Rectangle(150,170,100,50,red) #creating an object from our Rectangle class

    while not gameOver: #running our game loop
        for event in pygame.event.get(): #getting all the events like keypress, mouse movement,etc using pygame.event.get()
            if event.type == pygame.QUIT: #if close button(X) is pressed, then quit the program
                quit()

            if event.type == pygame.KEYDOWN: #if a key is pressed
                if event.key == pygame.K_LEFT: #if left key is pressed
                    myRectangle.movement[0] = -2 #the rectangle will move 2 pixels in x direction
                if event.key == pygame.K_RIGHT: #similarly for right, up and down key presses
                    myRectangle.movement[0] = 2
                if event.key == pygame.K_UP:
                    myRectangle.movement[1] = -2
                if event.key == pygame.K_DOWN:
                    myRectangle.movement[1] = 2

            if event.type == pygame.KEYUP: #if a key is unpressed
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #if either left or right key is lifted
                    myRectangle.movement[0] = 0 #stop the rectangle's movement

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    myRectangle.movement[1] = 0

        myRectangle.update() #updating any changes in our rectangle

        screen.fill(black) #filling the entire screen with black so that to erase everything and redraw them later on
        myRectangle.draw() #drawing our rectangle

        pygame.display.update() #updating the display for any changes on the screen
        clock.tick(FPS) #providing a delay of 1/FPS seconds

    pygame.quit() #quitting from pygame
    quit() #quitting the program

main() #running our main function
