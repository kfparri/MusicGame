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

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Music Game')

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
                if keys[K_BACKSPACE]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_TAB]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_CLEAR]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_RETURN]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_PAUSE]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_ESCAPE]:
                    resetScreen = True
                    playsound(soundFiles[0])
                if keys[K_SPACE]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_EXCLAIM]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_QUOTEDBL]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_HASH]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_DOLLAR]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_AMPERSAND]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_QUOTE]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_LEFTPAREN]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_RIGHTPAREN]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_ASTERISK]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_PLUS]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_COMMA]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_MINUS]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_PERIOD]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_SLASH]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_0]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_1]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_2]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_3]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_4]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_5]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_6]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_7]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_8]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_9]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_COLON]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_SEMICOLON]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_LESS]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_EQUALS]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_GREATER]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_QUESTION]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_AT]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_LEFTBRACKET]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_BACKSLASH]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_RIGHTBRACKET]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_CARET]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_UNDERSCORE]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_BACKQUOTE]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_a]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_b]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_c]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_d]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_e]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_f]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_g]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_h]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_i]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_j]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_k]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_l]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_m]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_n]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_o]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_p]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_q]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_r]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_s]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_t]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_u]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_v]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_w]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_x]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_y]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_z]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_DELETE]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP0]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP1]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP2]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP3]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP4]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP5]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP6]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP7]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP8]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP9]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP_PERIOD]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP_DIVIDE]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP_MULTIPLY]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP_MINUS]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP_PLUS]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP_ENTER]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_KP_EQUALS]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_UP]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_DOWN]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_RIGHT]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_LEFT]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_INSERT]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_HOME]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_END]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_PAGEUP]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_PAGEDOWN]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F1]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F2]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F3]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F4]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F5]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F6]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F7]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F8]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F9]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F10]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F11]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F12]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F13]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F14]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_F15]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_NUMLOCK]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_CAPSLOCK]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_SCROLLOCK]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_RSHIFT]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_LSHIFT]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_RCTRL]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_LCTRL]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_RALT]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_LALT]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_RMETA]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_LMETA]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_LSUPER]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_RSUPER]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_MODE]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_HELP]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_PRINT]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_SYSREQ]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_BREAK]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_MENU]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_POWER]:
                    updateScreen = True
                    playsound(soundFiles[0])
                if keys[K_EURO]:
                    updateScreen = True
                    playsound(soundFiles[0])
            
        if resetScreen:
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            screen.blit(background, (0,0))
            pygame.display.update()

        if updateScreen:
            drawMyRect(background)
            screen.blit(background, (0,0))
            pygame.display.update()

if __name__ == '__main__': main()
