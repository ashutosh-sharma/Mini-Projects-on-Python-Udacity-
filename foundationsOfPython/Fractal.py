import turtle

window=turtle.Screen()
window.bgcolor("white")
a=turtle.Turtle()
a.shape("arrow")
a.color("blue","green")
a.speed(0.2)

times=3
x=3
y=3
times2=3

while(times2):
    times=3
    while(times):
        x=3
        while(x):
            y=3
            a.begin_fill()
            while(y):
                a.forward(25)
                a.left(120)
                y=y-1
        
            a.end_fill()    
            a.forward(25)   
            x=x-1
        
        a.left(120)
        a.forward(25)
        times=times-1
    if(times2!=1):
        a.forward(100)
    times2=times2-1
    
window.exitonclick()
