import turtle
from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard
from screen_manager import ScreenManager
from monkey import Monkey
from banana import Banana
from road import Road
from house import House
import constants

screen = Screen()
screen.setup(width=constants.SCREEN_WIDTH*2, height=constants.SCREEN_HEIGHT*2)
# screen.bgcolor('chartreuse')
screen.bgpic('img/jungle.gif')
# screen.bgpic('img/forest.gif')
screen.title("Monkey game")
screen.tracer(0)
turtle.register_shape('./img/monkey1.gif')
turtle.register_shape('./img/monkey2.gif')
turtle.register_shape('./img/monkey3.gif')
turtle.register_shape('./img/monkey4.gif')
turtle.register_shape('./img/monkey5.gif')
turtle.register_shape('./img/monkey6.gif')
turtle.register_shape('./img/monkey7.gif')
turtle.register_shape('./img/stone.gif')
turtle.register_shape('./img/grass1.gif')
turtle.register_shape('./img/grass2.gif')
turtle.register_shape('./img/banana.gif')
turtle.register_shape('./img/house.gif')
manager = ScreenManager()
road = Road()
banana = Banana()
monkey = Monkey()
house = House()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(monkey.start_jump, "space")

rock_counter = 20
game_is_on = True
while game_is_on:
	screen.update()
	monkey.move()
	rock_counter -= 1
	if rock_counter <= 0:
		rock_counter = 20
		road.add_rock()
	road.move_stones()
	banana.move_banana()
	house.move_house()
	score = 0
	if banana.collision(monkey):
		score = scoreboard.score_up()
	if score == constants.SCORE_TO_WIN:
		house.start_position()
	if house.house_collision(monkey):
		game_is_on = False
	time.sleep(0.1)






screen.exitonclick()