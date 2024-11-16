#Tiana Dumitrescu
#COP3502C
#Lab 10 - Whackamole
import pygame
import random

def main():
    x = 0
    y = 0
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512)) 
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x <= event.pos[0] <= x+32 and y <= event.pos[1] <= y+32:
                        x = random.randrange(0, 640-32)
                        y = random.randrange(0, 512-32)
            screen.fill("light green")
            #horizontal lines
            for i in range(0, 512, 32):
                pygame.draw.line(screen, (5, 70, 48), (0, i), (640, i))
            #vertical lines
            for i in range(0, 640, 32):
                pygame.draw.line(screen, (5, 70, 48), (i, 0), (i, 512))
            
            #fits into box
            if x % 32 != 0:
                x -= x % 32
            if y % 32 != 0:
                y -= y % 32
            
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
           
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
