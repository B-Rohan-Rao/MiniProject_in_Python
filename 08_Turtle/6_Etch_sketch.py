
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveforward():
    tim.forward(10)

def moveback():
    tim.back(10)
    
def moveleft():
    tim.left(15)

def moveright():
    tim.right(15)

def clear_Screen():
    tim.reset()


screen.listen()
screen.onkey(key = "w", fun = moveforward)   
screen.onkey(key = "s", fun = moveback)   
screen.onkey(key = "a", fun = moveleft)   
screen.onkey(key = "d", fun = moveright)   
screen.onkey(key = "c", fun = clear_Screen)   

screen.exitonclick()
