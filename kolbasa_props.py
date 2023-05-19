from pygame import *
from time import sleep as sl
from time import time as tm
from random import randint as rint

font.init()
mixer.init()

WND_SIZE = (700, 500)
PLR_SIZE = (250, 300)#(70, 90)
GRAY = (125, 125, 125)
wnd = display.set_mode(WND_SIZE)
clock = time.Clock()
display.set_caption('Where is my Kolbasa?!')
game = True
gamemode = 'basic'
shotgun_reload_time = 0


### кд
interval = 0.7
start = 0

### Очень специфичные 
tutorial_missed_shots = 0

plr_walk_props_left = [transform.scale(image.load('walk1_left.png'), PLR_SIZE), 
transform.scale(image.load('walk2_left.png'), PLR_SIZE), 
transform.scale(image.load('walk3_left.png'), PLR_SIZE)]

plr_walk_props_right = [transform.scale(image.load('walk1_right.png'), PLR_SIZE), 
transform.scale(image.load('walk2_right.png'), PLR_SIZE), 
transform.scale(image.load('walk3_right.png'), PLR_SIZE)]

shotguns_anims = [transform.scale(image.load('shotgun_first_person.png'), (300, 150)), 
transform.scale(image.load('shotgun_first_person_recoil.png'), (300, 150))]

plr_stand = transform.scale(image.load('mc_stand.png'), PLR_SIZE)
plr_stand_back = transform.scale(image.load('mc_stand_back.png'), PLR_SIZE)
dorozh_znak_when_invinc = None
lightning_strikes = [transform.scale(image.load('lightning1.png'), (65,65)),transform.scale(image.load('lightning2.png'), (65,65)),transform.scale(image.load('lightning3.png'), (65,65))]

def dorozh_znak_invinc():
    dorozh_znak_when_invinc = list()
    for i in range(10):
        e = rint(1, 15)
        if e not in dorozh_znak_when_invinc:
            dorozh_znak_when_invinc.append(e)
    return dorozh_znak_when_invinc

dorozh_znak_when_invinc = dorozh_znak_invinc()
    



class basicsprite(sprite.Sprite):
    def __init__(self, image_name, pos_x, pos_y, size):
        super().__init__()
        self.image = transform.scale(image.load(image_name), size)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        ### В основном только для ентера
        self.is_on_screen = False
    def render(self):
        wnd.blit(self.image, (self.rect.x, self.rect.y))
    def collpoint(self, x, y):
        return self.rect.collidepoint(x,y)

class player(basicsprite):
    def __init__(self, image_name, pos_x, pos_y, size):
        super().__init__(image_name, pos_x, pos_y, size)
        self.was_anim = None ###Для анимации ходьбы
        self.speed = 5
        self.cd_change_walk = 0
        self.moved = False
        self.talk = 1 #1
        self.level_on = 0 # 0
        self.no_shotgun = False
        self.is_dead = False
    def control(self):
        keys = key.get_pressed()

        if keys[K_LEFT]:
            self.rect.x -= self.speed
            if self.cd_change_walk == 0:
                if self.image == plr_walk_props_left[1] or self.image == plr_walk_props_left[2]:
                    self.image = plr_walk_props_left[0]
                    self.cd_change_walk = 5
                elif self.was_anim == 'walk3_left':
                    self.image = plr_walk_props_left[1]
                    self.was_anim = 'walk2_left'
                    self.cd_change_walk = 5
                elif self.was_anim == 'walk2_left':
                    self.image = plr_walk_props_left[2]
                    self.was_anim = 'walk3_left'
                    self.cd_change_walk = 5

                else:
                    self.image = plr_walk_props_left[1]
                    self.was_anim = 'walk2_left'
                    self.cd_change_walk = 5
            else:
                self.cd_change_walk -= 1
            self.moved = True
        if keys[K_RIGHT]:
            self.rect.x += self.speed
            if self.cd_change_walk == 0:
                if self.image == plr_walk_props_right[1] or self.image == plr_walk_props_right[2]:
                    self.image = plr_walk_props_right[0]
                    self.cd_change_walk = 5
                elif self.was_anim == 'walk3_right':
                    self.image = plr_walk_props_right[1]
                    self.was_anim = 'walk2_right'
                    self.cd_change_walk = 5
                elif self.was_anim == 'walk2_right':
                    self.image = plr_walk_props_right[2]
                    self.was_anim = 'walk3_right'
                    self.cd_change_walk = 5

                else:
                    self.image = plr_walk_props_right[1]
                    self.was_anim = 'walk2_right'
                    self.cd_change_walk = 5
            else:
                self.cd_change_walk -= 1
            self.moved = True
        if not keys[K_RIGHT] and not keys[K_LEFT]:
            self.image = plr_stand
    def size_change(self, size):
        global plr_walk_props_left, plr_walk_props_right, plr_stand, plr_stand_back
        plr_walk_props_left = [transform.scale(image.load('walk1_left.png'), size), 
        transform.scale(image.load('walk2_left.png'), size), 
        transform.scale(image.load('walk3_left.png'), size)]

        plr_walk_props_right = [transform.scale(image.load('walk1_right.png'), size), 
        transform.scale(image.load('walk2_right.png'), size), 
        transform.scale(image.load('walk3_right.png'), size)]

        plr_stand = transform.scale(image.load('mc_stand.png'), size)

        plr_stand_back = transform.scale(image.load('mc_stand_back.png'), size)

class enm(basicsprite):
    def __init__(self, image_name, pos_x, pos_y, size, hp):
        super().__init__(image_name, pos_x, pos_y, size)
        self.hp = hp
        self.max_hp = hp
        self.phase = 1
        self.cd_change_pos = 0
        self.cd_change_pos_var = 75


class lightning(basicsprite):
    def __init__(self, image_name, pos_x, pos_y, size, speed_on_strike):
        super().__init__(image_name, pos_x, pos_y, size)
        self.strike_cd = speed_on_strike ### cd на поинт єнд кликах и скорость на длинных
        self.full_strike_cd = speed_on_strike
        self.set_up = False
    def strike_setup(self, x, y, distance = -35):
        self.rect.x = x
        self.rect.y = y + distance
        self.set_up = True
    def strike(self, lightning_costumes, hand_rect, sound): ### Для тех который спавнятся на руке
        plr_dead = 'shotgun'
        self.strike_cd -= 1
        if self.strike_cd == 0:
            if self.image != lightning_costumes[2]:
                self.image = lightning_costumes[(lightning_costumes.index(self.image) + 1)]
            elif self.image == lightning_costumes[2]:
                print('here')
                if Rect.colliderect(self.rect, hand_rect):
                    plr_dead = 'dead'
                self.set_up = False
                self.image = lightning_costumes[0]
                self.full_strike_cd -= 1
            
            self.strike_cd = self.full_strike_cd
        return plr_dead
    def strike_lengthy_horiz(self, hand_rect, sound):
        plr_dead = 'shotgun'

        if self.rect.x <= WND_SIZE[0]:
            self.rect.x += self.strike_cd
            if Rect.colliderect(self.rect, hand_rect):
                plr_dead = 'dead'
        elif self.rect.x >= WND_SIZE[0]:
            self.set_up = False
            self.strike_cd += 0.5
            

        return plr_dead