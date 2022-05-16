import turtle as turtle_module


screen = turtle_module.Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title ="Make your bet", prompt = "Which turtle will win the race? Enter a color:")

tim = turtle_module.Turtle(shape="turtle")
tim.penup


#Take turtles to starting line
tim.goto(x=-230,y=100)

screen.exitonclick()
