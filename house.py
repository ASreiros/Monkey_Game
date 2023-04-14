from turtle import Turtle
import constants


class House(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.setheading(180)
		self.flag = False
		self.shape('./img/house.gif')

	def start_position(self):
		self.hideturtle()
		self.goto(x=constants.SCREEN_WIDTH+50, y=0)
		self.showturtle()
		self.flag = True

	def move_house(self):
		if self.flag:
			self.forward(20)
			position = self.pos()
			if position[0] < -constants.SCREEN_WIDTH:
				self.start_position()

	def house_collision(self, turtle):
		if self.distance(turtle) < 175 and self.flag:
			return True
		else:
			return False
