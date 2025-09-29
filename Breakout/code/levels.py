from settings import *
from sprites import *

class Level():
    def __init__(self, game, tile_surfs, all_sprites, tile_sprites):
        self.all_sprites, self.tile_sprites = all_sprites, tile_sprites
        self.tile_surfs, self.game = tile_surfs, game
        #self.default_level()
        self.default_level()
        self.level_count = 0
        self.display_surface = pygame.display.get_surface()


    def testing_level(self):
        self.tile = Tiles(self.tile_surfs, (self.all_sprites, self.tile_sprites), game = self.game,
        pos = (200, 400))

        self.tile = Tiles(self.tile_surfs, (self.all_sprites, self.tile_sprites), game = self.game,
        pos = (500, 400))

    def default_level(self):
        rows = 20 #20
        columns = 10  # 10 #12 is max
        offsetx = (UISIZE['width'] - (columns * SIZE['basic tile'][0] * 1.1) + SIZE['basic tile'][0] * .1) / 2# plus a cube
        offsety = (WINDOW_HEIGHT - (rows * SIZE['basic tile'][1] * 1.1) + SIZE['basic tile'][1] * .1) / 2
        for y in range(rows): #200 square block #20
            for x in range(columns): #10
                self.tile = Tiles(self.tile_surfs, (self.all_sprites, self.tile_sprites), game = self.game,
                pos = (offsetx + (x * SIZE['basic tile'][0] * 1.1), (offsety + (y * SIZE['basic tile'][1] * 1.1))))


    def is_within_circle(self, circle_center, circle_radius):
        tile_center_x = self.rect.centerx
        tile_center_y = self.rect.centery
        distance = math.sqrt((tile_center_x - circle_center[0]) ** 2 + (tile_center_y - circle_center[1]) ** 2)
        return distance <= circle_radius

    def TIE_Fighter_level(self):
        rows = 20
        columns = 11
        xoffset = (((WINDOW_WIDTH - UI_WIDTH) - (columns * SIZE['basic tile'][0] * 1.1) + SIZE['basic tile'][0] * .1) / 2)
        offsety = (WINDOW_HEIGHT - (rows * SIZE['basic tile'][1] * 1.1) + SIZE['basic tile'][1] * .1) / 2
        Locations = []
        for m in range(rows): #TURN THIS INTO A TIEFIGHTER
            for i in range(9):
                if (m == 0 or m == rows-1) and i not in range(3,6):
                    Locations += [(i+1,m)]
                elif ((m == 1 or m == 2) or (m == rows-2 or m == rows-3)) and i not in range(2,7):
                    Locations += [(i+1,m)]
                elif ((m == 3 or m == 4) or (m == rows-4 or m == rows-5)) and i not in range(1,8):
                    Locations += [(i+1,m)]


        #Locations = [(i,0) for i in range(9) if i not in range(3,6)]
        for y in range(rows):
            for x in range(columns):
                    if (x,y) not in Locations:
                        self.tile = Tiles(self.tile_surfs, (self.all_sprites, self.tile_sprites), game = self.game,
                        pos = ((xoffset + x * SIZE['basic tile'][0] * 1.1), ((offsety + (y * SIZE['basic tile'][1] * 1.1)))))



    def new_level(self):
        if len(self.tile_sprites) == 0:
            if self.level_count % 2 == 1:
                self.default_level()
            else:
                self.TIE_Fighter_level()
            self.level_count += 1


    def update(self, dt):
        self.new_level()
