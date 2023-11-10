from pygame import *
from random import randint
from time import time as timer

img_back = 'background.jpg'
img_racket = 'racket.png'
img_ball = 'tenis_ball.png'

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    


#создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
racket_1 = Player(img_racket,30,200,50,150,10)
racket_2 = Player(img_racket,620,200,50,150,10)
ball = GameSprite(img_ball,350,200,49,49,10)
ball_speed_x = 6
ball_speed_y = 6

#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background,(0,0))

    if ball.rect.y >= win_height -50 or ball.rect.y <= 0:
        ball_speed_y *= -1
    if sprite.collide_rect(racket_1,ball) or sprite.collide_rect(racket_2,ball):
        ball_speed_x *= -1

    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y

    racket_1.update_1()
    racket_2.update_2()
    racket_1.reset()
    racket_2.reset()
    ball.reset()

    if ball.rect.x < 0 or ball.rect.x > win_width - 50:
        break

    display.update()
    time.delay(30)
if ball.rect.x > 100:
    print('player 1 win')
else:
    print('player 2 win')