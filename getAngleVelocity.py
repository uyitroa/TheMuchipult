from graphics import *
import math

def motion(root):
	"""get mouse coordinate even not clicked"""

	x = root.winfo_pointerx() - root.winfo_rootx()
	y = root.winfo_pointery() - root.winfo_rooty()
	return x,y

def WaitUntilClicked(window, xRock, yRock):
	"""wait until player decide to
		fire the rock
		:type window: object"""
	decideToPull = False

	while not decideToPull:

		coordMouse = window.checkMouse()

		if coordMouse != None:
			xMouse = coordMouse.getX()
			yMouse = coordMouse.getY()

			if almostEqual(xMouse, xRock) and almostEqual(yMouse, yRock):
				decideToPull = True


def almostEqual(compared, comparee):
	"""Function to check if two values are almost equal 
	(means a difference of 5 unit)"""

	return comparee - 5 <= compared <= comparee + 5


def pullSystem(connectLine,connectLine2,rock, xRock, yRock, window):
	"""Funtion to animate well player drag the rock to fire
	rock will follow the cursor and etc"""

	# Rock need to follow the cursor

	"""xMouse = window.checkMouse().getX()
	yMouse = window.checkMouse().getY()"""

	xMouse, yMouse = motion(window)

	rock.move(xMouse - xRock, yMouse - yRock)


	connectLine.undraw()
	window.update()

	connectLine2.undraw()
	window.update()


	connectLine = Line(Point(xRock, yRock), Point(210, 320))
	connectLine2 = Polygon(Point(xRock, yRock), Point(210, 310))
	connectLine.draw(window)
	connectLine2.draw(window)


	return xMouse, yMouse, connectLine, connectLine2 # return mouse coordinate for the new coord of rock


def calculValues(xRock, yRock):

	opposite_side = yRock - 300
	hypotenuse = math.sqrt((220 - xRock)**2 + (300 - yRock)**2)

	angle = math.asin(opposite_side/hypotenuse) # radian type
	angle = math.degrees(angle)

	velocity = hypotenuse/100

	return xRock, yRock, velocity, angle

def getValues(win):
	#win = GraphWin("My Circle", 900, 600)

	Stand = Rectangle(Point(220, 500), Point(200, 300))
	Stand.draw(win)

	xRock = 210
	yRock = 320

	rock = Circle(Point(xRock, yRock), 5)
	rock.draw(win)

	connectLine = Polygon(Point(xRock , yRock),Point(210,320))
	connectLine2 = Polygon(Point(xRock, yRock),Point(210,310))


	WaitUntilClicked(win, xRock, yRock)


	while True:
		xRock, yRock, connectLine, connectLine2 = pullSystem(connectLine, connectLine2,rock, xRock, yRock, win)
		if win.checkMouse():
			break

	return calculValues(xRock, yRock)


if __name__ == "__main__":
	win = GraphWin("My Circle", 900, 600)
	x,y,velo,angle = getValues(win)
	print("x_Rock:",x)
	print("y_Rock:",y)
	print("Velocity:",velo)
	print("Angle:",angle)

