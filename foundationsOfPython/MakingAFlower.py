import turtle

window=turtle.Screen()
window.bgcolor("black")
a=turtle.Turtle()
a.shape("arrow")
a.color("blue")
a.speed(0.2)
times=24

while(times):
    a.right(10)
    a.forward(100)

    a.right(55)
    a.forward(35)

    a.right(90)
    a.forward(35)

    a.right(55)
    a.forward(100)
    a.right(3)
    times=times-1

a.color("green")
a.right(20)
a.forward(200)
window.exitonclick()
