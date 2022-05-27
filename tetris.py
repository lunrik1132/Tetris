from pygame import *
import time as tm

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
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def move(self):
        global movetiming, fast_down
        keys = key.get_pressed()
        if keys[self.move_keys[0]] and self.rect.x > 0 and self.alive == True:
            if tm.time() - movetiming > 0.3:
                movetiming = tm.time()
                self.rect.x -= self.speed_x

        if keys[self.move_keys[1]] and self.rect.x < 225 and self.alive == True:
            if tm.time() - movetiming > 0.3:
                movetiming = tm.time()
                self.rect.x += self.speed_x

        if keys[self.move_keys[2]] and player.rect.y != height_limit and self.alive == True:
            fast_down = True
            if tm.time() - movetiming > 0.1:
                movetiming = tm.time()
                self.rect.y += self.speed_y
        else:
            fast_down = False

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


img_redblock = 'redblock.png'
img_blueblock = 'blueblock.png'
img_greenblock = 'greenblock.png'
movekeys = [K_a, K_d, K_s]

height_limit = 475
win_width = 250
win_height = 500
display.set_caption("Pin-pong")
window = display.set_mode((win_width, win_height))

clock = time.Clock()
fps = 60
movetiming = tm.time()
downtiming = tm.time()
game_speed = 0.3
fast_down = False

player = Player(img_redblock, 100, 25, 25, 25, 25, 25, movekeys)

blocks = sprite.Group()
blocks.add(player)
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

        player.count()
        player.move()
        player.clear()
        player.reset()
        blocks.draw(window)

        if tm.time() - downtiming > game_speed and player.alive == True and fast_down == False:
            downtiming = tm.time()
            player.rect.y += player.speed_y
        
        if player.rect.y >= height_limit:
            player.alive = False
            player.rect.y = height_limit
            
            player = Player(img_redblock, 125, 25, 25, 25, 25, 25, movekeys)
            blocks.add(player)
        else:
            player.alive = True


        for b in blocks:
            if player.rect.y == b.rect.y - 25 and player.rect.x == b.rect.x:
                player.alive = False
                player.rect.y = b.rect.y - 25

                player = Player(img_redblock, 125, 25, 25, 25, 25, 25, movekeys)
                blocks.add(player)
                print(clear_list)
                print(len(clear_list))


        display.update()