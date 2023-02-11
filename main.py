import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(fun=player.go_up, key="Up")
screen.onkey(fun=player.go_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.6)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    #detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

    #detect successful crossing
    if player.is_at_finish_line():
        player.return_position()
        car_manager.increase_speed()
        score_board.update_level()


screen.exitonclick()
