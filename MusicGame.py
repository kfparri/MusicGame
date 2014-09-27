#------------------------------------------------------------------------------------------------------
# File Name:    MusicGame.py
# Author:       Kyle Parrish
# Date:         7/4/2014
# Description:  This is a simple program that I wrote for the raspberry pi so that my daughter can
#   play with.  It is a simple program that plays a different sound with every keystroke.  It also
#   displays a simple shape pattern on the screen with each keypress.  The pi can also be setup to
#   allow users to change the sounds by uploading them to a web form on the pi itself.  This code
#   will be included when it is finished.
#------------------------------------------------------------------------------------------------------

# Basic imports for the game
import os,sys,datetime
import pygame
# I don't believe that I need the time references anymore, to be removed with next commit
#from time import strftime, localtime 
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

def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.
    
    This will load the whole sound into memory before playback
    """

    sound = pygame.mixer.Sound(soundfile)
    #clock = pygame.time.Clock()
    sound.play()
    
    #while pygame.mixer.get_busy():
        #clock.tick(FRAMERATE)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Music Game')
    
    # create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    # hide the mouse
    # not used while developing
    #pygame.mouse.set_visible(False)
    
    screen.blit(background, (0,0))
    
    # main loop
    i = 1
    
    while 1:
        # This needs to change to match the new way of checking that I found on the web
        # http://stackoverflow.com/questions/12556535/programming-pygame-so-that-i-can-press-multiple-keys-at-once-to-get-my-character
        
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
        			
        soundfile = "Typewrit-Intermed-538_hifi.ogg"
        soundfile3 = "Typewrit-Bell-Patrick-8344_hifi.ogg"
        
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                return
            elif event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                print(len(keys))
                
                if keys[K_ESCAPE] and keys[K_LCTRL]:
                    pygame.quit()
                    sys.exit()
            	if keys[K_BACKSPACE]:
                    playsound(sounds[0])
            	if keys[K_TAB]:
            	    playsound(sounds[0])
            	if keys[K_CLEAR]:
            	    playsound(sounds[0])
            	if keys[K_RETURN]:
            	    playsound(sounds[0])
            	if keys[K_PAUSE]:
            	    playsound(sounds[0])
            	if keys[K_ESCAPE]:
            	    playsound(sounds[0])
            	if keys[K_SPACE]:
            	    playsound(sounds[0])
            	if keys[K_EXCLAIM]:
            	    playsound(sounds[0])
            	if keys[K_QUOTEDBL]:
            	    playsound(sounds[0])
            	if keys[K_HASH]:
            	    playsound(sounds[0])
            	if keys[K_DOLLAR]:
            	    playsound(sounds[0])
            	if keys[K_AMPERSAND]:
            	    playsound(sounds[0])
		if keys[K_QUOTE]:
    		    playsound(sounds[0])
		if keys[K_LEFTPAREN]:
		    playsound(sounds[0])
		if keys[K_RIGHTPAREN]:
		    playsound(sounds[0])
		if keys[K_ASTERISK]:
		    playsound(sounds[0])
		if keys[K_PLUS]:
		    playsound(sounds[0])
		if keys[K_COMMA]:
		    playsound(sounds[0])
		if keys[K_MINUS]:
		    playsound(sounds[0])
		if keys[K_PERIOD]:
		    playsound(sounds[0])
		if keys[K_SLASH]:
		    playsound(sounds[0])
		if keys[K_0]:
		    playsound(sounds[0])
		if keys[K_1]:
		    playsound(sounds[0])
		if keys[K_2]:
		    playsound(sounds[0])
		if keys[K_3]:
		    playsound(sounds[0])
		if keys[K_4]:
		    playsound(sounds[0])
		if keys[K_5]:
		    playsound(sounds[0])
	    	if keys[K_6]:
		    playsound(sounds[0])
		if keys[K_7]:
		    playsound(sounds[0])
		if keys[K_8]:
		    playsound(sounds[0])
		if keys[K_9]:
		    playsound(sounds[0])
		if keys[K_COLON]:
		    playsound(sounds[0])
		if keys[K_SEMICOLON]:
		    playsound(sounds[0])
		if keys[K_LESS]:
		    playsound(sounds[0])
		if keys[K_EQUALS]:
                    playsound(sounds[0])
		if keys[K_GREATER]:
                    playsound(sounds[0])
		if keys[K_QUESTION]:
		    playsound(sounds[0])
		if keys[K_AT]:
		    playsound(sounds[0])
		if keys[K_LEFTBRACKET]:
		    playsound(sounds[0])
		if keys[K_BACKSLASH]:
		    playsound(sounds[0])
		if keys[K_RIGHTBRACKET]:
                    playsound(sounds[0])
		if keys[K_CARET]:
		    playsound(sounds[0])
		if keys[K_UNDERSCORE]:
		    playsound(sounds[0])
		if keys[K_BACKQUOTE]:
		    playsound(sounds[0])
		if keys[K_a]:
		    playsound(sounds[0])
		if keys[K_b]:
		    playsound(sounds[0])
		if keys[K_c]:
		    playsound(sounds[0])
		if keys[K_d]:
		    playsound(sounds[0])
		if keys[K_e]:
		    playsound(sounds[0])
		if keys[K_f]:
		    playsound(sounds[0])
		if keys[K_g]:
		    playsound(sounds[0])
		if keys[K_h]:
		    playsound(sounds[0])
		if keys[K_i]:
		    playsound(sounds[0])
		if keys[K_j]:
		    playsound(sounds[0])
		if keys[K_k]:
		    playsound(sounds[0])
		if keys[K_l]:
		    playsound(sounds[0])
		if keys[K_m]:
		    playsound(sounds[0])
		if keys[K_n]:
		    playsound(sounds[0])
		if keys[K_o]:
		    playsound(sounds[0])
		if keys[K_p]:
		    playsound(sounds[0])
		if keys[K_q]:
		    playsound(sounds[0])
		if keys[K_r]:
		    playsound(sounds[0])
		if keys[K_s]:
		    playsound(sounds[0])
		if keys[K_t]:
		    playsound(sounds[0])
		if keys[K_u]:
		    playsound(sounds[0])
		if keys[K_v]:
		    playsound(sounds[0])
		if keys[K_w]:
		    playsound(sounds[0])
		if keys[K_x]:
		    playsound(sounds[0])
		if keys[K_y]:
		    playsound(sounds[0])
		if keys[K_z]:
		    playsound(sounds[0])
		if keys[K_DELETE]:
		    playsound(sounds[0])
		if keys[K_KP0]:
		    playsound(sounds[0])
                if keys[K_KP1]:
		    playsound(sounds[0])
		if keys[K_KP2]:
		    playsound(sounds[0])
		if keys[K_KP3]:
		    playsound(sounds[0])
		if keys[K_KP4]:
		    playsound(sounds[0])
		if keys[K_KP5]:
		    playsound(sounds[0])
		if keys[K_KP6]:
		    playsound(sounds[0])
		if keys[K_KP7]:
		    playsound(sounds[0])
		if keys[K_KP8]:
		    playsound(sounds[0])
		if keys[K_KP9]:
		    playsound(sounds[0])
		if keys[K_KP_PERIOD]:
		    playsound(sounds[0])
		if keys[K_KP_DIVIDE]:
		    playsound(sounds[0])
		if keys[K_KP_MULTIPLY]:
		    playsound(sounds[0])
		if keys[K_KP_MINUS]:
		    playsound(sounds[0])
		if keys[K_KP_PLUS]:
		    playsound(sounds[0])
		if keys[K_KP_ENTER]:
		    playsound(sounds[0])
		if keys[K_KP_EQUALS]:
		    playsound(sounds[0])
		if keys[K_UP]:
		    playsound(sounds[0])
		if keys[K_DOWN]:
		    playsound(sounds[0])
		if keys[K_RIGHT]:
		    playsound(sounds[0])
		if keys[K_LEFT]:
		    playsound(sounds[0])
		if keys[K_INSERT]:
		    playsound(sounds[0])
		if keys[K_HOME]:
		    playsound(sounds[0])
		if keys[K_END]:
		    playsound(sounds[0])
		if keys[K_PAGEUP]:
		    playsound(sounds[0])
		if keys[K_PAGEDOWN]:
		    playsound(sounds[0])
		if keys[K_F1]:
		    playsound(sounds[0])
		if keys[K_F2]:
		    playsound(sounds[0])
		if keys[K_F3]:
		    playsound(sounds[0])
		if keys[K_F4]:
		    playsound(sounds[0])
		if keys[K_F5]:
		    playsound(sounds[0])
		if keys[K_F6]:
		    playsound(sounds[0])
		if keys[K_F7]:
		    playsound(sounds[0])
		if keys[K_F8]:
		    playsound(sounds[0])
		if keys[K_F9]:
                    playsound(sounds[0])
		if keys[K_F10]:
		    playsound(sounds[0])
		if keys[K_F11]:
		    playsound(sounds[0])
		if keys[K_F12]:
		    playsound(sounds[0])
		if keys[K_F13]:
		    playsound(sounds[0])
		if keys[K_F14]:
		    playsound(sounds[0])
		if keys[K_F15]:
		    playsound(sounds[0])
		if keys[K_NUMLOCK]:
		    playsound(sounds[0])
		if keys[K_CAPSLOCK]:
		    playsound(sounds[0])
		if keys[K_SCROLLOCK]:
		    playsound(sounds[0])
		if keys[K_RSHIFT]:
		    playsound(sounds[0])
		if keys[K_LSHIFT]:
		    playsound(sounds[0])
		if keys[K_RCTRL]:
		    playsound(sounds[0])
		if keys[K_LCTRL]:
		    playsound(sounds[0])
		if keys[K_RALT]:
		    playsound(sounds[0])
		if keys[K_LALT]:
		    playsound(sounds[0])
                if keys[K_RMETA]:
		    playsound(sounds[0])
		if keys[K_LMETA]:
		    playsound(sounds[0])
		if keys[K_LSUPER]:
		    playsound(sounds[0])
		if keys[K_RSUPER]:
		    playsound(sounds[0])
		if keys[K_MODE]:
		    playsound(sounds[0])
		if keys[K_HELP]:
		    playsound(sounds[0])
		if keys[K_PRINT]:
		    playsound(sounds[0])
		if keys[K_SYSREQ]:
		    playsound(sounds[0])
                if keys[K_BREAK]:
		    playsound(sounds[0])
		if keys[K_MENU]:
		    playsound(sounds[0])
		if keys[K_POWER]:
		    playsound(sounds[0])
		if keys[K_EURO]:
		    playsound(sounds[0])
            #elif event.type == KEYDOWN and event.key == K_ESCAPE:
                #pygame.quit()
                #sys.exit()
                #return
            #elif event.type == KEYDOWN and event.key == K_RETURN:
            	#playsound(sounds[1])
            #elif event.type == KEYDOWN:
            	#playsound(sounds[0])
            	#print(event.key)

if __name__ == '__main__': main()
