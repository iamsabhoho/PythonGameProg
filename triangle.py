import turtle

def tri(sqrlen, tur):
    """
    #draw squares with turtle
    :param sqrlen: the len of the square
    :param tur:
    :return:
    """
    if sqrlen < 5:
        return
    else:
        for i in range(3):
            tur.forward(sqrlen)
            tur.left(120)
        '''
        tur.up()
        tur.fd(5)
        tur.left(120)
        tur.fd(5)
        tur.left(-120)
        tur.down()
        '''

        tri(sqrlen - 10, tur)

#creates window
myWin = turtle.Screen()
#creates turtle
rp = turtle.Turtle()
#draw square
tri(100, rp)
#close the window with a click
myWin.exitonclick()
