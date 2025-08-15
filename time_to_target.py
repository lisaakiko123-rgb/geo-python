#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:44:21 2024

@author: lisaiizuka
"""


import math

#constants
v0 = 10 #volts
R = 10 * 10**3 #ohms
C = 10 * 10**-6 #farads

#user specified voltage and user specified charging time for max voltage
tc= float(input("enter the max charging time in seconds:"))
goal_voltage = float(input("enter the goal voltage in volts:"))

#make sure tc and goal voltage is pos
while tc<0 or goal_voltage<0:
    print('please enter a pos value')
    tc= float(input("enter the max charging time in seconds:"))
    goal_voltage = float(input("enter the goal voltage in volts:"))



#inital values of time and voltage
time = 0 #initial time
voltage = 0 #inital voltage
time_increment = 0.001 #time increment that t increases in each iteration of loop
reached_goal_voltage = False #set a variable to track if goal voltage has been reached

#update the voltage as time increases until tc
while time<=tc:
    voltage = v0 * (1-math.exp(-time/(R*C))) #calculate the voltage at specific time
    
    #stop once it reaches goal voltage
    if voltage >= goal_voltage:
        reached_goal_voltage = True
        print (f'it takes {time:.3f} seconds to reach {goal_voltage} volts')
        #stop the while loop by making time<=tc false
        time = tc + 10
        
        
    time += time_increment #increment time until it reaches the goal voltage
        
if not reached_goal_voltage:
    print(f'the capcitator cannot reach {goal_voltage} volts' )


