#!/usr/bin/python3
# Connor Gray, KJ klamer
# oct 16th 2019

""" maze racer thing """

#-----import statements-----
import time
import turtle as t
import random as rd
from random import randint, choice

#if blue.pos() == agent.pos():
 #   collision.goto(0,0)
  #  collision.showturtle()
   # collision.write("COLLISION")

#-----game configuration----
win = t.Screen()
win.title("Maze Runner")
can = win.getcanvas()
win.bgcolor("black")
path_width = 16
wall_length = path_width
wall = 30






#-----initialize turtle-----

#-----drawers-----
author = t.Turtle()

author.color("Firebrick")
author.hideturtle
author.speed(10)
author.penup()
author.setpos(-45, 350)
author.pendown()
author.write("Maze Runner", False, "center", font=("Ultra", 30, "bold"))

agent = t.Turtle()

agent.color("red")
agent.hideturtle
agent.speed(10)
agent.penup()
agent.setpos(-400, 0)
agent.pendown()

doomguy = t.Turtle()


doomguy.hideturtle
doomguy.color("blue")
doomguy.speed(10)
doomguy.penup()
doomguy.setpos(400, 0)
doomguy.pendown()

#-----runners-----
runner = t.Turtle()
runner.color=('blue')
runner.pencolor('blue')
runner.up()
runner.setpos(-450, 0)
runner.shape("turtle")


arlo = t.Turtle()
arlo.color=('red')
arlo.pencolor('red')
arlo.up()
arlo.setpos(350, 0)
arlo.shape("turtle")

#-----finish lines--------
runfinish = t.Turtle()
runfinish.hideturtle
runfinish.color=("white")
runfinish.pencolor("white")
runfinish.penup()
runfinish.setpos(-400, -250)
runfinish.pendown()
#-----game functions--------
def go_up():
    runner.setheading(90)
def go_down():
    runner.setheading(270)
def go_left():
    runner.setheading(180)
def go_right():
    runner.setheading(0)
def go_forward():
    runner.forward(5)
    x = runner.xcor()
    y = runner.ycor()
    x1 = x + 4
    y1 = -(y+4)
    x2 = x - 4
    y2 = -(y-4)   
    overlap = can.find_overlapping(x1,y1,x2,y2)
    print(overlap)
    if len(overlap)>1:
        runner.setpos(-450, 0)
        #runner.write(0,0,"COLLISION")
def go_fast():
    runner.speed(10)    
def go_slow():
    runner.speed(1)

def go_upp():
    arlo.setheading(90)
def go_downn():
    arlo.setheading(270)
def go_leftt():
    arlo.setheading(180)
def go_rightt():
    arlo.setheading(0)
def go_forwardd():
    arlo.forward(5)
    x_ = arlo.xcor()
    y_ = arlo.ycor()
    x1_ = x_ + 2
    y1_ = -(y_+2)
    x2_ = x_ - 2
    y2_ = -(y_-2)   
    overlap = can.find_overlapping(x1_,y1_,x2_,y2_)
    print(overlap)
    if len(overlap)>1:
        arlo.setpos(350, 0)    
def go_fastt():
    arlo.speed(10)    
def go_sloww():
    arlo.speed(1)    
    
def draw_door(spot, length):
    '''draw door in wall'''
    agent.pendown()
def draw_barrier (spot, length):
    agent.pendown()
    
def draw_door(spot, length):
    '''draw door in wall'''
    doomguy.pendown()
def draw_barrier (spot, length):
    doomguy.pendown()    
#create door 'door_spot' pixels from start of wall.

#Finish line

runfinish.pendown()
runfinish.fd(260)
runfinish.left(90)
runfinish.fd(550)
runfinish.left(90)
runfinish.fd(560)
runfinish.left(90)
runfinish.fd(550)
runfinish.left(90)
runfinish.fd(300)
runfinish.fd(260)
runfinish.left(90)
runfinish.fd(550)
runfinish.left(90)
runfinish.fd(560)
runfinish.left(90)
runfinish.fd(550)
runfinish.left(90)
runfinish.fd(300)
runfinish.fd(260)
runfinish.left(90)
runfinish.fd(550)
runfinish.left(90)
runfinish.fd(560)
runfinish.left(90)
runfinish.fd(550)
runfinish.left(90)
runfinish.fd(300)
runfinish.hideturtle()
for i in range(1, wall+1):
    wall_length += path_width
    
    if i <= 4:
        agent.penup()
        agent.left(90)
        agent.forward(wall_length)
    
    else:
       door = rd.randrange(path_width*2, wall_length - (path_width*2)+1, path_width*2)
       barrier = rd.randrange(path_width*2, wall_length - (path_width*2)+1, path_width*2)
       
       agent.pendown()
       agent.left(90)
       
       agent.forward(door)
       agent.penup()
       agent.forward(path_width*2)
       agent.pendown()  
       
       agent.forward(wall_length - (door + path_width))
       agent.penup()
       agent.backward(wall_length)
       
       
       agent.forward(barrier)
       agent.pendown()
       agent.left(90)
       agent.forward(path_width*2)
       agent.backward(path_width*2)
       agent.right(90)
       agent.penup()
       agent.forward(wall_length - barrier)
       
       draw_door(door,wall_length)  
       
       draw_barrier(barrier,wall_length)  
       
       
#turtle 2 stuff

    if i <= 4:
        doomguy.penup()
        doomguy.left(90)
        doomguy.forward(wall_length)
    
    else:
       door = rd.randrange(path_width*2, wall_length - (path_width*2)+1, path_width*2)
       barrier = rd.randrange(path_width*2, wall_length - (path_width*2)+1, path_width*2)
       
       doomguy.pendown()
       doomguy.left(90)
       
       doomguy.forward(door)
       doomguy.penup()
       doomguy.forward(path_width*2)
       doomguy.pendown()  
       
       doomguy.forward(wall_length - (door + path_width))
       doomguy.penup()
       doomguy.backward(wall_length)
       
       
       doomguy.forward(barrier)
       doomguy.pendown()
       doomguy.left(90)
       doomguy.forward(path_width*2)
       doomguy.backward(path_width*2)
       doomguy.right(90)
       doomguy.penup()
       doomguy.forward(wall_length - barrier)
       
       draw_door(door,wall_length)  
       
       draw_barrier(barrier,wall_length)  
       
       




    

#-----events----------------


win.onkeypress(go_up, 'Up')
win.onkeypress(go_down, 'Down')
win.onkeypress(go_left, 'Left')
win.onkeypress(go_right, 'Right')
win.onkeypress(go_forward,'0')
win.onkeypress(go_fast, "1")
win.onkeypress(go_slow, "2")

win.onkeypress(go_upp, 'w')
win.onkeypress(go_downn, 's')
win.onkeypress(go_leftt, 'a')
win.onkeypress(go_rightt, 'd')
win.onkeypress(go_forwardd, 'space')
win.onkeypress(go_fastt, "c")
win.onkeypress(go_sloww, "b")

win.listen()
timer = 30

def countdown():
    global timer

    timer -= 1

    if timer <= 0:  # time is up, disable user control
        win.onkey(None, 'Left')
        win.onkey(None, 'Right')
        win.onkey(None, 'Up')
        win.onkey(None, 'Down')
    else:
        win.ontimer(countdown, 1000)  # one second from now

win.ontimer(countdown, 1000)
win.mainloop()