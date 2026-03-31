# 1 - Import packages
import pygame
from pygame.locals import *
import sys

import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30  # 30 frames per second -->  1/30 ~ 33 minisecond

def ResetCounter(nickName):
    #print('reset')
    global frameCount
    if nickName == "Reset":
        frameCount = 0
    elif nickName == "Start":
        print("Start Button is clicked")


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
oFrameCountLabel = pygwidgets.DisplayText(window, (60, 20),
                                          'Program has run throught this main loop: ',
                                          fontSize=24, width=350, textColor=WHITE,
                                          justified='center')
oFrameCountDisplay = pygwidgets.DisplayText(window, (450, 20), '00000',
                                            fontSize=24, width=50, textColor=WHITE,
                                            justified='right')
oRestartButton = pygwidgets.CustomButton(window, (280, 60),
                                         'images/buttonUp.png',
                                         down='images/buttonDown.png',
                                         nickname="Reset",
                                         callBack=ResetCounter)
oStartButton = pygwidgets.TextButton(window, (280, 100), "Start",
                                     nickname="Start",
                                     callBack=ResetCounter)

# 5 - Initialize variables
frameCount = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        oRestartButton.handleEvent(event)
        oStartButton.handleEvent(event)

    # 8 - Do any "per frame" actions
    frameCount = frameCount + 1
    oFrameCountDisplay.setValue(frameCount)

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()
    oStartButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait