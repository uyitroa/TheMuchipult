from graphics import *


def WaitUntilClicked(window):
		decideToPull = False

		while decideToPull == False:

			if window.checkMouse() != None:
				xMouse = window.checkMouse().getX()
				yMouse = window.checkMouse().getY()

				if almostEqual(xMouse,xRock) and almostEqual(yMouse,yRock):
					decideToPull = True

def almostEqual(compared, comparee):
	if compared >= comparee - 5 and compared <= comparee +5:
		return True
	else:
		return False


def pullSystem(rock,window):
	
	# Rock need to follow the cursor
	xRock = window.checkMouse().getX()
	yRock = window.checkMouse().getY()
	rock = Circle(Point(xRock,yRock),5)
	rock.draw(window)

	connectLine = Line(Point(xRock,yRock),Point(210,620))
	connectLine.draw(window)
	
	return xRock,yRock


def main():
	win = GraphWin("My Circle", 1440, 900)

	
	Stand = Rectangle(Point(220,800),Point(200,600))
	Stand.draw(win)
	

	xRock = 210
	yRock = 620

	rock = Circle(Point(xRock,yRock),5)
	rock.draw(win)

	WaitUntilClicked(win)			
	
	while True:
		xRock, yRock = pullSystem(rock,win)

if __name__ == "__main__":
	main()
