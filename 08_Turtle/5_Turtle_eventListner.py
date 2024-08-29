from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveforward():
    tim.forward(10)
    
screen.listen()
screen.onkey(key = "space", fun = moveforward)   # Note that when we pass a function as an input of another function, we don't add any kind of paranthesis to it.

screen.exitonclick()
