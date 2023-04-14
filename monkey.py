from turtle import Turtle
import constants


class Monkey(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.jump_flag = False
		self.jump_counter = 0
		self.penup()
		self.goto(x=-constants.SCREEN_WIDTH/2, y=-constants.SCREEN_HEIGHT+250)
		self.monkey_counter = 1
		self.showturtle()
		self.shape('./img/monkey1.gif')

	def move(self):
		if not self.jump_flag:
			self.shape(f'./img/monkey{self.monkey_counter}.gif')
			self.monkey_counter += 1
			if self.monkey_counter > 5:
				self.monkey_counter = 1
		else:
			self.jump_counter += 1
			if self.jump_counter <= 15:
				self.shape('./img/monkey6.gif')
				position = self.pos()
				self.goto(position[0], position[1]+20)
			elif self.jump_counter <= 22:
				self.shape('./img/monkey7.gif')
			elif self.jump_counter <= 37:
				position = self.pos()
				self.goto(position[0], position[1]-20)
			else:
				self.shape('./img/monkey1.gif')
				self.jump_flag = False
				self.jump_counter = 0
				self.monkey_counter = 1

	def start_jump(self):
		self.jump_flag = True

	def hide_monkey(self):
		self.hideturtle()

