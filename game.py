#rectangle function
def rectangle(turtle,length,breadth,tilt):
    for i in range(2):
        turtle.forward(length)
        turtle.right(45)
        turtle.forward(tilt)
        turtle.right(45)
        turtle.forward(breadth)
        turtle.right(45)
        turtle.forward(tilt)
        turtle.right(45)
        turtle.forward(length)




import turtle
import random
import time
# turtle.bgcolor("lightblue")
screen = turtle.Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("#99b9d1")
screen.tracer(0)    # Turn off automatic screen updates

#Game Title
title = turtle.Turtle()
title.penup()
title.pensize(7)
title.color("black")
title.hideturtle()
title.goto(0,430)
title.pendown()
title.begin_fill()
rectangle(title,520,70,9)
title.end_fill()
title.penup()
title.color("white")
title.goto(0,347)
title.write("THE TURTLE GAME",move=True,align='center',font=["Zero Velocity BRK", 70, "bold"])
title.pendown()



# Create two turtles

player_one = turtle.Turtle()
player_one.penup()
player_one.goto(-320,250)
player_one.color("Brown")
player_one.write("Player 1",move=True,align='left',font=["Zero Velocity BRK", 27, "italic"])
player_one.pendown()
player_one.penup()
player_one.goto(-320,150)
player_one.pendown()
player_one.color("black","red")
player_one.begin_fill()
player_one.shape('turtle')
player_one.shapesize(2.5,2.5,2.5)
player_one.end_fill()

player_two = turtle.Turtle()
player_two.penup()
player_two.goto(-320,-250)
player_two.color("Brown")
player_two.write("Player 2",move=True,align='left',font=["Zero Velocity BRK", 27, "italic"])
player_two.pendown()
player_two.penup()
player_two.goto(-320,-150)
player_two.pendown()
player_two.color("black","yellow")
player_two.begin_fill()
player_two.shape('turtle')
player_two.shapesize(2.5,2.5,2.5)
player_two.end_fill()

finish_line = turtle.Turtle()
#finish_line.hideturtle()
finish_line.pensize(4)
finish_line.color("black","white")
finish_line.penup()
finish_line.goto(440,250)
finish_line.pendown()
finish_line.right(90)
# finish_line.forward(500)
# finish_line.right(90)
# finish_line.forward(5)
# finish_line.right(90)
# finish_line.forward(500)
# finish_line.right(90)
# finish_line.forward(5)

for j in range(35):
    finish_line.begin_fill()
    for i in range(4):
        finish_line.forward(15)
        finish_line.left(90)
    finish_line.end_fill() 
    finish_line.forward(15)                            
     



winner = None
win = turtle.Turtle()
win.pensize(5)
win.pencolor("Black")
win.penup()
win.goto(0,0)
win.pendown()
win.hideturtle()

# Make both turtles move
while player_one.xcor() <=440 or player_two.xcor()<=440:
    random_dist = [5,4,6,2,1,0]
    player_one.penup()
    player_one.forward(random.choice(random_dist))
    player_one.pendown()
    player_two.penup()
    player_two.forward(random.choice(random_dist))
    player_two.pendown()
    screen.update()  # Manually update the screen after both movements

    # screen.delay(20) # Optional delay to control speed
    if player_one.xcor() > 440 and winner == None:
        winner = player_one
        win.write("Player 1 Won",move=False,align='center',font=["Zero Velocity BRK", 120, "bold"])
        break
    elif player_two.xcor() > 440 and winner == None:
        winner = player_two
        win.write("Player 2 Won",move=False,align='center',font=["Zero Velocity BRK", 120, "bold"])   
        break

for _ in range(10):
    winner.shapesize(4, 4, 4)
    screen.update()
    time.sleep(0.2)
    winner.shapesize(1, 1, 1)
    screen.update()
    time.sleep(0.2)

screen.mainloop()
turtle.done()




