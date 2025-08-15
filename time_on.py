#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:16:46 2024

@author: lisaiizuka
"""

import math
import matplotlib.pyplot as plt 

v0 = 10 #volts
R = 10 * 10**3 #ohms
C = 10 * 10**-6 #farads
vmin = 0.01 #volts

#target voltage inputted by the user
target_voltage = float(input("enter the target voltage:"))
#make sure target voltage is a pos value
while target_voltage<0:
    print('target voltage must be a pos value')
    target_voltage = float(input("enter the target voltage:"))
    
#set up the graph
plt.figure()
plt.xlabel('charging time (seconds)')
plt.ylabel('duration(seconds)')
plt.title(f'duration above {target_voltage} volts')
plt.grid(True)



#calculate how long the light stays on for 
for tc in range(1, 51):
    tc *= 0.01
    time = 0
    duration_light_on = 0 #initialize the duration the light is on
    time_increment = 0.001 #time increment that t increases in each iteration of loop
    
    #calculate vmax after the end of charging
    vmax = v0 * (1-math.exp(-tc/(R*C))) 
    
    #calculate total time for one cycle
    tf = tc - (R*C)*math.log(vmin/vmax)
    
    #charge and discharge cycles
    while time <= tf:
        if time <= tc:
            #charge
            voltage = v0 * (1-math.exp(-time/(R*C)))
        else:
            #discharge
            voltage = vmax*math.exp(-(time-tc)/(R*C))
            
        #check if voltage is above the target voltage and if it is, plot
        if voltage >= target_voltage:
            duration_light_on += time_increment #add time increments to thetotal time the light is on
            
        #increment time
        time += time_increment
        
    #plot the graph
    plt.plot(tc, duration_light_on, 'bo')

plt.show()

    
    
    
    
    
    