import pygame

class InputHandler:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((100, 100))

    def wait_for_space(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
            pygame.time.wait(20) # Small delay to prevent high CPU usage
