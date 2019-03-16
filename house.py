import turtle
import random
t = turtle.Turtle()
t.up()
t.speed(30)

LightBlueR = 44
LightBlueG = 178
LightBlueB = 178

MidiumRedR = 193
MediumRedG = 49
MediumRedB = 17

GreenR = 6
GreenG = 165
GreenB = 46

t.color(LightBlueR, LightBlueG, LightBlueB)
t.home() #set to (0,0)
t.down()

#create box for home.
t.begin_fill()
for i in range (4):
  t.forward(100)
  t.rt(90)
t.end_fill()

t.up() #don't draw

t.goto(40, -100)
t.down()
t.color(MidiumRedR, MediumRedG, MediumRedB)

t.begin_fill()
for i in range(2):
  t.forward(25)
  t.lt(90)
  t.forward(50)
  t.lt(90)
t.end_fill()


#windows
t.up()
t.goto(10, -10)
t.down()
t.color(GreenR, GreenG, GreenB)
t.begin_fill()
for i in range(4):
  t.forward(20)
  t.rt(90)
t.end_fill()


t.color(0,0,0) #fill in windows
for i in range(4):
  t.forward(20)
  t.rt(90)
t.up()
t.goto(10, -20)
t.down()
t.forward(20)
t.up()
t.goto(20, -10)
t.rt(90)
t.down()
t.forward(20)
t.setheading(0)


#right window
t.up()
t.goto(70,-10)
t.down()
t.color(GreenR, GreenG, GreenB)
t.begin_fill()
for i in range(4):
  t.forward(20)
  t.rt(90)
t.end_fill()


#right window panels
t.color(0,0,0)
for i in range(4):
  t.forward(20)
  t.rt(90)
t.up()
t.goto(70, -20)
t.down()
t.forward(20)
t.up()
t.goto(80,-10)
t.rt(90)
t.down()
t.forward(20)
t.setheading(0)


#roof
t.up()
t.goto(0,0)
for h in range(5):
  for i in range(10-2*h):
    t.goto(10*i+10*h, 8*h)
    t.color(random.randint(200, 255), MediumRedG, MediumRedB)
    t.down()
    t.begin_fill()
    for j in range(4):
      t.forward(10)
      t.lt(90)
    t.end_fill()
    t.up()

#bonus challenge for students. 
#right bush
t.up()
t.goto(150, -100)
t.down()
t.color(GreenR,GreenG,GreenB)
t.begin_fill()
t.circle(20)
t.end_fill()
t.up()
