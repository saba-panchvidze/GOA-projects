from turtle import *

#we want to paint a house

#step 1: draw a square 
speed(3)
width(7)
color("purple") 
forward(200) 
left(90) 

forward(200) 
left(90) 

forward(200) 
left(90) 

forward(200) 
left(90) 
#end of square

#drawing a door 

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #heght of the droor
right(90)
forward(60) 
right(90)
forward(120) 
end_fill()

#end of door


#drawing a roof 
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150) 
forward(200)

left(120)
forward(200)
end_fill()
#end of roof

#drawing 1st window
penup()
goto(0, 0) 
pendown() 

color("purple")
right(150)
forward(180)

color("blue")
begin_fill()
right(90) 
forward(45)

right(90) 
forward(45)

right(90)
forward(45)
end_fill()
#end of 1st window

#drawing 2nd window
penup()
goto(200, 180)
pendown()
color("blue")
begin_fill()
forward(45) 

left(90)
forward(45)

left(90)
forward(45)
end_fill()
#end of 2nd window

#drawing ended, thanks for watching :)))