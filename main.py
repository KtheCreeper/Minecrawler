import pygame
import sys
from typing import Literal

class Object:
    def __init__(self, type:Literal["PLAYER","STONE"], x_pos:int, y_pos:int, visibility:Literal[0,1,2,3] = 0) -> None:
        self.type = type
        self.pos = x_pos, y_pos
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.visibility = visibility

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((550,550)) # 39x21 chars
        pygame.display.set_caption('Mine-crawler')
        self.font = pygame.Font("ProggyCleanCP.fon")

        self.objects:list[Object] = [Object("PLAYER",5,6),Object("STONE",12,6,1)]

    def draw_screen(self):
        screen_array:list[list[str]] = []
        for i in range(21):
            screen_array.append([])
            for _ in range(39):
                screen_array[i].append(" ")

        for object in self.objects:
            match object.type:
                case "PLAYER":
                    screen_array[object.y_pos][object.x_pos] = "@"
                case "STONE" :
                    screen_array[object.y_pos][object.x_pos] = "#"
                case _ :
                    pass
        
        screen_rows_array:list[str] = []
        for array in screen_array:
            screen_rows_array.append("".join(array) + "\n")
        screen_str = "".join(screen_rows_array)
        return screen_str
    
    def run(self):
        running = True
        delta_time = 0.1
        clock = pygame.Clock()
        text_scale = 2
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.screen.fill("black")

            text_surface = self.font.render(self.draw_screen(), False, (255,255,255))
            text_surface = pygame.transform.scale(text_surface, (
                text_surface.width * text_scale,
                text_surface.height * text_scale
            ))
            self.screen.blit(text_surface, (0,0))

            for object in self.objects:
                if object.type != "PLAYER":
                    wall_surface = self.font.render("#", False, (33 * object.visibility, 33 * object.visibility, 33 * object.visibility))
                    wall_surface = pygame.transform.scale(
                        wall_surface,
                        (wall_surface.width * text_scale, wall_surface.height * text_scale)
                    )
                    cell_width = self.font.size(" ")[0] * text_scale
                    cell_height = self.font.get_linesize() * text_scale
                    self.screen.blit(
                        wall_surface,
                        (object.x_pos * cell_width, object.y_pos * cell_height)
                    )

            pygame.display.flip()
            delta_time = clock.tick(60) / 1000
            delta_time = max(0.001, min(0.1, delta_time))

if __name__ == "__main__":
    Game().run()
