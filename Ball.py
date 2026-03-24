import pygame
from pygame.locals import *
import random

class Ball():
    # ==== pass an image reference to the initializer ====
    # ballImage = pygame.image.load('images/ball.png')
    # oBall = Ball(window, ballImage)
    # def __init__(self, window, image):
    # ==== pass the path of image to the initializer =====
    # oBall = Ball(window, 'images/ball.png')
    # def __init__(self, window, imagepath):

    # ==== Textbook example ==============================
    def __init__(self, window, windowWidth, windowHeight):
        # Save the parameters from the environment
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        # Define attributes of the object
        self.image = pygame.image.load("images/ball.png")
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        self.x = random.randrange(self.maxWidth)
        self.y = random.randrange(self.maxHeight)

        speedList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedList)
        self.ySpeed = random.choice(speedList)

    def update(self):
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))