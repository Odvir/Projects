import turtle
import time

screen_height = 600
screen_width = 800

left_screen = -1 * screen_width / 2
right_screen = screen_width / 2
bottom_screen = -1 * screen_height / 2
top_screen = screen_height / 2

# Screen
screen = turtle.Screen()
screen.title("Ball Bouncing Game")
screen.bgcolor("blue")
screen.tracer(0) # stops the screen from refreshing
screen.setup(screen_width, screen_height) # sets up the size of our screen


# Player
player = turtle.Turtle()
player.shape("square")
player.color("green")
player.up()
player.shapesize(stretch_wid=1, stretch_len=10)
player.sety(bottom_screen + 20)

def player_right():
    x = player.xcor()
    x += 10
    player.setx(x)

def player_left():
    x = player.xcor()
    x -= 10
    player.setx(x)

screen.listen() # Need this or the key press will not work
screen.onkeypress(player_right, "Right")
screen.onkeypress(player_left, "Left")

# Ball
t = turtle.Turtle()
t.shape("circle")
t.color("red")
t.up()
t.setpos(0, 50)

# Default size of a square and circle is 20 by 20
# Position gives us the center of the turtle
def ball_player_collision():
    player_left = player.xcor() - 10 * 10 # account for size stretch
    player_right = player.xcor() + 10 * 10 # account for the size stretch
    player_bottom = player.ycor() - 10
    player_top = player.ycor() + 10

    ball_left = t.xcor() - 10
    ball_right = t.xcor() + 10
    ball_bottom = t.ycor() - 10
    ball_top = t.ycor() + 10


    x_axis = False
    y_axis = False

    if ball_bottom <= player_top and ball_top >= player_bottom:
        x_axis = True
    if ball_left <= player_right and ball_right >= player_left:
        y_axis = True

    return x_axis and y_axis # this will return the condition result

def t_collision():
    global x_move
    global y_move
    global ball_in_air

    x = t.xcor()
    y = t.ycor()
    
    if y >= top_screen:
        y_move = -1 * y_move
    elif x >= right_screen:
        x_move = -1 * x_move
    elif x <= left_screen:
        x_move = -1 * x_move
    elif ball_player_collision() == True:
        y_move = -1 * y_move
    elif y <= bottom_screen:
        ball_in_air = False

def t_move():
    x = t.xcor()
    x += x_move
    t.setx(x)

    y = t.ycor()
    y += y_move
    t.sety(y)

x_move = 3
y_move =3
ball_in_air = True


timer = 60
def countdown():
    global timer
    timer -=1
    screen.ontimer(countdown,1000)
screen.ontimer(countdown,1000)

def go():
    screen.update()
    t_move()
    t_collision() 
    if timer > 0:
        screen.ontimer(go,10)
# while True:
#     screen.update() # refreshes the screen manually
#     turtle.ontimer(f,1000)
#     t_move()
#     t_collision()
    
#     time.sleep(.01) 
go()
turtle.mainloop()