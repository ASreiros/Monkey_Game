from turtle import Turtle
from random import randint
import constants


class Road:
	def __init__(self):
		self.stones = []
		self.retired_stones = []
		self.add_rock()

	def add_rock(self):
		if len(self.retired_stones) == 0:
			rock = Turtle()
		else:
			rock = self.retired_stones.pop(0)
		rock.hideturtle()
		rock.penup()
		rock.goto(x=constants.SCREEN_WIDTH+20, y=-constants.SCREEN_HEIGHT+randint(1, 3)*50)
		rock.setheading(180)
		rock.showturtle()
		option = randint(1, 3)
		#
		if option == 1:
			rock.shape('./img/grass1.gif')
		elif option == 2 :
			rock.shape('./img/stone.gif')
		else:
			rock.shape('./img/grass2.gif')
		self.stones.append(rock)

	def move_stones(self):
		for rock in self.stones:
			rock.forward(20)
			if rock.pos()[0] < -constants.SCREEN_WIDTH:
				rock.hideturtle()
				self.retired_stones.append(rock)
		for rock in self.retired_stones:
			if rock in self.stones:
				self.stones.remove(rock)


