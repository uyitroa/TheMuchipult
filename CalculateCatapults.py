from graphics import *
import math

def main():
    win = GraphWin("My Circle", 1000, 1000)
    c = Circle(Point(50,50), 10)
    c.draw(win)

    a = 10
    v = 1

    alphaDegrees = 85
    alphaRadians = (math.pi * alphaDegrees) / 180
    tgAlfa = math.tan(alphaRadians)

    t = 0

    x = 0
    y = 200



    for z in range(0,68):
        t+=1

        lX = x
        lY = y


        y += ((a*t)-(tgAlfa * v))
        x += v

        
        aLine = Line(Point(lX,lY), Point(x,y))
        aLine.draw(win)

        time.sleep(0.01)

    win.getMouse() # pause for click in window
    win.close()

main()
