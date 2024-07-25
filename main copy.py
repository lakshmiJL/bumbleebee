import pgzrun
from random import randint


WIDTH = 500
HEIGHT = 500

bee = Actor("bee.png")
bee.w = 10
bee.pos = (100, 50)
flower = Actor("flower.png")
flower.pos = (100, 200)

score = 0
game_over = False

def draw():
        if game_over == False:
                screen.blit("background.png", (0, 0))
                bee.draw()
                flower.draw()
                screen.draw.text(f"score is {score}",
                                midtop=(WIDTH / 2, 10),
                                fontsize=20,
                                color="red")
        else:
                screen.fill("red")
                screen.draw.text(f"Time up your final score is {score}",
                                midtop=(WIDTH / 2, 10),
                                fontsize=20,
                                color="white")


def place_flower():
    flower.x = randint(55, WIDTH - 55)
    flower.y = randint(55, HEIGHT - 55)

def update():
        global score
        if keyboard.a:
                bee.x -= 5
        if keyboard.d:
                bee.x += 5
        if keyboard.w:
                bee.y -= 5
        if keyboard.s:
                bee.y += 5
        if bee.colliderect(flower):
             place_flower() 
             score += 1  

def time_up():
        global game_over
        game_over = True

clock.schedule(time_up, 60)
pgzrun.go()