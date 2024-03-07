from turtle import * 

#draw a house 

#draw a square
speed(8) 
width(5) 
color("green") 
forward (160)
left(90)

forward(200)
left(90)

forward(160)
left(90)

forward(200)
left(90) 
 
forward(60) 
left(90)

#draw a door 

color("blue")
begin_fill()

forward(80)
right(90) 

forward(40)
right(90) 

forward(80)
left(90) 
end_fill()

#draw a second house 
color("green")
forward(60) 

forward (160)
left(90)

forward(200)
left(90)

forward(160)
left(90)

forward(200)
left(90) 
 
forward(60) 
left(90)

color("blue")
begin_fill()
forward(80)
right(90) 

forward(40)
right(90) 

forward(80)
left(90) 
end_fill()

#draw a third house
color("green")
forward (220)
left(90)

forward(200)
left(90)

forward(160)
left(90)

forward(200)
left(90) 
 

forward(60) 
left(90)

color("blue")
begin_fill()
forward(80)
right(90) 

forward(40)
right(90) 

forward(80)
left(90) 
end_fill()

#draw 3 roof
color("green")

forward(60)
left(90)

forward(200)
left(30) 

color("red")
begin_fill()
forward(160)
left(120) 

forward(160) 
right(120)

forward(160)
left(120) 

forward(160) 
right(120)

forward(160)
left(120) 

forward(160) 
left(30)
end_fill()

#drawing field
color("green")
forward(200)
left(90)
forward(480)

begin_fill()
forward(220)
left(138) 

forward(292)
end_fill()

#drawing sun 
color("white")

right(45)
forward(120)

color("yellow") 
forward(60)

left(180)
forward(30)

right(90)
forward(30)

left(180)
forward(60)

left(180)
forward(30)

left(45)
forward(30)

left(180)
forward(60)

left(180)
forward(30)

left(90)
forward(30)

left(180) 
forward(60) 
color("green")

#drawing windows
penup()
goto(0,0) 
pendown()


right(48)
forward(175)

begin_fill()
color("orange")
right(90)
forward(45)

right(90)
forward(45)

right(90)
forward(45) 
end_fill() 

penup()
goto(160, 175)
pendown()

begin_fill()
forward(45)
left(90)

forward(45)
left (90)

forward(90)
left(90)

forward(45)
left(90)

forward(45)
end_fill()

penup()
goto(320,175)

begin_fill()
forward(45)
left(90)

forward(45)
left(90)

forward(90)
left(90)

forward(45)
left(90)

forward(45)
end_fill() 

penup()
goto(480,175)
pendown()

begin_fill()
forward(45)
left(90)

forward(45)
left(90)

forward(45)
end_fill() 

#drawing stars
penup()
goto(0,450)
pendown()

color("blue")
begin_fill()
forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
end_fill()

penup()
goto(160,450)
pendown()

begin_fill()
forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
end_fill()

penup()
goto(320,420)
pendown()

begin_fill()
forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
left(60)

forward(30)
right(120)

forward(30)
end_fill()