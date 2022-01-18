from turtle import *

color('#80B54A')
bgcolor('#15202B')
speed(200)
hideturtle()
penup()
goto( 0, -150)
pendown()

b = 0
while b < 200:
        left(b)
        forward(b * 3)
        b = b + 1
input()
