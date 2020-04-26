
# from math import *
# from drawingpanel import *

# GRAVITY = -9.81

# # Plots the motion of a single projectile with the given
# # initial velocity v0, angle, and number of steps to plot.
# def projectile(panel, v0, angle, steps, color="black"):
#     # v0y = v0 sin theta, v0x = v0 cos theta
#     v0y = v0 * sin(radians(angle))
#     v0x = v0 * cos(radians(angle))

#     # t = -2v0 / a
#     totalTime = -2 * v0y / GRAVITY
#     dt = totalTime / steps

#     print ("       x       y      time")
#     for i in range(steps + 1):
#         t = i * dt
#         x = v0x * t
#         y = displacement(v0y, GRAVITY, t)
#         print ("%8.2f %8.2f %8.2f \n" % (x, y, t))
#         panel.canvas.create_oval(x, 300 - y, x + 5, 305 - y,
#                                  fill=color, outline=color)
#         panel.sleep(dt * 100)

# # Computes and returns the change in position of a projectile
# # given its initial velocity v0, acceleration a, and time t.
# def displacement(v0, a, t):
#     return v0 * t + 0.5 * a * t**2

# # Main
# panel = DrawingPanel(400, 300)

# projectile(panel, 30, 85, 20)
# projectile(panel, 60, 85, 50, color="red")
# projectile(panel, 120, 85, 100, color="green")

''' projectile_motion.py
projectile motion equations:
height = y(t) = hs + (t * v * sin(a)) - (g * t*t)/2
distance = x(t) = v * cos(a) * t
where:
t is the time in seconds
v is the muzzle velocity of the projectile (meters/second)
a is the firing angle with repsect to ground (radians)
hs is starting height with respect to ground (meters)
g is the gravitational pull (meters/second_square)
tested with Python27/Python33  by  vegaseat  20mar2013
'''
import math
def projectile_xy(v, a, hs=0.0, g=9.8):
    '''
    calculate a list of (x, y) projectile motion data points
    where:
    x axis is distance (or range) in meters
    y axis is height in meters
    v is muzzle velocity of the projectile (meter/second)
    a is the firing angle with repsect to ground (radians)
    hs is starting height with respect to ground (meters)
    g is the gravitational pull (meters/second_square)
    '''
    data_xy = []
    t = 0.0
    while True:
        # now calculate the height y
        y = hs + (t * v * math.sin(a)) - (g * t * t)/2
        # projectile has hit ground level
        if y < 0:
            break
        # calculate the distance x
        x = v * math.cos(a) * t
        # append the (x, y) tuple to the list
        data_xy.append((x, y))
        # use the time in increments of 0.1 seconds
        t += 0.1
    return data_xy
# use a firing angle of 45 degrees
d = 45
a = math.radians(d)  # radians
# muzzle velocity of the projectile (meters/second)
v = 100
data_45 = projectile_xy(v, a)
# find maximum height ...
point_height_max = max(data_45, key = lambda q: q[1])
xm, ym = point_height_max
print('''
    Projectile Motion ...
Using a firing angle of {} degrees
and a muzzle velocity of {} meters/second
the maximum height is {:0.1f} meters
at a distance of {:0.1f} meters,'''.format(d, v, ym, xm))
# find maximum distance ...
x_max = max(data_45)[0]
print("the maximum distance is {:0.1f} meters.".format(x_max))
''' result ...
    Projectile Motion ...
Using a firing angle of 45 degrees
and a muzzle velocity of 100 meters/second
the maximum height is 255.1 meters
at a distance of 509.1 meters,
the maximum distance is 1018.2 meters.
'''