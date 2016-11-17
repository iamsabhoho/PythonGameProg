import math
import turtle
import time

##TRIANGLE CODE BELOW##
def draw_triangle(edge_len):
    for i in range(3):
        terence.forward(edge_len)
        terence.left(120)

def draw_sp_triangle(x,y,edge_len):
    if(edge_len <= 5):
        return

    terence.up()
    terence.goto(x,y)
    terence.down()
    draw_triangle(edge_len)


    draw_sp_triangle(x,y,edge_len/2)
    draw_sp_triangle(x+(edge_len/2),y,edge_len/2)
    draw_sp_triangle(x+(edge_len/4),y+((math.sqrt(3)/4)*edge_len),edge_len/2)

def nOS(): ## gotta go fasst
    turtle.delay(0)
    terence.speed(9)
    turtle.tracer(30,0)


terence = turtle.Turtle()
nOS()
start=time.time()
draw_sp_triangle(-200,-200,800) #The difference between size 200(0.64s) and 400(2.3s) is around 1.7s and it's quite significant.
terence.write("Computation time: " + str(time.time()-start) + "s")
