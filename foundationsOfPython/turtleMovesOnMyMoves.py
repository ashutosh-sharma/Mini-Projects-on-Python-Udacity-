import turtle


#Drawing a circle with a sqaures using a turtle
def draw_sq():
    window=turtle.Screen()
    window.bgcolor("red")

    kachua=turtle.Turtle()
    kachua.speed(0.2)
    kachua.color("yellow")
    kachua.shape("turtle")
    
    a=50
    while(a):
        kachua.right(2)
        kachua.forward(100)
        kachua.right(90)
        a=a-1
        
    window.exitonclick()


#Drawing a triangle with a turtle
def draw_triangle():
    kachua=turtle.Turtle()
    kachua.color("Green")

    a=3
    while(a):
        kachua.forward(100)
        kachua.right(120)
        a=a-1
        
    
    draw_sq()
    window.exitonclick()


draw_triangle()


