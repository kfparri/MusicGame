#------------------------------------------------------------------------------------------------------
# File Name:    MusicGame.py
# Author:       Kyle Parrish
# Date:         7/4/2014
# Description:  This is a simple program that I wrote for the raspberry pi so that my daughter can
#   play with.  It is a simple program that plays a different sound with every keystroke.  It also
#   displays a simple shape pattern on the screen with each keypress.  The pi can also be setup to
#   allow users to change the sounds by uploading them to a web form on the pi itself.  This code
#   will be included when it is finished.
# Change log:
#       4.30.15 - Updated the header to test out Visual Studio Code git integration
#       9.18.15 - Started making some changes to the application.  Natalie is starting to enjoy
#                   the application so I'm starting to make it do more:
#               - Updated the code to put circles as well as squares on the screen.
#------------------------------------------------------------------------------------------------------

# Basic imports for the game
import os,sys,datetime
import pygame
# I don't believe that I need the time references anymore, to be removed with next commit
#from time import strftime, localtime
from random import randint
from pygame.locals import *

# Setup basic constants

# Screen height and width
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#CENTER_POINT = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#LOWER_CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
#CENTER_RECT_HEIGHT = 40
#CLOCK_TEXT_FONT = 48

# Colors, any of these can be used in the program
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MATRIX_GREEN = (0, 255, 21)

# Code taken from: http://code.activestate.com/recipes/521884-play-sound-files-with-pygame-in-a-cross-platform-m/
# global constants
FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished

sounds = ["Typewrit-Intermed-538_hifi.ogg",
            "Typewrit-Bell-Patrick-8344_hifi.ogg",
            "Arcade_S-wwwbeat-8528_hifi.ogg",
            "Arcade_S-wwwbeat-8529_hifi.ogg",
            "Arcade_S-wwwbeat-8530_hifi.ogg",
            "Arcade_S-wwwbeat-8531_hifi.ogg",
            "PowerUp-Mark_E_B-8070_hifi.ogg",
            "PulseGun-Mark_E_B-7843_hifi.ogg",
            "PulseSho-Mark_E_B-8071_hifi.ogg",
            "SineySpa-Mark_E_B-7844_hifi.ogg",
            "ToySpace-Mark_E_B-7846_hifi.ogg",
            "ZipUp-Mark_E_B-8079_hifi.ogg"]
soundFiles = []

def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.

    This will load the whole sound into memory before playback
    """

    soundfile.play()
    #sound = pygame.mixer.Sound(soundfile)
    #clock = pygame.time.Clock()
    #sound.play()

    #while pygame.mixer.get_busy():
        #clock.tick(FRAMERATE)

def drawMyRect(surface):
    #pygame.draw.rect(screen, color, (x,y,width,height), thickness)
    pygame.draw.rect(surface, RED, (randint(0,600), randint(0,440), 40,40), 5)
    return surface

def drawMyCircle(surface):
    pygame.draw.circle(surface, GREEN, (randint(0,600), randint(0,440)), 20, 5)
    return surface 

def main():
    pygame.mixer.pre_init(44100,-16,2, 1024)
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Music Game')

    drawCircle = True

    # create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    #allocate all the sound files, this should make it work better...
    for file in sounds:
        tempsound = pygame.mixer.Sound(file)
        soundFiles.append(tempsound)

    # hide the mouse
    # not used while developing
    #pygame.mouse.set_visible(False)

    #pygame.draw.rect(screen, color, (x,y,width,height), thickness)
    #pygame.draw.rect(background, RED, (10,10,40,40), 5)
    #drawMyRect(background)

    screen.blit(background, (0,0))
    pygame.display.update()
    # main loop
    while 1:
        # This needs to change to match the new way of checking that I found on the web
        # http://stackoverflow.com/questions/12556535/programming-pygame-so-that-i-can-press-multiple-keys-at-once-to-get-my-character
        updateScreen = False
        resetScreen = False

        soundfile = "Typewrit-Intermed-538_hifi.ogg"
        soundfile3 = "Typewrit-Bell-Patrick-8344_hifi.ogg"

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                return
            elif event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                #print(len(keys))

                if keys[K_ESCAPE] and keys[K_LCTRL]:
                    pygame.quit()
                    sys.exit()
		elif keys[K_ESCAPE]:
		    resetScreen = True;
		    playsound(soundFiles[1])
                else:
                    updateScreen = True
                    playsound(soundFiles[0])

        if resetScreen:
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            screen.blit(background, (0,0))
            pygame.display.update()

        if updateScreen:
	    if drawCircle:
		drawMyCircle(background)
	    else:
		drawMyRect(background)

	    drawCircle = not drawCircle
            screen.blit(background, (0,0))
            pygame.display.update()

if __name__ == '__main__': main()
