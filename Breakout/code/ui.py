from settings import *

class UI:
    def __init__(self, balls_surf):
        self.display_surface = pygame.display.get_surface()
        self.ball_surfs = balls_surf
    
    def menu(self):
        rect = pygame.FRect(UISIZE['width'], 0, 250, WINDOW_HEIGHT)
        pygame.draw.rect(self.display_surface, COLORS['UIbackground'], rect, 0, 0)

    def ball_count_menu(self):
        #should be a sprite eventually
        rect = pygame.FRect(800, 100, 40, 40)
        pygame.draw.rect(self.display_surface, '#000000', rect, 0, 0)
        ball_surf = self.ball_surfs['1']
        ball_rect = ball_surf.get_frect(topleft = (800, 100))
        self.display_surface.blit(ball_surf, ball_rect)



    def upgrade_menu(self):
        pass

    def draw(self):
        self.menu()
        self.ball_count_menu()

