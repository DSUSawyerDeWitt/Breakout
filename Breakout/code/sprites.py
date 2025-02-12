from settings import *

#Clean Up the Code. Learn to Understand everything / Comments

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

class BasicBall(Ball):
    def __init__(self, groups, tile_sprites, game):
        super().__init__(groups)
        self.tile_sprites = tile_sprites
        self.game = game
        #image
        #self.image = pygame.Surface(SIZE['basic ball'], pygame.SRCALPHA)
        self.image = pygame.Surface(SIZE["basic ball"], pygame.SRCALPHA)

        pygame.draw.circle(self.image, '#A1A1A1', (SIZE["basic ball"][0] / 2, SIZE["basic ball"][1] / 2), SIZE["basic ball"][0] / 2,)
        #pygame.draw.circle(self.image, '#000000', (SIZE["basic ball"][0] / 2, SIZE["basic ball"][1] / 2), SIZE["basic ball"][0] / 2, 2)
        #pygame.draw.circle(self.image, '#000000', (WINDOW_WIDTH / 2 + 221, WINDOW_HEIGHT / 2 + 10), 50 / 2)

        #rect & movement
        #self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2 + 221, WINDOW_HEIGHT / 2 + 10))#(200, 500))
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2(1,1)
        #self.score = 0
        self.pos = pygame.Vector2(self.rect.topleft)
        self.tile_spawn_collision()

    
    def move(self, dt):
        self.rect.x += self.direction.x * SPEED['basic ball'] * dt #its adding
        self.tile_collision('horizontal')
        self.rect.y += self.direction.y * SPEED['basic ball'] * dt
        self.tile_collision('vertical')

    def tile_spawn_collision(self):
        for tile in self.tile_sprites:
            if tile.rect.colliderect(self.rect):
                tile.kill()
                self.game.update_score()  

    def tile_collision(self, direction):
        for tile in self.tile_sprites:
            if tile.rect.colliderect(self.rect):
                if direction == 'horizontal': #sprite = tile  rect = ball
                    if self.direction.x > 0: self.rect.right = tile.rect.left
                    if self.direction.x < 0: self.rect.left = tile.rect.right
                    self.direction.x *= -1
                if direction == 'vertical': #sprite = object  rect = ball
                    if self.direction.y > 0: self.rect.bottom = tile.rect.top
                    if self.direction.y < 0: self.rect.top = tile.rect.bottom
                    self.direction.y *= -1
                tile.hit()
                self.game.update_score()

    def wall_collision(self):
        if self.rect.top <= 0: #top
            self.rect.top = 0
            self.direction.y *= -1
    
        if self.rect.bottom >= WINDOW_HEIGHT: #bottom
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1

        if self.rect.left <= 0: #left
            self.rect.left = 0
            self.direction.x *= -1

        if self.rect.right >= UISIZE['width']: #right (menu)
            self.rect.right = UISIZE['width']
            self.direction.x *= -1

    def update(self, dt):
        self.move(dt)
        self.wall_collision()

class Tiles(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.font = pygame.font.Font(None, 15) #need to change the font.

        #image
        self.image = pygame.Surface(SIZE['basic tile'])

        #rect & movement
        self.rect = self.image.get_frect(topleft = (pos))
        self.lives = 2
        self.update_tile()

    def update_tile(self):
        #Adds the Lives Numbers to the Center of the Tiles.
        text_surf = self.font.render(str(self.lives), True, 'white')
        text_rect = text_surf.get_frect(center =(SIZE['basic tile'][0] / 2, SIZE['basic tile'][1] / 2))
        self.image.blit(text_surf, text_rect)

    def tile_color_picker(self): #maybe use case:
        if self.lives == 2:
            self.image.fill('black')
        elif self.lives == 1:
            self.image.fill('black')

    def hit(self):
        self.lives -= 1
        self.tile_color_picker() #change the color
        if self.lives <= 0:
            self.kill() #remove the tile
        else:
            self.update_tile()  # Redraw tile with new lives count

class Level(pygame.sprite.Sprite): #Use acutal spries for the tiles.
    def __init__(self, groups, all_sprites, tile_sprites):
        super().__init__(groups)
        self.all_sprites = all_sprites
        self.tile_sprites = tile_sprites
        self.default_level()

    def default_level(self):
        rows = 20
        columns = 10  #12 is max
        offsetx = (UISIZE['width'] - (columns * SIZE['basic tile'][0] * 1.1) + SIZE['basic tile'][0] * .1) / 2# plus a cube
        offsety = (WINDOW_HEIGHT - (rows * SIZE['basic tile'][1] * 1.1) + SIZE['basic tile'][1] * .1) / 2
        for y in range(rows): #200 square block #20
            for x in range(columns): #10
                self.tile = Tiles((self.all_sprites, self.tile_sprites),
                #pos = (200 + (x * SIZE['basic tile'][0] * 1.1), 100 + (y * SIZE['basic tile'][1] * 1.1)))
                pos = (offsetx + (x * SIZE['basic tile'][0] * 1.1), (offsety + (y * SIZE['basic tile'][1] * 1.1))))

                #0 55 110 165


    def new_level(self):
        if len(self.tile_sprites) == 0:
            self.default_level()

    def update(self, dt):
        self.new_level()
        
