
import turtle as t
t.pensize(20)
t.color("red","pink")
i=0
n=1
t.speed(10)
while i<10000: 
    
    t.goto(n-6,i*5-10)
    n-=6
    i+=3
    
    print("x=")
    print(n)

    print("y=")
    print(i)






