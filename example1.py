import sys, pygame, random, time
from pygame.locals import *
from leperchaun import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w /2), int(screen_info.current_h /2))
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
color = (255,255,255)
chauns = []

global leperstand
global leperwalk1
global leperwalk2
global speed

def main():
    for i in range(10):
        chauns.append(Lucky((width/2, height/2)))
    while True:
        clock.tick(60)
        screen.fill(color)
        for leper in chauns:
            leper.__draw__(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(event.type)
            if event.type == KEYDOWN:
                if event.key == K_d:
                    for i in range(len(chauns) // 2):
                        chauns.pop(0)
        pygame.display.flip()

if __name__ == "__main__":
    main()