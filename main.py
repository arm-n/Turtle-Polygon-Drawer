from turtle import Turtle,Screen
from random import choice


tom=Turtle()
print(tom)
tom.shape("turtle")
colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "gold", "silver",
    "navy", "lime", "teal", "maroon", "violet", "turquoise", "indigo",
    "beige", "salmon", "coral", "orchid", "plum", "tan", "olive"
]

tom.color(choice(colors))
moves = [tom.forward, tom.backward, tom.left, tom.right]
tom.pensize(7)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.right(angle)

for shape_side_n in range(3, 10):
    tom.color(choice(colors))
    draw_shape(shape_side_n)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()