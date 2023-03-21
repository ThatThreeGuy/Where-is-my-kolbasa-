from ding_dong_props import *


clock = time.Clock()


game = True
game_over = False

bg = transform.scale(image.load('xd.png'), WNDS_SIZE)
ball_s = transform.scale(image.load('squigglebob.png'), (50, 50))

left = stick('kanye_gaming.jpg', 2, 0, WNDS_SIZE[1] / 2)
right = stick('kanye_gaming.jpg', 2, WNDS_SIZE[0] - SPR_SIZE[0], WNDS_SIZE[1] / 2)
ball = gamesprite('squigglebob.png', 2, 250, 250)
ball.image = ball_s
while game:
    for ev in event.get():
        if ev.type == QUIT:
            game = False
    
    if not game_over:
        wnd.blit(bg, (0,0))
        left.update_pos('left')
        right.update_pos('right')
        ball.move(left, right)
        left.render()
        right.render()
        ball.render()
    
    clock.tick(60)
    display.update()