from settings import *
from sprites import *
from support import *
from levels import *
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

        
        #score
        try:
            with open(join('..', 'data', 'score.txt')) as score_file:
                self.score = json.load(score_file)
        except:
            self.score = {'player': 0, 'opponent': 0}

        self.ui = UI(self.ball_surfs, self.UI_ball_surfs, self.UI_upgrade_surfs, self)
        #spawn level
        self.level = Level(self, self.tile_surfs, self.all_sprites, self.tile_sprites)


    def ball_spawner(self): #spawn ball
        if NUMBEROFBALLS['Basic Ball'] > BasicBall.instance_count:
            self.basic_ball = BasicBall((self.all_sprites, self.ball_sprites), self.tile_sprites, self, self.ball_surfs['Basic Ball'])
        if NUMBEROFBALLS['Speed Ball'] > SpeedBall.instance_count:
            self.speed_ball = SpeedBall((self.all_sprites, self.ball_sprites), self.tile_sprites, self, self.ball_surfs['Speed Ball'])
        if NUMBEROFBALLS['Monster Ball'] > MonsterBall.instance_count:
            self.monster_ball = MonsterBall((self.all_sprites, self.ball_sprites), self.tile_sprites, self, self.ball_surfs['Monster Ball'])
        if NUMBEROFBALLS['Sniper Ball'] > SniperBall.instance_count:
            self.sniper_ball = SniperBall((self.all_sprites, self.ball_sprites), self.tile_sprites, self, self.ball_surfs['Sniper Ball'])


    def display_score(self):
        player_surf = self.font.render(str(self.score['player']), True, '#ffffff')
        player_rect = player_surf.get_frect(topleft = (10, 0))
        self.display_surface.blit(player_surf, player_rect)

    def update_score(self, lives, name):
        if name == 'spawn':
            self.score['player'] += lives
        elif lives < 0:
            self.score['player'] += lives + STRENGTH_LEVEL[name]
        else:
            self.score['player'] += STRENGTH_LEVEL[name]
    
    def import_assets(self):
        self.ball_surfs = folder_importer('..', 'images', 'balls')
        self.UI_ball_surfs = folder_importer('..', 'images', 'UI', 'UI Balls')
        self.UI_upgrade_surfs = folder_importer('..', 'images', 'UI', 'UI Upgrades')
        self.tile_surfs = folder_importer('..', 'images', 'tiles')
        self.font = pygame.font.Font("../fonts/VCRLED.ttf", 60)

    def run(self):
        while self.running:
            dt = self.clock.tick(120) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('..', 'data', 'score.txt'), 'w') as score_file:
                        json.dump(self.score, score_file)
            #update
            #self.mouse_click()
            self.ball_spawner()
            #drawing
            self.display_surface.fill(COLORS['background'])
            self.all_sprites.draw()
            self.all_sprites.update(dt)
            self.level.update(dt) #updates the level group
            self.display_score()
            self.ui.draw()
            pygame.display.update()
        pygame.quit()
        

if __name__ == "__main__":
    game = Game()
    game.run()
