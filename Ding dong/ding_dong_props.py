from pygame import *
from random import randint as rand

wnd = display.set_mode((700, 500))
display.set_caption('ding dong')

winner = None


WNDS_SIZE = (700, 500)
SPR_SIZE = (40, 130)


class gamesprite(sprite.Sprite):
    def __init__(self, image_name, speed, pos_x, pos_y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), SPR_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        ###Чисто для мяча
        self.speed_x = speed
        self.speed_y = speed
    def render(self):
        wnd.blit(self.image, (self.rect.x, self.rect.y))
    def move(self, left, right):
        global winner
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y >= WNDS_SIZE[1] - 50 or self.rect.y <= 0:
            self.speed_y *= -1

        if Rect.colliderect(self.rect, left.rect) or Rect.colliderect(self.rect, right.rect):
            self.speed_x *= -1


        if self.rect.x >= WNDS_SIZE[0] - 50:
            winner = 1
        if self.rect.x <= 0:
            winner = 2


class stick(gamesprite):
    def update_pos(self, who):
        keys = key.get_pressed()
        if who == 'right':
            if keys[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed_y
            if keys[K_DOWN] and self.rect.y < WNDS_SIZE[1]:
                self.rect.y += self.speed_y
        if who == 'left':
            if keys[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed_y
            if keys[K_s] and self.rect.y < WNDS_SIZE[1]:
                self.rect.y += self.speed_y
