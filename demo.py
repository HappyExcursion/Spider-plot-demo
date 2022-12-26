from turtle import *
from math import cos, sqrt, radians

# drawing out the background of a spider plot

# Looking at the client's briefing, we can make the following
# observations:
# 1. The background of a spider plot looks like it's made up of
#    multiple small triangles.
# 2. The amount of triangles are dependent on how many elements 
#    there are in each dataset, i.e. if there are 10 elements in 
#    a dataset, then there should be 10 small triangles
# 3. The triangles are isosceles (have equal length sides)
#
# From the observations above, we can devise a plan to draw out 
# the background of the spider plot
#
# 1. We can use a loop that loops repeats x times (x = amount of 
#    elements in dataset), in each iteration we draw out one 
#    trangle
# 2. The triangle's side length (called leg in trigonometry) is 
#    the same. The triangle's top angle (vertex angle in trig) can
#    be calculated by dividing 360 by the number of triangles as
#    the triangles forms a circle.
# An alternative approach of drawing out the base of the triangles 
# would be drawing the legs only first, and each time a leg is drawn,
# record the position (coordinates) of the end points. After the legs
# are drawn, loop through all the end position coordinates to connect
# them (with goto())
#
# Below is some partial code that attempt to draw parts of the 
# background spider plot with the trig approach


# defining constants
num_of_tri = 10
triangle_side = 100  # side length of the triangle
triangle_top_angle = 360/num_of_tri
triangle_base_angle = (180-triangle_top_angle)/2
# using cosine rule to calculate the length of the base of the triangle
# sqrt, cos, and radians are functions of the math module. They need to
# be imported
triangle_base = sqrt(triangle_side**2*2 - 2*triangle_side**2*cos(radians(triangle_top_angle)))

# first triangle (start drawing from 12 o'clock position)
setheading(90)  # start with the turtle facing up (12 o'clock)
forward(triangle_side)  # draw out one side line 
right(180-triangle_base_angle)  # the turning angle is the supplementary angle to the base angle
forward(triangle_base)  # draw out the base

# second triangle (clockwise rotation)
penup()  # go home without leaving a trace
home()  # go back to the center (0, 0)
pendown()  # put the pen down ready for drawing the next triangle
setheading(90-triangle_top_angle)
forward(triangle_side)
right(180-triangle_base_angle)
forward(triangle_base)

# a loop is needed to draw out the full background plot.
# I'm sure you got this！
pass

done()