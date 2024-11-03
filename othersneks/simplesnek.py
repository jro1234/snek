
from pygame.locals import *
import pygame


class Snek:

    x = 10
    y = 10

    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed
        #self.x = self.y + self.speed + self.x*self.y/(self.x**0.5)


class App:

    windowWidth = 1280
    windowHeight = 720

    player = 0


    def __init__(self):

        self._running      = True
        self._display_surf = None
        self._image_surf   = None
        self.player        = Snek()


    def on_init(self):

        pygame.init()

        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Pygame pythonspot.com example')

        self._running    = True
        self._image_surf = pygame.transform.scale(pygame.image.load("whitemountains.png").convert(), (1280, 720))


    def on_event(self, event):

        if event.type == QUIT:
            self._running = False


    def on_loop(self):

        pass


    def on_render(self):

        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):

        if self.on_init() == False:
            self._running = False

        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()



if __name__ == "__main__" :

    theApp = App()
    theApp.on_execute()

