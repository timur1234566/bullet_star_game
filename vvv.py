import pygame
import hero_class
import enemy_class
from bullet_hero import Bullet

pygame.init()  # предварительный запуск зависимостей
clock = pygame.time.Clock()  # создание экземпляра класса слок
GREEN = (0, 255, 0)  # задаём цвета для ужобной работы
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen_size = wight, height = 800, 800  # задаём ширину высоту для удобной работы
screen = pygame.display.set_mode(screen_size)  # задаём размер экрана
pygame.display.set_caption('Моя игра')  # название окна

hero1 = hero_class.Player(wight, height) # создание экземпляра класса
hero2 = hero_class.Player(
    wight, height, 2, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, size_image=0.09
)

all_enemy = pygame.sprite.Group()
for i in range(3): # создать 10 врагов
    mob = enemy_class.Enemy(wight, height)
    all_enemy.add(mob)


running = True  # игровой цикл

while running:  # запуск игрового цикла
    if len(all_enemy) < 3:  # если врагов меньше 10 , то создать новый эеземпляр класса врага
            mob = enemy_class.Enemy(wight, height)
            all_enemy.add(mob)
    screen.fill(BLACK)
    clock.tick(60)  # устанавливаем количество игровыйх фреймов в секунду ( повторений while)
    for event in pygame.event.get():  # перебераем все события
        if event.type == pygame.QUIT:  # если нажали на крестик
            running = False

    hero1.update() # обновление расположения коробля
    hero2.update()
    # отрисовка врагов
    all_enemy.update()
    all_enemy.draw(screen)

    hero1.all_bullet.update()
    hero2.all_bullet.update()
    hero1.all_bullet.draw(screen)
    hero2.all_bullet.draw(screen)

    if pygame.sprite.spritecollide(hero1, all_enemy, False): #остоновка програмы если спрайты столкнулись
        running = False
    if pygame.sprite.groupcollide(all_enemy, hero1.all_bullet, True, True):
        pass
    if pygame.sprite.groupcollide(all_enemy, hero2.all_bullet, True, True):
        pass

    # if pygame.sprite.spritecollide(hero2, all_enemy, False):
    #     running = False

    screen.blit(hero1.image, hero1.rect) # отрисовка кораблика
    screen.blit(hero2.image, hero2.rect)  # отрисовка кораблика
    pygame.display.update()  # обновляем наш дисплей

pygame.quit()  # завершаем все зависимости pygame