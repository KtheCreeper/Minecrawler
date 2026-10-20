import pygame
import sys

class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((550,550), pygame.RESIZABLE)
        pygame.display.set_caption('Mine-crawler')

        
    
    def run(self):
        running = True
        delta_time = 0.1
        clock = pygame.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.screen.fill("white")

            pygame.display.flip()
            delta_time = clock.tick(60) / 1000
            delta_time = max(0.001, min(0.1, delta_time))

if __name__ == "__main__":
    game().run()
