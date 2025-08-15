#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:31:52 2024

@author: lisaiizuka
"""

import numpy as np
import matplotlib.pyplot as plt


#calculate the voltage at different times
def approx_voltage ( v0 , R , C , tC ):
    '''
    Return the voltage of the capacitor over time
    Parameters
    v0 : ( float or int ) voltage of the battery in volts
    R : ( float or int ) resistance of the resistor in ohms
    C : ( float or int ) capacitance of the capacitor in farads
    tC : ( float or int ) charging time of the capacitor in seconds
    Returns as a tuple
    t : a list of numbers of time values in seconds from 0 to tf
    v : a list of numbers of capacitor voltage in volts , corresponding
        to time values in t
    '''
    #assign constant values
    vmin = 0.01 #volts
    tf = tC - R*C*np.log(vmin/(v0*(1-np.exp(-tC/(R*C))))) #seconds
    
    #generate an array of time values (in secs) from 0 to tf with length 1000 to ensure a smooth curve
    t_charge = np.linspace(0, tC, 500) #generate an array of 500 evenly spaced time values btwn 0 and tC corresponding to the charging phase
    t_discharge = np.linspace(tC, tf, 500) #generate 500 evenly spaced time values vetween tC and tf corresponding to the discharging phase
    
    
    #calculate voltage during charging (0 ≤ t ≤ tc)
    v_charge = v0 * (1-np.exp(-t_charge/(R*C)))
    
    #calculate maximum capacitor voltage (achieved at t = tc)
    vmax = v0 * (1-np.exp(-tC/(R*C)))
    
    #calculate voltage during discharging (tc < t ≤ tf)
    v_discharge = vmax * np.exp(-(t_discharge-tC)/(R*C))
    
    #create a single aray v that contains the voltage values of the capacitator over time
    v = np.zeros(np.size(v_charge) + np.size(v_discharge)) #create a new array with the correct length
    v[:np.size(v_charge)] = np.copy(v_charge) #copy v_charge into the first part of v with voltage values from the charging phase
    v[np.size(v_charge):] = np.copy(v_discharge) #copy v_discharge into the second part of v with voltage values from the discharging phase
    
    #do the same thing to create a time array
    t = np.zeros(np.size(t_charge) + np.size(t_discharge)) #create a new array filled with zeros of the correct length
    t[:np.size(t_charge)] = np.copy(t_charge) #copies the t_charge array into the first part of the t array
    t[np.size(t_charge):] =np.copy(t_discharge) #copies the t_discharge array inot the second part of the t array
    
    return t, v

#plot for sensitivity analysis 1 with varying C values and a fixed tC
def sensitivity_analysis_1(v0, R,tC):
    capacitances = [5e-6, 7.5e-6, 10e-6, 12.5e-6, 15e-6] #in farads
    plt.figure(1)
    
    #iterate over different capacitance values and plot the resulting voltage vs time curves for each capacitance value
    for C in capacitances:
        t, v = approx_voltage(v0, R, C, tC) #call approx_voltage ( v0 , R , C , tC ) to return an array of time values and an array of the corresponding capacitor voltage values over time
        legend_text = f'C = {C * 1e6:1f} uF' #creates a label that will be used in the plot's legend to identify each line to their corresponding capacitances in microfarads
        plt.plot(t,v, label=legend_text) #plot the voltage vs time curve and label each curve with the corresponding capacitance value 
        
    plt.title('Capacitor Voltage vs Time (Varying Capacitance)')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.legend()
    plt.grid()
    plt.show()
        


#plot the sensitivity analysis 2 with random tC and a fixed C
def sensitivity_analysis_2(v0, R, C) :
    charging_times = np.linspace(0.1, 0.5, 5) #generate an array of charging times between 0.1 and 0.5 seconds
    plt.figure(2)
    
    for tC in charging_times:
       t, v =  approx_voltage(v0, R, C, tC) #call approx_voltage ( v0 , R , C , tC ) to return an array of time values and an array of the corresponding capacitor voltage values over time
       legend_text = f'tC = {tC:.2f} s' #creates a label that will be used in the plot's legend to identify each line to their corresponding charging times in seconds
       plt.plot(t,v, label=legend_text) #plot the voltage vs time curve and label each curve with the corresponding charging time value 
       
    plt.title('Capacitor Voltage vs Time (Varying Charging Time)')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.legend()
    plt.grid()
    plt.show()
    


    