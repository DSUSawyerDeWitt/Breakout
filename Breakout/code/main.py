from settings import *
from sprites import *
from support import *
from groups import AllSprites
from random import randint
from ui import *
import json

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()

        #sprites
        self.all_sprites = AllSprites()
        self.level = pygame.sprite.Group()
        self.tile_sprites = pygame.sprite.Group()
        self.ball_sprites = pygame.sprite.Group()

        self.ui = UI(self.balls_surf)
        
        #score
        try:
            with open(join('..', 'data', 'score.txt')) as score_file:
                self.score = json.load(score_file)
        except:
            self.score = {'player': 0, 'opponent': 0}
        self.font = pygame.font.Font("../fonts/VCRLED.ttf", 60)

        #spawn level
        #Level(self.level, self.all_sprites, self.tile_sprites)
        #spawn ball
        Level(self.level, self.all_sprites, self.tile_sprites)
        for i in range (1):
            self.ball = BasicBall((self.all_sprites, self.ball_sprites), self.tile_sprites, self)
        #Level(self.level, self.all_sprites, self.tile_sprites)

    def display_score(self):
        player_surf = self.font.render(str(self.score['player']), True, '#ffffff')
        player_rect = player_surf.get_frect(topleft = (10, 0))
        self.display_surface.blit(player_surf, player_rect)

    def update_score(self):
        self.score['player'] += 1
    
    def import_assets(self):
        self.balls_surf = folder_importer('..', 'images', 'balls')


    def run(self):
        while self.running:
            dt = self.clock.tick(120) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('..', 'data', 'score.txt'), 'w') as score_file:
                        json.dump(self.score, score_file)
            #update
            self.all_sprites.update(dt)
            self.level.update(dt) #updates the level group

            #drawing
            self.display_surface.fill(COLORS['background'])
            self.display_score()
            self.all_sprites.draw()
            self.ui.draw()
            pygame.display.update()
        pygame.quit()
        

if __name__ == "__main__":
    game = Game()
    game.run()
