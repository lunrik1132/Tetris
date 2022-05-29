from pygame import *
import time as tm
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_x, player_speed_y, move_keys):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.move_keys = move_keys
        self.alive = True
        self.downtiming = tm.time()
        self.movetiming = tm.time()

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def move(self):
        global fast_down
        keys = key.get_pressed()
        if keys[self.move_keys[0]] and self.rect.x > 0 and self.alive == True:
            if tm.time() - self.movetiming > 0.3:
                self.movetiming = tm.time()
                self.rect.x -= self.speed_x

        if keys[self.move_keys[1]] and self.rect.x < 225 and self.alive == True:
            if tm.time() - self.movetiming > 0.3:
                self.movetiming = tm.time()
                self.rect.x += self.speed_x

        if keys[self.move_keys[2]] and self.rect.y != height_limit and self.alive == True:
            fast_down = True
            if tm.time() - self.movetiming > 0.1:
                self.movetiming = tm.time()
                self.rect.y += self.speed_y
        else:
            fast_down = False

        if tm.time() - self.downtiming > game_speed and self.alive == True and fast_down == False:
            self.downtiming = tm.time()
            self.rect.y += self.speed_y

    def count(self):
        for b in blocks:
            if b.rect.y == 475:
                if not b in clear_list:
                    clear_list.append(b)
    
    def clear(self):
        if len(clear_list) == 10:
            for c in clear_list:
                c.kill()
                cleared_list.append(c)
        if len(cleared_list) == 10:
            for c in cleared_list:
                if c in clear_list:
                    clear_list.remove(c)

    def dead(self):
        global alive_blocks, block1, block2, block3, block4
        if self.rect.y >= height_limit:
            for b in alive_blocks:
                blocks.add(b)
                b.alive = False
            alive_blocks.clear()

            set_block()
            alive_blocks = [block1, block2, block3, block4]

        
        for b in blocks:
            if self.rect.y == b.rect.y - 25 and self.rect.x == b.rect.x:
                for b in alive_blocks:
                    blocks.add(b)
                    b.alive = False
                alive_blocks.clear()

                set_block()
                alive_blocks = [block1, block2, block3, block4]

def set_block():
    global block1, block2, block3, block4
    if tm.time() - setform_time > 0.1:
        block_color = choice(colors)
        block_form = 1
        if block_form == 1: #лінія
            block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
            block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
            block3 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)
            block4 = Player(block_color, 100, 100, 25, 25, 25, 25, movekeys)
        if block_form == 2: #квадрат
            block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
            block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
            block3 = Player(block_color, 125, 25, 25, 25, 25, 25, movekeys)
            block4 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
        if block_form == 3: #зигзаг1
            block1 = Player(block_color, 125, 25, 25, 25, 25, 25, movekeys)
            block2 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
            block3 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
            block4 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)
        if block_form == 4: #зигзаг2
            block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
            block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
            block3 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
            block4 = Player(block_color, 125, 75, 25, 25, 25, 25, movekeys)
        if block_form == 5: #трикутник
            block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
            block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
            block3 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
            block4 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)
        if block_form == 6: #кут 90 градусів1
            block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
            block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
            block3 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)
            block4 = Player(block_color, 125, 75, 25, 25, 25, 25, movekeys)
        if block_form == 7: #кут 90 градусів2
            block1 = Player(block_color, 125, 25, 25, 25, 25, 25, movekeys)
            block2 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
            block3 = Player(block_color, 125, 75, 25, 25, 25, 25, movekeys)
            block4 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)

img_redblock = 'redblock.png'
img_blueblock = 'blueblock.png'
img_greenblock = 'greenblock.png'
movekeys = [K_a, K_d, K_s]
setform_time = tm.time()

forms = [1,2,3,4,5,6,7]
colors = [img_redblock, img_blueblock, img_greenblock]

height_limit = 475
win_width = 250
win_height = 500
display.set_caption("Pin-pong")
window = display.set_mode((win_width, win_height))

clock = time.Clock()
fps = 60
game_speed = 0.3
fast_down = False

set_block()
alive_blocks = [block1, block2, block3, block4]
blocks = sprite.Group()

clear_list = []
cleared_list = []

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    if not finish:
        dt = clock.tick(fps)
        
        draw.rect(window, (200,255,255), Rect(0, 0, win_width, win_height))
        
        for b in alive_blocks:
            b.move()
            b.count()
            b.clear()
            b.dead()
            b.reset()

        blocks.draw(window)

        display.update()