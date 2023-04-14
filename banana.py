from turtle import Turtle
import constants
from random import randint

class Banana(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.setheading(180)
		self.shape('./img/banana.gif')
		self.start_position()

	def start_position(self):
		self.hideturtle()
		self.goto(x=constants.SCREEN_WIDTH+50, y=randint(-10, 10)*25)
		self.showturtle()

	def move_banana(self):
		self.forward(constants.SPEED)
		position = self.pos()
		if position[0] < -constants.SCREEN_WIDTH:
			self.start_position()

	def collision(self, turtle):
		if self.distance(turtle) < 100:
			self.start_position()
			return True
		else:
			return False

