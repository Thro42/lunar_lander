import pygame
import pygame.math
import Game

class Player:
    def __init__(self, game: Game, pos: pygame.math.Vector2, size: pygame.math.Vector2):
        self.game = game
        self.life = True
        self.boost_on = False
        self.draw_center = False
        self.speed = 0
        self.gavety = 0.05
        self.angle = 0
        self.posistion = pos
        self.size = size
        self.image_off = pygame.image.load("Images/space-ship-off.png")
        self.image_on = pygame.image.load("Images/space-ship-on.png")
        self.player = pygame.Rect(pos.x - (size.x/2), pos.y - (size.y/2), size.x, size.y)
    
    def startBoost(self):
        self.boost_on = True

    def stopBoost(self):
        self.boost_on = False

    def move(self):
        self.speed += self.gavety
        if self.boost_on:
            self.speed -= self.gavety * 1.5
        self.posistion.y += self.speed
        if self.posistion.y <= 0:
            self.posistion.y = 0
        if self.posistion.y >= (self.game.screen.get_height()-38):
            self.game.game_over = True
            self.posistion.y = (self.game.screen.get_height()-38)

        pos = self.posistion
        self.player = pygame.Rect(pos.x - (self.size.x/2), pos.y - (self.size.y/2), self.size.x, self.size.y)

    def loop(self):
        if self.boost_on:
            image = pygame.transform.scale(self.image_on, self.size)
        else:
            image = pygame.transform.scale(self.image_off, self.size)
        self.move()
        self.game.screen.blit(image, self.player)
