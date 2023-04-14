from turtle import Turtle
import constants


class ScreenManager:
	def __init__(self):
		self.drawer = Turtle()
		self.drawer.hideturtle()
		self.drawer.penup()
		self.draw_land()

	def draw_land(self):
		self.drawer.goto(x=constants.SCREEN_WIDTH*-1-10, y=-constants.SCREEN_HEIGHT+100)
		self.drawer.width(200)
		self.drawer.color('sienna')
		self.drawer.pendown()
		self.drawer.forward(constants.SCREEN_WIDTH*2+20)