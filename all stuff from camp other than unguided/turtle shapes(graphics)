import turtle

turtle.title("Turtle Intro")
turtle.bgcolor("dark green")
turtle.setup(600,600)
turtle.shape("circle")

screen = turtle.Screen()
tut = turtle.Turtle()

def star(length, color):
    tut.fillcolor(color)
    tut.begin_fill()

    x = 0
    while x < 5:
        tut.forward(int(length))
        tut.right(144)
        x += 1
    tut.end_fill()

def triangle(length, color):
    tut.fillcolor(color)
    tut.begin_fill()

    x = 0
    while x < 3:
        tut.forward(int(length))
        tut.right(120)
        x += 1
        tut.end_fill()

def circle(length, color):
    tut.fillcolor(color)
    tut.begin_fill()
    tut.circle(int(length))
    tut.end_fill()

input_shape = input("triangle, circle or star?\n")
input_length = input("Choose a size between 10 and 500\n")
input_color = input("Choose a color\n")

if input_shape == 'triangle':
    triangle(input_length,input_color)
elif input_shape == 'circle':
    circle(input_length,input_color)
elif input_shape == 'star':
    star(input_length,input_color)

turtle.done()