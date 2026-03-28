import pgzrun, random, pyautogui
WIDTH, HEIGHT=pyautogui.size()
TITLE= "str"
score=0
life=3
mo=[]
gamestate="start"
music.play("monkispinmonki.mp3")
#kevmac
STR=Actor("star.png")
STR.scale=0.5
STR.pos= WIDTH-100, HEIGHT-100
element=["meteorite", "spaceship", "sun"]
def create_elements():
    if gamestate=="play":
        A=Actor(random.choice(element))
        A.pos= 0, random.randint(0, HEIGHT)
        mo.append(A)
def draw():
    screen.blit("space.jpg", (0, 0))
    STR.draw()
    if gamestate=="start":
        message="Press space to start \n Control the star with up & down arrow keys \n Collect meteorites and suns, avoid spaceships \n You have 3 lives \n If you touch trash, you lose a life"
        screen.draw.text(message, center=(WIDTH//2, HEIGHT//2))
    elif gamestate=="play":
        screen.draw.text("Score:"+str(score), (50, 50))
        screen.draw.text("Life:"+str(life), (50, 70))
        for i in mo:
            i.draw()
    else:
        message="GAME OVER"
        screen.draw.text(message, center=(WIDTH//2, HEIGHT//2, fontsize=40))

def update():
    global score, life, gamestate
    if gamestate=="play":
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
                if i.image=="meteorite":
                    sound.bloxysplat.play
                    score+=5
                elif i.image=="sun":
                    sound.kaboom.play
                    #universfield
                    score+=10
                elif i.image=="spaceship":
                    sound.frostedow.play
                    #Frosted_52
                    life-=1
                mo.remove(i)
        if life==0:
            gamestate="end"


clock.schedule_interval(create_elements, 2)
pgzrun.go()