import pgzrun, random, pyautogui
WIDTH, HEIGHT=pyautogui.size()
TITLE= "str"

score=0
life=3
mo=[]
gamestate="start"

STR=Actor("star.png")
STR.scale=0.5
STR.pos= WIDTH-100, HEIGHT-100
element=["money", "banpeel", "coin"]
def create_elements():
    A=Actor(random.choice(element))
    A.pos= 0, random.randint(0, HEIGHT)
    mo.append(A)
def draw():
    screen.blit("space.jpg", (0, 0))
    STR.draw()
    if gamestate=="start":
        message="Press space to start \n Control the star with up & down arrow keys \n Collect money, avoid trash \n You have 3 lives \n If you touch trash, you lose a life"
        screen.draw.text(message, center=(WIDTH//2, HEIGHT//2))

    screen.draw.text("Score:"+str(score), (50, 50))
    screen.draw.text("Life:"+str(life), (50, 70))
    for i in mo:
        i.draw()

def update():
    global score, life, gamestate
    if keyboard.up:
        STR.y=STR.y-10
    if keyboard.down:
        STR.y=STR.y+10
    if STR.y<0:
        STR.y=WIDTH
    elif STR.y>WIDTH:
        STR.x=0
    for i in mo:
        i.x+=10
        if i.colliderect(STR):
            if i.image=="money":
                score+=5
            elif i.image=="coin":
                score+=10
            elif i.image=="banpeel":
                life-=1
            mo.remove(i)
    if life==0:
        gamestate="end"
clock.schedule_interval(create_elements, 2)
pgzrun.go()
clock.schedule_interval(create_elements, 2)
pgzrun.go()