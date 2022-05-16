import turtle as turtle_module

tim = turtle_module.Turtle()
screen = turtle_module.Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title ="Make your bet", prompt = "Which turtle will win the race? Enter a color:")


screen.exitonclick()
