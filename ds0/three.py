from turtle import *

def carre(cote,x,y):
    up()
    goto(x,y)
    down()
    angle=90
    i=0
    while i<4:
        forward(cote)
        left(angle)
        i=i+1


nb = int(input('nb carrés: '))
cote = int(input('longueur côté: '))

x = -350
y = 300

for i in range(nb):
    carre(cote, x, y)
    x += cote
    y += cote


