import pygame
import os

class DrinkSelection:

    def __init__(self, win, width, height, fps) -> None:

        self.WIDTH, self.HEIGHT = width, height
        self.WIN = win
        self.FPS = fps

        # Read in background images
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/drink_select', 'frame_0.png')), 
                                            (self.WIDTH, self.HEIGHT))
        self.SELECT_GRID = [pygame.transform.scale(pygame.image.load(os.path.join('assets/drink_select', 'frame_' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(1,7)]
        # Define colors
        self.WHITE = (255,255,255)

    def draw_window(self, select_i):

        if select_i < 0:
            self.WIN.blit(self.BG, (0,0))
        else:
            self.WIN.blit(self.SELECT_GRID[select_i], (0,0))

        # update
        pygame.display.update()


    def run_scene(self):
        # initialize clock
        clock = pygame.time.Clock()
        run = True
        select_i = -1

        # game loop
        while(run):
            clock.tick(self.FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    
                    # Start select mode
                    if select_i == -1:
                        select_i += 1

                    # Return drink selected
                    elif event.key == pygame.K_RETURN:
                        return select_i + 1

                    # Move selection
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and select_i < 3:
                        select_i += 3
                    elif (event.key == pygame.K_UP or event.key == pygame.K_w) and select_i > 2:
                        select_i -= 3
                    elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and select_i%3 != 0:
                        select_i -= 1
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and select_i%3 != 2:
                        select_i += 1

                            
            self.draw_window(select_i)


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = DrinkSelection(win, w, h)

    mc.run_scene()