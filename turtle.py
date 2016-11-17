import turtle

def tree(sqrlen, tur, b):
    """
    #draw a tree with turtle
    :param sqrlen: the len of the square
    :param tur:
    :return:
    """
    if sqrlen >= 10:
        return
    else:
        tur.fd(sqrlen)

        tree(sqrlen-20, tur, 10)

#creates window
myWin = turtle.Screen()
#creates turtle
rp = turtle.Turtle()
#turing left
rp.left(90)
#draw square
tree(150, rp, 10)
#close the window with a click
myWin.exitonclick()
