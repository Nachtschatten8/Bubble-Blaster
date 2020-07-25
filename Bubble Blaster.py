#Bubble Blaster
from tkinter import *
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title("Bubble Blaster")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg="blue")
c.pack()
schiff_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill="red")
schiff_id2 = c.create_oval(0, 0, 30, 30, outline="red")
SCHIFF_R = 15
MID_X = WIDTH / 2
MID_Y= HEIGHT / 2
c.move(schiff_id, MID_X, MID_Y)
c.move(schiff_id2, MID_X, MID_Y)
SCHIFF_GESCHW = 10
def schiff_beweg(event):
    if event.keysym == "Up":
        c.move(schiff_id, 0, -SCHIFF_GESCHW)
        c.move(schiff_id2, 0, -SCHIFF_GESCHW)
    elif event.keysym == "Down":
        c.move(schiff_id, 0, SCHIFF_GESCHW)
        c.move(schiff_id2, 0, SCHIFF_GESCHW)
    elif event.keysym == "Left":
        c.move(schiff_id, -SCHIFF_GESCHW, 0)
        c.move(schiff_id2, -SCHIFF_GESCHW, 0)
    elif event.keysym == "Right":
        c.move(schiff_id, SCHIFF_GESCHW, 0)
        c.move(schiff_id2, SCHIFF_GESCHW, 0)
c.bind_all("<Key>", schiff_beweg)
from random import randint
bub_id = list()
bub_r = list()
bub_geschw = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_GESCHW = 10
GAP = 100
def erstelle_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x-r, y-r, x+r, y+r, outline="white")
    bub_id.append(id1)
    bub_r.append(r)
    bub_geschw.append(randint(1, MAX_BUB_GESCHW))
def bewege_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_geschw[i], 0)


def hole_koord(id_num):
    pos = c.coords(id_num)
    x = (pos[0] +  pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y
def lösche_bubble(i):
    del bub_r[i]
    del bub_geschw[i]
    c.delete(bub_id[i])
    del bub_id[i]
def entf_bubbles():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = hole_koord(bub_id[i])
        if x < -GAP:
            lösche_bubble(i)

from math import sqrt
def distanz(id1, id2):
    x1, y1 = hole_koord(id1)
    x2, y2 = hole_koord(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
def kollision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distanz(schiff_id2, bub_id[bub]) < (SCHIFF_R + bub_r[bub]):
            points += (bub_r[bub] + bub_geschw[bub])
            lösche_bubble(bub)
    return points

c.create_text(50, 30, text="ZEIT", fill="white")
c.create_text(150, 30, text="PUNKTE", fill="white")
time_text = c.create_text(50,50, fill="white")
score_text = c.create_text(150,50, fill="white")

def zeige_punkte(score):
    c.itemconfig(score_text, text=str(score))

def zeige_zeit(time_left):
    c.itemconfig(time_text, text=str(time_left))

from time import sleep, time
BUB_CHANCE = 10
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
ende = time() + TIME_LIMIT

#HAUPTSCHLEIFE

while time() < ende:
    if randint(1, BUB_CHANCE) == 1:
        erstelle_bubble()
    bewege_bubbles()
    entf_bubbles()
    score += kollision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        ende += TIME_LIMIT

    zeige_punkte(score)
    zeige_zeit(int(ende - time()))
    #print(score)
    
    window.update()
    sleep(0.01)
c.create_text(MID_X, MID_Y, \
    text="GAME OVER", fill="black", font=("Helvetica",30))
c.create_text(MID_X, MID_Y+30, \
    text="Punkte: "+ str(score), fill="black")
c.create_text(MID_X, MID_Y+45, \
    text="Bonus-Zeit: "+ str(bonus*TIME_LIMIT), fill="black")




            
    
