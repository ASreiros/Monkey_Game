from turtle import Turtle
import constants


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.color("yellow")
		self.goto((constants.SCREEN_WIDTH - 400), (constants.SCREEN_HEIGHT - 50))
		self.score = 0

	def score_up(self):
		self.score += 1
		self.clear()
		self.write(f"Score: {self.score}", font=("Courier", 30, 'normal'))
		return self.score
