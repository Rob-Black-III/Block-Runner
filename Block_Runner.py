import pygame, sys, random, os
import time
from pygame.locals import *
from pygame.sprite import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,100,0)
LIME_GREEN = (0,255,0)

#Initialize Pygame
pygame.init()

#Make a variable to set framerate
clock = pygame.time.Clock()

#Set up the window
myWindow = pygame.display.set_mode((700,400))
pygame.display.set_caption("Block Runner")
class Block(pygame.sprite.Sprite):
    #Constructor or the init method
    #pass in the color of the block and its width and height
    def __init__(self, color, width, height):
        #call the parent class's constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        #Create a rectangular object that has the right dimensions
        self.rect = self.image.get_rect()
        self.blockCounter = 8
        self.totalDistance = 0
    def move(self):
        self.rect.x -= self.blockCounter
class Player(Block):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png").convert()
        #Set transparency color.
        self.image.set_colorkey(WHITE)
        #Create the rectangle object for the image.
        self.rect=self.image.get_rect()
        self.isJumping = False
        self.isSliding = False
        self.tc = 0
        self.startingMove = 0
        #time counter
    def move(self):
        if self.rect.x >= 350:
            self.rect.x+=0
        else:
            self.rect.x += 10
            static_block.totalDistance += 10
            print("Distance: " + str(static_block.totalDistance) + " meters")
        """if self.isSliding == True and self.isJumping == True:
            self.image = pygame.image.load("player_slide.png").convert()
            self.image.set_colorkey(WHITE)
            self.isSliding = False
            self.isJumping = False
            self.rect.y = 343
            self.tc+=1
            self.rect.y += -15 * self.tc +1 * self.tc**2
            if self.rect.y >= 327:
                self.rect.y = 327
                self.isJumping = False
                self.tc = 0"""
        if self.isSliding == True and self.isJumping == True:
            pass
        if self.isSliding == True:
            self.rect.y = 343
            self.image = pygame.image.load("player_slide.png").convert()
            self.image.set_colorkey(WHITE)
            self.isSliding = False
        if self.isJumping == True:
            self.rect.y = 327
            self.tc+=1
            self.rect.y += -15 * self.tc +1 * self.tc**2
            if self.rect.y >= 327:
                self.rect.y = 327
                self.isJumping = False
                self.tc = 0
        if self.rect.x >= 700:
            self.rect.x = -50
    def reset(self):
        self.image = pygame.image.load("player.png").convert()
        #Set transparency color.
        self.image.set_colorkey(WHITE)
        player.rect.y = 327
        
    def isDead(self):
        self.image = pygame.image.load("player_dead.png").convert()
        #Set transparency color.
        self.image.set_colorkey(WHITE)
        player.rect.y = 341
        myWindow.fill(WHITE)
        #Draw the sprites
        all_sprites.draw(myWindow)
        static_block_list.draw(myWindow)
        pygame.display.flip()
        time.sleep(0.5)

    #Update the screen
    pygame.display.flip()
     
class Textured_Block(Block):
    def __init__(self, width, height):
        Block.__init__(self, RED, width, height)
        self.image = pygame.image.load("block.png").convert()
        #Set transparency color.
        self.image.set_colorkey(WHITE)
        #Create the rectangle object for the image.
        self.rect=self.image.get_rect()

#In Development
class Laser(Block):
    def shootLaser(self):
        self.rect.x -=3
    def removeLaser(self):
        pygame.Sprite.sprite.kill(laser)
        
def getScores():
    curScore = 0
    highScore = -1
    highScore_pos = 0
    list_pos = 0
    my_file_player = open("playerName.txt", "r")
    my_file_score = open("playerScores.txt", "r")
    my_score_list = []
    my_player_list = []
    my_player_list = my_file_player.read().splitlines()
    my_score_list = my_file_score.read().splitlines()
    print()
    print(my_player_list)
    print(my_score_list)
    my_file_player.close()
    my_file_score.close()
    while len(my_score_list) > 0:
        while list_pos < len(my_score_list):
            curScore = my_score_list[list_pos]
            if int(curScore) >= int(highScore):
                highScore = curScore
                highScore_pos = list_pos
            list_pos+=1
        print(str(highScore_pos))
        print(my_player_list[highScore_pos])
        print(my_score_list[highScore_pos])
        my_score_list = my_score_list
        my_player_list = my_player_list

def enterScores():
    #Entering New Score
    print("Your Score: " + str(finalScore) + " meters")
    print("What is your name? ")
    player_name = input()
    my_file_player = open("playerName.txt", "r+")
    my_file_score = open("playerScores.txt", "r+")
    temp_text_name = my_file_player.read()
    temp_text_score = my_file_score.read()
    my_file_player.write(temp_text_name + player_name+ "\n")
    my_file_score.write(temp_text_score + str(finalScore) +"\n")
    my_file_player.close()
    my_file_score.close()
        
        

#Assign Groups Here:
all_sprites = pygame.sprite.Group()
static_block_list = pygame.sprite.Group()

#Generates Random Blocks
block_num = 1
while block_num <= 50:
    #this represent a single enemy block
    static_block = Textured_Block(20,20)
    #put it in a random position
    position_chooser_1 = random.randint(0,1)
    if position_chooser_1 == 0: 
        static_block.rect.y = 345
    if position_chooser_1 == 1:
        static_block.rect.y = 310
        #240 is the spacin between each block
    static_block.rect.x = 240 * block_num
    static_block.rect.x += 100
    #Add to sprite lists
    static_block_list.add(static_block)
    #all_sprites.add(static_block)
    block_num = block_num + 1
    
#Assign "player" Block
player = Player(20,40)
player.rect.x = 30
player.rect.y = 327

#Make the "ground" Block
ground = Block(GREEN, 9000,30)
ground.rect.y = 375

#Add player and ground to the list to be updated
all_sprites.add(ground)
all_sprites.add(player)

runningRight = False
runningLeft = False
counter =0
while True:
    #Controls:
    player.move()
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_UP:
                player.isJumping = True
            if event.key == K_DOWN:
                if player.rect.y >= 327:
                    player.isSliding = True
        if event.type == KEYUP:
            if event.key == K_DOWN:
                player.reset()
                player.rect.y -16
    #Collision Checking:
    block_hit_list = pygame.sprite.spritecollide(player, static_block_list, True)
    for block in static_block_list:
        if len(block_hit_list):
            player.isDead()
            player.kill()
            finalScore = static_block.totalDistance
            getScores()
            enterScores()
            pygame.quit()
            sys.exit()
            
    #Clear the screen
    myWindow.fill(WHITE)

    #Shifts all sprites negative in order to advance in game.
    if player.rect.x >= 350:
        for block in static_block_list:
            block.move()
        static_block.totalDistance += static_block.blockCounter
        print("Distance: " + str(static_block.totalDistance) + " meters")
        counter+=1
        if counter > 40:
            for block in static_block_list:
                block.blockCounter +=1
            counter = 0
        
    #Draw the sprites
    all_sprites.draw(myWindow)
    static_block_list.draw(myWindow)

    #Update the screen
    pygame.display.flip()
    
    #Limit to 20 frames per second
    clock.tick(24)
