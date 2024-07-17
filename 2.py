#import the turtle library for
# drawing the required curve

import turtle as tt
# set the background color as black,
# pensize as 2 and speed of drawing
# curve as 10(relative)
tt.bgcolor('black')
tt.pensize(2)
tt.speed(10)

# Iterate six times in total
for i in range(6):
    # choose your color combination
    for color in('red','magenta','blue','cyan','green','white','yellow'):
        tt.color(color)
    # draw a circle of chosen size, 100 here
    tt.circle(100)
    # move 10 pixels left to draw another circle
    tt.left(10)
    # hide the cursor(or turtle) which drew the circle
    tt.hideturtle()