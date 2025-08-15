#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:33:58 2024

@author: lisaiizuka
"""

import random
import math
import matplotlib.pyplot as plt 

#big circle parameters
b_radius = 5
b_x =0
b_y =0

#small circle parameters
s_radius = 1
s_x = 0
s_y = 0

#make sure big radius is actually bigger than small radius and switch if it isn't
if b_radius < s_radius:
    x = s_radius
    s_radius = b_radius
    b_radius = x
 
#checks if the circles overlap
distance = math.sqrt((s_x - b_x)**2 + (s_y -b_y)**2)
overlap = distance < (b_radius + s_radius)
#when they don't overlap
if not overlap: 
    print('the 2 circles do not overlap')
else: 
    #set up the bounds of the box
    x_max = 10
    x_min = -10 
    y_max = 8 
    y_min = -10
    #setting up counters for counting the number of points in each regions
    inside_small = 0
    inside_big = 0
    #setting up the number of darts
    num_darts = 10000
    #plot the points
    for i in range (num_darts):
        rand_x = random.uniform(x_min, x_max)
        rand_y = random.uniform(y_min, y_max)
        #check if the point is inside the small circle
        in_small_circle= ((rand_x - s_x)**2 + (rand_y - s_y)**2) <= s_radius**2
        in_big_circle= ((rand_x - b_x)**2 + (rand_y - b_y)**2) <= b_radius**2
        # Plot the dart 
        if in_small_circle:
            plt.plot(rand_x, rand_y,'r*')
            inside_small += 1
        elif in_big_circle:
            plt.plot(rand_x, rand_y,'b*')
            inside_big += 1
        else:
            plt.plot(rand_x, rand_y, 'g*' )
    #use the bounds to calculate the area of the rectangle
    area = (x_max - x_min)*(y_max-y_min)
    #use the area of the rectangle to calculate the area of the crescent
    crescent_area = area*(inside_big/num_darts)

    
    #present estimated area of the crescent!
    plt.title(f'Lune(or ring) has area {crescent_area: .4f} units squared')
    plt.axis('equal')
    plt.show()
    

