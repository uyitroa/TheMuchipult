import getAngleVelocity # <- my part
import CalculateCatapults # <- your part
from graphics import *

def frames():
	win = GraphWin("Catapult", 900, 600)
	Stand = Rectangle(Point(220, 500), Point(200, 300))
	Stand.draw(win)

	x, y, velocity, angle = getAngleVelocity.getAngle(win)

	"""x, y = coord of rock"""
	"""variable win is the window that we will draw/work on"""
	CalculateCatapults.main(win, x, y, velocity, angle) # <- your part

frames()
