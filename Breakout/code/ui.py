from settings import *

class UI():
    def __init__(self, ball_surfs, UI_ball_surfs, UI_upgrade_surfs, game_instance):
        self.display_surface = pygame.display.get_surface()
        self.ball_surfs, self.UI_ball_surfs, self.UI_upgrade_surfs = ball_surfs, UI_ball_surfs, UI_upgrade_surfs
        self.game = game_instance
        #Open Menus
        self.Open_Strength_Menu = False
        self.Open_Speed_Menu = False
        self.Open_Mouse_Menu = False
        self.y_offset = 25

        #Fonts
        self.Main_UI_Ball_Name_font = pygame.font.SysFont('../fonts/Lato-Regular.ttf', 25)
        #self.font = pygame.font.SysFont(None, 25)
        self.Strength_UI_Menu_Font = pygame.font.Font('../fonts/Lato-Regular.ttf', 15)
        self.Title_Font = pygame.font.Font('../fonts/Lato-Regular.ttf', 40)
        self.Ball_Count_Font = pygame.font.Font('../fonts/Lato-Regular.ttf', 40)
        self.Title_Font.set_underline(True)

    def menu(self):
        rect = pygame.FRect(UISIZE['width'], 0, 250, WINDOW_HEIGHT)
        pygame.draw.rect(self.display_surface, COLORS['UIbackground'], rect, 0, 0) 
        #pygame.draw.rect(self.display_surface, 'grey', rect, 4, 0)


    def Display_Text(self, Font, Color, Location, Text, placement = 'center'):
        text_surf = Font.render(Text, True, Color)
        if placement == 'center':
            text_rect = text_surf.get_frect(center = Location)
        elif placement == 'topleft':
            text_rect = text_surf.get_frect(topleft = Location)
        self.display_surface.blit(text_surf, text_rect)

    def Display_Surf(self, surf, Location):
        rect = surf.get_frect(center = Location)
        self.display_surface.blit(surf, rect)
        return rect

    def Ball_Menu(self):
        self.height = 120 #Maybe Dictonary
        self.Display_Text(self.Title_Font, 'white', (UISIZE['center'], 20), 'Shop')
        for i in range(4):
            if i % 2 == 0:
                UI_ball_rect = self.Display_Surf(self.UI_ball_surfs[f'UI {UIBALLS[i]}'], (UISIZE['center'] - 62.5, self.height))
                self.Display_Text(self.Main_UI_Ball_Name_font, 'white', (UISIZE['center'] - 62.5, self.height - 60), UIBALLS[i])
            else:
                UI_ball_rect = self.Display_Surf(self.UI_ball_surfs[f'UI {UIBALLS[i]}'], (UISIZE['center'] + 62.5, self.height))
                self.Display_Text(self.Main_UI_Ball_Name_font, 'white', (UISIZE['center'] + 62.5, self.height - 60), UIBALLS[i])
                self.height += 125
            self.Ball_Purchase_Hover(UI_ball_rect, UIBALLS[i])
            self.UI_Ball_Click(UI_ball_rect, UIBALLS[i])
            
    def Upgrade_Menu(self): #The Main UI Upgrades
        self.height = 425
        self.Display_Text(self.Title_Font, 'white', (UISIZE['center'], 315), 'Upgrades') #Large Title
        for i in range(4):
            if i % 2 == 0:
                UI_upgrade_rect = self.Display_Surf(self.UI_upgrade_surfs[f'UI {UIUPGRADES[i]}'], (UISIZE['center'] - 62.5, self.height))
                self.Display_Text(self.Main_UI_Ball_Name_font, 'white', (UISIZE['center'] - 62.5, self.height - 60), UIUPGRADES[i])
            else:
                UI_upgrade_rect = self.Display_Surf(self.UI_upgrade_surfs[f'UI {UIUPGRADES[i]}'], (UISIZE['center'] + 62.5, self.height))
                self.Display_Text(self.Main_UI_Ball_Name_font, 'white', (UISIZE['center'] + 62.5, self.height - 60), UIUPGRADES[i])
                self.height += 100 + 25
            self.UI_Upgrade_Click(UI_upgrade_rect, UIUPGRADES[i])

    def UI_Ball_Click(self, UI_Rect, Name):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and UI_Rect.collidepoint(mouse_pos) and not self.clicked:
            self.UI_Ball_Payment(Name)
            #NUMBEROFBALLS[Name] += 1
            #self.Open_Ball_Menu = True
            self.clicked = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

    def UI_Ball_Payment(self, name):
        if self.game.score['player'] >= BALL_COST[name]:
            self.game.score['player'] -= BALL_COST[name]  # Deduct cost
            BALL_COST[name] *= 2  # Increase price
            NUMBEROFBALLS[name] += 1  # Add a new ball

        #if self.game.score >= BALL_COST['Basic Ball']:
        #    self.game.score -= BALL_COST[name]
        #    BALL_COST[name] *= 2   #Increase Price
        #    NUMBEROFBALLS[name] += 1

    def Upgrade_Menu_Background(self, Called_Menu):
        rect = pygame.FRect((0, 0), (UI_WIDTH, 450)).move_to(topright=(WINDOW_WIDTH - UI_WIDTH, (WINDOW_HEIGHT - 450) // 2))
        
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackground'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackgroundborder'], rect, 4, 4)
        #Vertical Line
        pygame.draw.line(self.display_surface, COLORS['UIMenubackgroundborder'],
                        (UI_CENTER, 100 + self.y_offset), (UI_CENTER, WINDOW_HEIGHT - 105 + self.y_offset), 6)
        #Horizontal Lines
        
        def draw_horizontal_line(start_height, increment, num_lines):
            height = start_height
            for i in range(num_lines):
                pygame.draw.line(self.display_surface, COLORS['UIMenubackgroundborder'],
                                (WINDOW_WIDTH - UI_WIDTH * 2, height + self.y_offset), (WINDOW_WIDTH - (UI_WIDTH + 5), height + self.y_offset), 6)
                height += increment
        #First Set
        draw_horizontal_line(100, 0, 1)
        draw_horizontal_line(140, 120, 2)
        #Second Set
        draw_horizontal_line(300, 40, 2)
        draw_horizontal_line(460, 0, 1)
        #Last Line
        height = 225
        for i in range(4):
            offset_x = -UI_WIDTH / 4 if i % 2 == 0 else UI_WIDTH / 4
            Menu_ball_rect = self.Display_Surf(self.UI_ball_surfs[f'UI {UIBALLS[i]}'], (UI_CENTER + offset_x, height))
            self.UI_Single_Upgrade_Click(Menu_ball_rect, UIBALLS[i], Called_Menu)

            if i % 2 != 0:  # Increase height after every second element
                height += 200

    def Speed_Upgrade_Menu(self): #Clean this Code to use the new Functions.
        self.Upgrade_Menu_Background('Speed Menu')

        height = 200  #Starting Height
        for i in range(4):
            offset_x = -UI_WIDTH / 4 if i % 2 == 0 else UI_WIDTH / 4
            ball_name = UIBALLS[i]
            level_text = f"{SPEED_LEVEL[ball_name]} -> {SPEED_LEVEL[ball_name] * 2}" #Double
            cost_text = f'${SPEED_COST[ball_name]}'
            #Text
            self.Display_Text(self.Title_Font, 'black', (UISIZE['center'] - 250, 98), 'Speed')
            self.Display_Text(self.Strength_UI_Menu_Font, 'black', (UI_CENTER + offset_x, height - 52), level_text)
            self.Display_Text(self.Strength_UI_Menu_Font, 'black', (UI_CENTER + offset_x, height + 105), cost_text)

            if i % 2 != 0:  # Increase height after every second element
                height += 200

    def Strength_Upgrade_Menu(self):
        self.Upgrade_Menu_Background('Strength Menu') # 250X400

        height = 200  #Starting Height
        for i in range(4):
            offset_x = -UI_WIDTH / 4 if i % 2 == 0 else UI_WIDTH / 4
            ball_name = UIBALLS[i]
            level_text = f"{STRENGTH_LEVEL[ball_name]} -> {STRENGTH_LEVEL[ball_name] * 2}" #Double
            cost_text = f"${STRENGTH_COST[ball_name]}"
            #Text
            self.Display_Text(self.Title_Font, 'black', (UISIZE['center'] - 250, 98), 'Strength')
            self.Display_Text(self.Strength_UI_Menu_Font, 'black', (UI_CENTER + offset_x, height - 52), level_text)
            self.Display_Text(self.Strength_UI_Menu_Font, 'black', (UI_CENTER + offset_x, height + 105), cost_text)

            if i % 2 != 0:  # Increase height after every second element
                height += 200

    def UI_Single_Upgrade_Click(self, UI_Rect, Name, Called_Menu):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and UI_Rect.collidepoint(mouse_pos) and not self.clicked:
            if Called_Menu == 'Strength Menu':
                if STRENGTH_COST[Name] <= self.game.score['player']:
                    self.game.score['player'] -= STRENGTH_COST[Name] #Takes away the Money/Score
                    STRENGTH_COST[Name] *= 2
                    STRENGTH_LEVEL[Name] *= 2
            if Called_Menu == 'Speed Menu':
                if SPEED_COST[Name] <= self.game.score['player']:
                    self.game.score['player'] -= SPEED_COST[Name] #Takes away the Money/Score
                    SPEED_COST[Name] *= 2
                    SPEED_LEVEL[Name] *= 2
            if Called_Menu == 'Mouse Menu':
                self.game.score['player'] -= STRENGTH_COST[Name]
                STRENGTH_COST[Name] *= 2
                STRENGTH_LEVEL[Name] *= 2
            self.clicked = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

    def UI_Upgrade_Click(self, UI_Rect, Name):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and UI_Rect.collidepoint(mouse_pos) and not self.clicked:
            #UPGRADELEVELS[Name] += 1
            #print(UPGRADELEVELS['Speed'])
            if Name == 'Strength':
                if self.Open_Speed_Menu:
                    self.Open_Speed_Menu = not self.Open_Speed_Menu
                if self.Open_Mouse_Menu:
                    self.Open_Mouse_Menu = not self.Open_Mouse_Menu
                self.Open_Strength_Menu = not self.Open_Strength_Menu
            if Name == 'Speed':
                if self.Open_Strength_Menu:
                    self.Open_Strength_Menu = not self.Open_Strength_Menu
                if self.Open_Mouse_Menu:
                    self.Open_Mouse_Menu = not self.Open_Mouse_Menu
                self.Open_Speed_Menu = not self.Open_Speed_Menu
            if Name == 'Click':
                if self.Open_Strength_Menu:
                    self.Open_Strength_Menu = not self.Open_Strength_Menu
                if self.Open_Speed_Menu:
                    self.Open_Speed_Menu = not self.Open_Speed_Menu
                self.Open_Mouse_Menu = not self.Open_Mouse_Menu
            
            self.clicked = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

    def Ball_Purchase_Hover(self, rect, name):
        mouse_pos = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos):# and name == 'Basic Ball':
            if not self.Open_Strength_Menu and not self.Open_Speed_Menu:
                self.Ball_Purchase_Menu(name)

    def Ball_Purchase_Menu(self, name):
        width = 160
        y_offset = 125 if name == 'Monster Ball' or name == 'Sniper Ball' else 0

        rect = pygame.FRect((0, 0), (width, 180)).move_to(topright=(WINDOW_WIDTH - UI_WIDTH, 50 + y_offset))
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackground'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackgroundborder'], rect, 4, 4)

        def draw_horizontal_line(start_height, increment, num_lines):
            height = start_height
            for i in range(num_lines):
                pygame.draw.line(self.display_surface, COLORS['UIMenubackgroundborder'],
                                ((WINDOW_WIDTH - UI_WIDTH) - width, height + y_offset), (WINDOW_WIDTH - (UI_WIDTH + 5), height + y_offset), 4)
                height += increment
        TITLE = {'Basic Ball': 'Basic Count', 'Speed Ball': 'Speed Count', 'Monster Ball': 'Monster Count', 'Sniper Ball': 'Sniper Count'}

        self.Display_Text(self.Main_UI_Ball_Name_font, 'black', ((WINDOW_WIDTH - UI_WIDTH) - (width / 2), 70 + y_offset), f'{TITLE[name]}')
        self.Display_Text(self.Ball_Count_Font, 'black', ((WINDOW_WIDTH - UI_WIDTH) - (width / 2), 100 + y_offset), f'{NUMBEROFBALLS[name]}')

        #Horizontal Lines
        draw_horizontal_line(125, 25, 4)

        self.Display_Text(self.Strength_UI_Menu_Font, 'black', ((WINDOW_WIDTH - UI_WIDTH) - (width) + 7, 130 + y_offset), f'Cost: ${BALL_COST[name]}', 'topleft')
        self.Display_Text(self.Strength_UI_Menu_Font, 'black', ((WINDOW_WIDTH - UI_WIDTH) - (width) + 7, 155 + y_offset), f'Speed: {SPEED_LEVEL[name]}', 'topleft')
        self.Display_Text(self.Strength_UI_Menu_Font, 'black', ((WINDOW_WIDTH - UI_WIDTH) - (width) + 7, 180 + y_offset), f'Strength: {STRENGTH_LEVEL[name]}', 'topleft')
        self.Display_Text(self.Strength_UI_Menu_Font, 'black', ((WINDOW_WIDTH - UI_WIDTH) - (width) + 7, 205 + y_offset), f'Damage Done: {DAMAGE_DONE[name]}', 'topleft')

    def Mouse_Upgrade_Menu_Background(self, Called_Menu):
        x_extension = 20
        rect = pygame.FRect((0, 0), (UI_WIDTH // 2 + x_extension, 450)).move_to(topright=(WINDOW_WIDTH - UI_WIDTH, (WINDOW_HEIGHT - 450) // 2))
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackground'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackgroundborder'], rect, 4, 4)

        def draw_horizontal_line(start_height, increment, num_lines):
            height = start_height
            for i in range(num_lines):
                pygame.draw.line(self.display_surface, COLORS['UIMenubackgroundborder'],
                                ((WINDOW_WIDTH - UI_WIDTH * 2) + (UI_WIDTH // 2) - x_extension, height + self.y_offset), (WINDOW_WIDTH - (UI_WIDTH + 5), height + self.y_offset), 6)
                height += increment
        draw_horizontal_line(100, 0, 1)
        draw_horizontal_line(140, 0, 1)
        draw_horizontal_line(260, 40, 3)
        draw_horizontal_line(460, 40, 1)

        height = 220
        for i in range(2): #Need Multiple different Mouse Sprites to Upgrade.
            Mouse_rect = self.Display_Surf(self.UI_upgrade_surfs[f'UI {UIUPGRADES[2]}'], (UI_CENTER + (UI_WIDTH // 4) - (x_extension / 2), height))
            self.UI_Single_Upgrade_Click(Mouse_rect, UIUPGRADES[2], Called_Menu)
            height += 200

    def Mouse_Upgrade_Menu(self):
        self.Mouse_Upgrade_Menu_Background('Mouse Menu')
        height = 100

        for i in range(2):
            if i == 0:
                level_text = f"{STRENGTH_LEVEL['Click']} -> {STRENGTH_LEVEL['Click'] * 2}"
                cost_text = f"${STRENGTH_COST['Click']}"
            else:
                level_text = f"{STRENGTH_LEVEL['Click Area']} -> {STRENGTH_LEVEL['Click Area'] * 2}"
                cost_text = f"${STRENGTH_COST['Click Area']}"
            self.Display_Text(self.Title_Font, 'black', (UI_CENTER + (UI_WIDTH // 4) - 10, 98), 'Mouse')
            self.Display_Text(self.Strength_UI_Menu_Font, 'black', (UI_CENTER + (UI_WIDTH // 4) - 10, height + 46), level_text)
            self.Display_Text(self.Strength_UI_Menu_Font, 'black', (UI_CENTER + (UI_WIDTH // 4) - 10, height + 205), cost_text)
            height += 200

    def Prestige_Menu_Background(self):
        rect = pygame.FRect((0, 0), ((UI_WIDTH // 2) + 150, 450)).move_to(topright=(WINDOW_WIDTH - UI_WIDTH, (WINDOW_HEIGHT - 450) // 2))
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackground'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackgroundborder'], rect, 4, 4)

        rect = pygame.FRect((0, 0), (70, 50)).move_to(topright=((WINDOW_WIDTH - UI_WIDTH) - ((UI_WIDTH // 2) + 147), (WINDOW_HEIGHT - 450) // 2))
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackground'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['UIMenubackgroundborder'], rect, 4, 4)

        def draw_horizontal_line(start_height, increment, num_lines):
            height = start_height
            for i in range(num_lines):
                pygame.draw.line(self.display_surface, COLORS['UIMenubackgroundborder'],
                                (((WINDOW_WIDTH - UI_WIDTH) - ((UI_WIDTH // 2) + 150)), height), (WINDOW_WIDTH - (UI_WIDTH + 5), height), 6)
                height += increment
        draw_horizontal_line(200, 0, 1)
        #draw_horizontal_line(140, 0, 1)
        #draw_horizontal_line(260, 40, 3)
        #draw_horizontal_line(460, 40, 1)

    def draw(self):
        self.menu()
        self.Ball_Menu()
        self.Upgrade_Menu()
        if self.Open_Strength_Menu: #make it so only 1 Menu is open at a time.
            self.Strength_Upgrade_Menu()
        if self.Open_Speed_Menu:
            self.Speed_Upgrade_Menu()
        if self.Open_Mouse_Menu:
            self.Mouse_Upgrade_Menu()
        if False:
            self.Prestige_Menu_Background()