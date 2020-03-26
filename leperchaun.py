import pygame, random

class Lucky:
    def __init__(self,pos):
        self.leperstand = pygame.image.load("leperstand.png")
        self.leperwalk1 = pygame.image.load("leperwalk1.png")
        self.leperwalk2 = pygame.image.load("leperwalk2.png")
        self.standrect = self.leperstand.get_rect()
        self.walk1rect = self.leperwalk1.get_rect()
        self.walk2rect = self.leperwalk2.get_rect()
        self.speed = pygame.math.Vector2(0, 10)
        self.rotation = random.randint(0, 360)
        self.speed.rotate_ip(self.rotation)
        self.leperstand = pygame.transform.rotate(self.leperstand, self.rotation)
        self.standrect.center = pos
    def __update__(self):
        self.screen_info = pygame.display.Info()
        self.standrect.move_ip(self.speed)
        if self.standrect.left < 0 or self.standrect.right < self.screen_info.current_w:
            self.speed[0] *= -1
            self.leperstand = pygame.transform.flip(self.leperstand, True, False)
            self.standrect.move_ip(self.speed[1], 0)
        if self.standrect.top < 0 or self.standrect.right > self.screen_info.current_h:
            self.speed[1] *= -1
            self.leperstand = pygame.transform.flip(self.leperstand, True, False)
            self.standrect.move_ip(self.speed[1], 0)
    def __draw__(self, screen):
        screen.blit(self.leperstand, self.standrect)
        screen.blit(self.leperwalk1, self.walk1rect)
        screen.blit(self.leperwalk2, self.walk2rect)
        self.__update__()