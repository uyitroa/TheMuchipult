from graphics import *


def WaitUntilClicked(window):
		"""wait until player decide to 
		fire the rock"""
		decideToPull = False

		while not decideToPull:
			coordMouse = window.checkMouse()
			
			if coordMouse != None:
				xMouse =  coordMouse.getX()
				yMouse = coordMouse.getY()

				if almostEqual(xMouse,xRock) and almostEqual(yMouse,yRock):
					decideToPull = True

def almostEqual(compared, comparee):
	"""Function to check if two values are almost equal 
	(means a difference of 5 unit)"""
	
	return compared >= comparee - 5 and compared <= comparee +5


def pullSystem(rock,xRock,yRock,window):
	"""Funtion to animate well player drag the rock to fire
	rock will follow the cursor and etc"""
	# Rock need to follow the cursor
	xMouse = window.checkMouse().getX()
	yMouse = window.checkMouse().getY()

	rock.move(xMouse - xRock, yMouse - yRock)

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
		xRock, yRock = pullSystem(rock,xRock,yRock,win)

if __name__ == "__main__":
	main()
