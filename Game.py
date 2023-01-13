import pygame
import pygame.math
import sys
import Player

class Game:
    def __init__(self, breite: int, hoehe: int):
        self.game_over = False
        self.youWin = False 
        self.breite = breite
        self.hoehe = hoehe
        size = (breite, hoehe)
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.goundImage = pygame.image.load("Images/ground.png")
        self.spaceImage =  pygame.image.load("Images/stars.png")
        self.initPlayer()
        self.clock = pygame.time.Clock()
        self.endScale = 20

    def HandleKeybord(self):
        # Tastatur befele verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:  # Taste wurde gedrückt
                if event.key == pygame.K_UP:
                    self.player.startBoost()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.player.stopBoost()

    def darawBackground(self):
        winRect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        goundImage = pygame.transform.scale(self.goundImage, (self.screen.get_width(), self.screen.get_height()))
        spaceImage = pygame.transform.scale(self.spaceImage, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(spaceImage, winRect)
        self.screen.blit(goundImage, winRect)

    def initPlayer(self):
        # Init the Player
        p_pos = pygame.math.Vector2(self.screen.get_width()/2, self.screen.get_height()/2)
        p_size = pygame.math.Vector2(48, 96)
        self.player = Player.Player(self, p_pos, p_size)

    def showEnd(self):
        self.darawBackground()
        imgSize = pygame.math.Vector2(self.screen.get_width()/self.endScale, self.screen.get_height()/self.endScale)
        center = pygame.math.Vector2((self.screen.get_width()/2)-(imgSize.x/2), (self.screen.get_height()/2)-(imgSize.y/2))
        # print(imgSize)
        self.endScale -= 3
        if self.endScale <= 1:
            self.endScale = 1
        self.gameover = pygame.image.load("Images/game_over.png")
        self.gameover = pygame.transform.scale(self.gameover, imgSize)
        self.youwinImg = pygame.image.load("Images/youwin.png")
        self.youwinImg = pygame.transform.scale(self.youwinImg, imgSize)
        imgrec = pygame.Rect(center.x, center.y, imgSize.x, imgSize.y)
        if self.youWin:
            self.screen.blit(self.youwinImg, imgrec)
        else:
            self.screen.blit(self.gameover, imgrec)

    def loop(self):
        # -------- Main Program Loop -----------
        while not self.game_over:
            # --- Main event loop
            self.HandleKeybord()
            # self.screen.fill(GRAY)
            self.darawBackground()
            self.player.loop()
            pygame.display.update()
            self.clock.tick(60)
        print(self.player.speed)
        if self.player.speed <= 4:
            self.youWin = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # Taste wurde gedrückt
                    if event.key == pygame.K_q:
                        sys.exit()
            self.showEnd()
            pygame.display.update()
            self.clock.tick(60)

