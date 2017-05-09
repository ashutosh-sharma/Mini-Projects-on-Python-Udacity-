import turtle
#Drawing a circle with a sqaures using a turtle
def draw_sq():
    window=turtle.Screen()
    window.bgcolor("red")

    kachua=turtle.Turtle()
    kachua.speed(0.6)
    kachua.color("yellow")
    kachua.shape("turtle")
    
    a=50

    while(a):
        kachua.forward(100)
        kachua.right(90)
        a=a-1
        
    window.exitonclick()

draw_sq()
