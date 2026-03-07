import pgzrun, random, pyautogui
WIDTH, HEIGHT=pyautogui.size()
TITLE= "str"

mo=[]
STR=Actor("star.png")
STR.scale=0.5
STR.pos= WIDTH-100, HEIGHT-100
element=["money", "banpeel", "coin"]
def create_elements():
    A=Actor(random.choice(element))
    y=random.randint(0, HEIGHT-50)
    A.pos= 0, y
    mo.append(A)
def draw():
    screen.clear()
    screen.blit("space.jpg", (0, 0))
    STR.draw()
    for i in mo:
        i.draw()

def update():
    if keyboard.down:
        STR.y=STR.y+10
    if keyboard.up:
        STR.y=STR.y-10
    if STR.y<0:
        STR.y=WIDTH
    elif STR.y>WIDTH:
        STR.y=0
    for i in mo:
        i.x+=10
        if i.colliderect(STR):
            mo.remove(i)
clock.schedule_interval(create_elements, 2)
pgzrun.go()