from settings import *

#Clean Up the Code. Learn to Understand everything / Comments

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, tile_sprites, game, ball_image):
        super().__init__(groups)
        self.tile_sprites, self.game, self.image = tile_sprites, game, ball_image
        self.width, self.height = self.image.get_size()
        self.direction = pygame.Vector2(choice([1,-1]),choice([1,-1])).normalize()
        #Random Starting Location
        self.rect = self.image.get_frect(center = (randint(50, (WINDOW_WIDTH - UI_WIDTH) - 50), randint(50, WINDOW_HEIGHT - 50)))
        #self.width, self.height = self.image.get_size()
        #self.pos = pygame.Vector2(self.rect.topleft)
        self.tile_spawn_collision()

    def tile_spawn_collision(self):
        for tile in self.tile_sprites:
            if tile.rect.colliderect(self.rect):
                tile.kill()
                self.game.update_score(tile.lives, 'spawn')  

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
                tile.hit(self.name)
                #self.game.update_score()

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

class BasicBall(Ball):
    instance_count = 0
    def __init__(self, groups, tile_sprites, game, ball_image):
        super().__init__(groups, tile_sprites, game, ball_image)
        BasicBall.instance_count += 1
        self.name = 'Basic Ball'
        #print(f"Ball instance created. Total: {BasicBall.instance_count}")


    def __del__(self):
        # Decrease the count when a Ball instance is deleted or goes out of scope
        BasicBall.instance_count -= 1
        #print(f"Ball instance deleted. Total: {BasicBall.instance_count}")

    def move(self, dt):
        self.rect.x += self.direction.x * SPEED_LEVEL[self.name] * dt #its adding
        self.tile_collision('horizontal')
        self.rect.y += self.direction.y * SPEED_LEVEL[self.name] * dt
        self.tile_collision('vertical')

class SpeedBall(Ball):
    instance_count = 0
    def __init__(self, groups, tile_sprites, game, ball_image):
        super().__init__(groups, tile_sprites, game, ball_image)
        SpeedBall.instance_count += 1
        #Attributes
        self.name = 'Speed Ball'
        self.speed_multiplier = 2

    def __del__(self):
        SpeedBall.instance_count -= 1
    
    def move(self, dt):
        self.rect.x += self.direction.x * SPEED_LEVEL[self.name] * self.speed_multiplier * dt  # Multiply speed by 2
        self.tile_collision('horizontal')
        self.rect.y += self.direction.y * SPEED_LEVEL[self.name] * self.speed_multiplier * dt  # Multiply speed by 2
        self.tile_collision('vertical')

class MonsterBall(Ball): #Scale, Twice as big and Double Damage
    instance_count = 0
    def __init__(self, groups, tile_sprites, game, ball_image):
        super().__init__(groups, tile_sprites, game, ball_image)
        MonsterBall.instance_count += 1
        self.name = 'Monster Ball'
        self.scale = 1.5
        self.image = pygame.transform.scale(ball_image, (self.width * self.scale, self.height * self.scale))
        self.rect = self.image.get_frect(center = self.rect.center)
        self.tile_spawn_collision()

    def __del__(self):
        MonsterBall.instance_count -= 1
    
    def move(self, dt):
        self.rect.x += self.direction.x * SPEED_LEVEL[self.name] * dt #its adding
        self.tile_collision('horizontal')
        self.rect.y += self.direction.y * SPEED_LEVEL[self.name] * dt
        self.tile_collision('vertical')

class SniperBall(Ball):
    instance_count = 0
    def __init__(self, groups, tile_sprites, game, ball_image):
        super().__init__(groups, tile_sprites, game, ball_image)
        SniperBall.instance_count += 1
        self.name = 'Sniper Ball'

    def __del__(self):
        SniperBall.instance_count -= 1
        #add goes to nearest tile after hitting the wall, by changing the direction.

    def move(self, dt):
        self.rect.x += self.direction.x * SPEED_LEVEL[self.name] * dt #its adding
        self.tile_collision('horizontal')
        self.rect.y += self.direction.y * SPEED_LEVEL[self.name] * dt
        self.tile_collision('vertical')
    
    def closest_tile(self):
        if not self.tile_sprites:
            return None
        
        ball_center = pygame.Vector2(self.rect.center)

        closest = min(self.tile_sprites, key = lambda tile: ball_center.distance_to(pygame.Vector2(tile.rect.center)))
        return closest
    
    def move_towards_tile(self, tile):
        target_pos = pygame.Vector2(tile.rect.center)
        ball_pos = pygame.Vector2(self.rect.center)

        new_direction = (target_pos - ball_pos).normalize()
        self.direction = new_direction

    def wall_collision(self):
        nearest_tile = None
        if self.rect.top <= 0: #top
            self.rect.top = 0
            self.direction.y *= -1
            nearest_tile = self.closest_tile()
    
        if self.rect.bottom >= WINDOW_HEIGHT: #bottom
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1
            nearest_tile = self.closest_tile()

        if self.rect.left <= 0: #left
            self.rect.left = 0
            self.direction.x *= -1
            nearest_tile = self.closest_tile()

        if self.rect.right >= UISIZE['width']: #right (menu)
            self.rect.right = UISIZE['width']
            self.direction.x *= -1
            nearest_tile = self.closest_tile()
        if nearest_tile:
            self.move_towards_tile(nearest_tile)

class Tiles(pygame.sprite.Sprite):
    def __init__(self, tile_surfs, groups, pos, game):
        super().__init__(groups)
        self.font = pygame.font.Font(None, 15) #need to change the font.
        #image
        self.tile_surfs = tile_surfs
        self.image = self.tile_surfs['sprite_00'].copy()
        #rect & movement
        self.rect = self.image.get_frect(topleft = (pos))
        self.lives = 1
        self.update_tile()
        self.clicked = False
        self.prev_mouse_pressed = False
        self.game = game

    def update_tile(self):
        #Adds the Lives Numbers to the Center of the Tiles.
        text_surf = self.font.render(str(self.lives), True, 'white')
        text_rect = text_surf.get_frect(center =(SIZE['basic tile'][0] / 2, SIZE['basic tile'][1] / 2))
        self.image.blit(text_surf, text_rect)

    def tile_color_picker(self): #maybe use case:
        self.argument = (self.lives % 10)
        match self.argument:
            case 0: #for 10,20,30 ect. (not 0)
                self.image = self.tile_surfs['sprite_09'].copy()
            case 1:
                self.image = self.tile_surfs['sprite_00'].copy()
            case 2:
                self.image = self.tile_surfs['sprite_01'].copy()
            case 3:
                self.image = self.tile_surfs['sprite_02'].copy()
            case 4:
                self.image = self.tile_surfs['sprite_03'].copy()
            case 5:
                self.image = self.tile_surfs['sprite_04'].copy()
            case 6:
                self.image = self.tile_surfs['sprite_05'].copy()
            case 7:
                self.image = self.tile_surfs['sprite_06'].copy()
            case 8:
                self.image = self.tile_surfs['sprite_07'].copy()
            case 9:
                self.image = self.tile_surfs['sprite_08'].copy()

    def tile_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        #mouse_pressed = pygame.mouse.get_pressed()[0]
        if pygame.mouse.get_pressed()[0] and not self.prev_mouse_pressed and self.rect.collidepoint(mouse_pos) and not self.clicked:
            self.hit('Click')
            self.clicked = True
        if not pygame.mouse.get_pressed()[0] and self.clicked:
            self.clicked = False
        self.prev_mouse_pressed = pygame.mouse.get_pressed()[0]

    def update(self, dt):
        self.tile_clicked()


    def hit(self, name): #should update score inside of hit.
        self.lives -= STRENGTH_LEVEL[name]
        if self.lives < 0:
            DAMAGE_DONE[name] += self.lives + STRENGTH_LEVEL[name]
        else:
            DAMAGE_DONE[name] += STRENGTH_LEVEL[name]
        if self.lives <= 0:
            self.kill() #remove the tile
            self.game.update_score(self.lives, name)
        else:
            self.tile_color_picker() #change the color
            self.update_tile()  # Redraw tile with new lives count
            self.game.update_score(self.lives, name)

class ExplodingTile(Tiles): #Maybe later
    pass
        
