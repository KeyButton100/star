import pgzrun, random, pyautogui
WIDTH, HEIGHT=pyautogui.size()
TITLE= "str"

STR=Actor("star.png")
STR.pos= WIDTH-100, HEIGHT-100
def draw():
    screen.clear()
    screen.blit("space.jpg", (0, 0))
    STR.draw()

def update():
    if keyboard.down:
        STR.y=STR.y+10
    if keyboard.up:
        STR.y=STR.y-10
    if STR.y<0:
        STR.y=WIDTH
    elif STR.y>WIDTH:
        STR.y=0
pgzrun.go()