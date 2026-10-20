import pygame
import sys

class Object:
    def __init__(self, type:str, x_pos:int, y_pos:int):
        self.type = type
        self.pos = x_pos, y_pos
        self.x_pos = x_pos
        self.y_pos = y_pos

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((550,550)) # 39x21 chars
        pygame.display.set_caption('Mine-crawler')
        self.font = pygame.Font("ProggyCleanCP.fon")

    def blank_screen(self):
        screen_array:list[list[str]] = []
        for i in range(21):
            screen_array.append([])
            for _ in range(39):
                screen_array[i].append(" ")
        
        screen_rows_array:list[str] = []
        for array in screen_array:
            screen_rows_array.append("".join(array) + "\n")
        screen_str = "".join(screen_rows_array)
        return screen_str
    
    def run(self):
        running = True
        delta_time = 0.1
        clock = pygame.Clock()
        #objects = []
        text_scale = 2
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.screen.fill("black")

            text_surface = self.font.render(self.blank_screen(), False, (255,255,255))
            text_surface = pygame.transform.scale(text_surface, (
                text_surface.width * text_scale,
                text_surface.height * text_scale
            ))
            self.screen.blit(text_surface, (0,0))

            pygame.display.flip()
            delta_time = clock.tick(60) / 1000
            delta_time = max(0.001, min(0.1, delta_time))

if __name__ == "__main__":
    Game().run()
