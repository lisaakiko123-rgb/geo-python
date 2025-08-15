# colliding_blocks.py
"""
Simulates and animates the motion of blocks in a room.  Assumes the blocks are
correctly initialized (not overlapped and all fit inside the bounding box).  
All units are metric: the length unit is meter, the mass unit is kilogram, and 
the time unit is second.


In order to see the animation, in the Spyder Python Console, type
    %matplotlib qt
to send the graphics to the qt graphical user interface.  You only need to do
this once in a session (unless you restart the kernel).
"""
# DO NOT MODIFY the given function docstrings.

import numpy as np
import matplotlib.pyplot as plt
import shapes 

def draw_blocks(xs, ws, hs, cs, w, h, title):
    """
    Draws the blocks in a bounding box of width w and height h and shows them 
    for at least 0.01 seconds. 
    xs[i] is the x-coordinate of the left edge of the i'th block.
    ws[i], hs[i] are the width and height of the i'th block.
    cs[i] is the color of the i'th block (e.g. 'blue' or 'brown').
    xs, ws, hs, cs all have the same length.
    You may assume that all blocks fit inside the bounding box.

    Parameters:
        xs (1D numpy array): x positions of the left edge of the blocks, in
                             ascending order                              
        ws (1D numpy array): widths of the blocks
        hs (1D numpy array): heights of the blocks
        cs (list of strings): colors of the blocks
        w (float): room width
        h (float): room height
        title (str): diagram title
    """
    floor= 0               # y-coordinate of the floor
    plt.cla()              # Clears current axes (removes all drawn objects).
    plt.xlim(floor, w)     # Sets the x-axis to range from 0 to w.
    plt.ylim(floor, h)     # Sets the y-axis to range form 0 to h.
    ax = plt.gca()         # Get current axes
    ax.set_aspect('equal') # Set current axes to equal scaling
    plt.xticks([])         # Removes the tick marks from the x-axis.
    plt.yticks([])         # Removes the tick marks from the y-axis.
    
    #######################################################
    ### DO NOT modify the function code above this line ###
    ### TODO: add your code below this line             ###
    #loop through the blocks and draw each one
    for i in range(len(xs)):
        #draw a rectangle for each block
        shapes.draw_rect(xs[i], floor, ws[i], hs[i], cs[i]) #pass the parameters to draw_rect

    pass

    #####################################################################
    ### DO NOT delete the function code below this line               ###
    ### OK to change the pause time (pause longer) during development ###
    
    plt.show()       # Shows the plot.
    plt.pause(0.01)  # Pauses 0.01 seconds in code execution; this is not the 
                     #   simulation time of the blocks model.


def next_timestep(xs, vxs, ws, hs, ms, w, h, dt, mu_k, e):
    """
    Returns the positions and velocities of the blocks at the next timestep,
    updated via the equations of motion, collisions between blocks and walls,
    and collisions between blocks.

    Parameters:
        xs (1D numpy array): x positions of the left edge of the blocks, in
                             ascending order                              
        vxs (1D numpy array): current x velocities of the blocks
        ws (1D numpy array): widths of the blocks
        hs (1D numpy array): heights of the blocks
        ms (1D numpy array): masses of the blocks
        w (float): room width
        h (float): room height
        dt (float): increment of time of simulate
        mu_k (float): Coefficient of kinetic friction
        e (float): Coefficient of restitution (Inelastic collision)
    Returns as a tuple:
        xs (1D numpy array): x positions of blocks after 1 timestep
        vxs (1D numpy array): x velocities of blocks after 1 timestep
        
    xs, vxs, ws, hs, ms all have the same length.
    """
    ### TODO: implement this function
    pass

    g = 9.81 #gravitational acceleration (m/s^2)
    
    #update positions based on current velocities
    xs = xs + vxs*dt
    # Handle collisions with walls
    for i in range(len(xs)):
        if xs[i] < 0:  # checks for left wall collision
            xs[i] = 0 #corrects the position if the block is beyond the left wall
            vxs[i] = -vxs[i] * e  # Reverse velocity with inelastic factor to simulate a bounce off the wall
        elif xs[i] + ws[i] > w:  # checks for right wall collision
            xs[i] = w - ws[i]  # Correct the position if the block is beyond the right wall
            vxs[i] = -vxs[i] * e  # Reverse velocity with inelastic factor to simulate a bounce off the wall
            
        # Apply kinetic friction
        change_vf = mu_k * g * dt  # Amount by which velocity changes from friction
        if vxs[i] > 0: #checks if block i is moving to the right (pos velocity)
            vxs[i] = max(0, vxs[i] - change_vf)  # reduces the block's velocity by the change_vf, while ensuring that the velocity doesn't go below zero
        elif vxs[i] < 0: #checks if block i is moving to the left
            vxs[i] = min(0, vxs[i] + change_vf) # increases the block's velocity by the change_vf (since it is moving to the left, friction will reduce its neg velocity), while ensuring velocity doesn't go below zero
            
    # Handle block collisions
    i = 0
    #initialize the loop to check for collisions btwn adjacent blocks
    while i < len(xs) - 1:
        # Check if the right edge of block i collides with the left edge of block i+1
        if xs[i] + ws[i] >= xs[i + 1]:
            #call the check_collsion() function to calculate the new velocities of the blocks i and i+1 after the collision
            vxs[i:i + 2], _ = check_collision(xs[i:i + 2], vxs[i:i + 2], ws[i:i + 2], ms[i:i + 2], e) #returns updated velocities for both blocks (vxs[i:i + 2]), and the second return value (_) is ignored
            
            # Adjust positions to ensure no overlap after collision
            overlap = (xs[i] + ws[i]) - xs[i + 1] #calculates how much the 2 blocks overlap after collision
            xs[i] -= overlap / 2  # Move the left block back slightly to reduce overlap
            xs[i + 1] += overlap / 2  # Move the right block forward slightly to reduce overlap

        i += 1 #increament i to check the next pair of blocks
    
    return xs, vxs #return updated positions and velocities


def check_collision(xs, vxs, ws, ms, e):
    """
    Returns the velocities of two blocks and True/False to indicate whether a
    collision occurred. The velocities are updated if the blocks have collided;
    otherwise, the velocities are unchanged.

    Parameters:
        xs (1D numpy array of length 2): x positions of the left edge of two blocks
        vxs (1D numpy array of length 2): x velocities of the two blocks
        ws (1D numpy array of length 2): widths of the two blocks
        ms (1D numpy array of length 2): masses of the two blocks
        e (float): Coefficient of restitution (Inelastic collision)

    Returns as a tuple:
        vxs_new (1D numpy array of length 2): x velocities, possibly updated, of 
                                             the two blocks
        collision_occurred (bool): True if a collision occured; otherwise False
    """
    ### TODO: implement this function
    if xs[0] + ws[0] >= xs[1]: #checks if the right edge of block 0 (left position x[0] plus width w[0]) is greater than or equal to the left edge of block 1 (xs[1])
        #A collision occurred
        collision_occurred = True
        #masses and velocities of the block
        m1, m2 = ms[0], ms[1]
        v1, v2 = vxs[0], vxs[1]
        
        #calculate new velocities after the collision
        v1_new = ((m1 - e * m2) * v1 + (1 + e) * m2 * v2) / (m1 + m2)
        v2_new = ((m2 - e * m1) * v2 + (1 + e) * m1 * v1) / (m1 + m2)
        
        #return updated velocities and True for collision
        return np.array([v1_new, v2_new]), collision_occurred 
    else:
        #No collision occurred, return original velocities
        collision_occurred = False
        return vxs, collision_occurred
    pass



def simulate_motion(xs, vxs, ws, hs, ms, cs, dt, w, h, T, mu_k, e):
    """
    Simulates and visualizes the motion of the blocks over a total time T.

    Parameters:
        xs (1D numpy array): initial x positions of the left edge of the blocks, 
                             in ascending order
        vxs (1D numpy array): initial x velocities of the blocks
        ws (1D numpy array): widths of the blocks
        hs (1D numpy array): heights of the blocks
        ms (1D numpy array): masses of the blocks
        cs (list of str): colors of the blocks
        dt (float): time step for each simulation update
        w (float): width of the room
        h (float): height of the room
        T (float): total simulation time
        mu_k (float): Coefficient of kinetic friction
        e (float): Coefficient of restitution (Inelastic collision)
    """
    # Set up figure window
    plt.close()
    plt.figure(1)
    plt.pause(2)
    plt.show()

    # Calculate the total number of simulation steps and display frames
    frames_per_second = 12
    num_steps = int(T // dt)  # Total number of simulated time-steps
    num_frames = min(
        num_steps, 
        int(T * frames_per_second)
    )  # Total displayed frames
    show_every = max(
        1, num_steps // num_frames
    )  # Display blocks every 'show_every' steps

    #######################################################
    ### DO NOT modify the function code above this line ###
    ### TODO: add your code below this line             ###
    
    #draw the blocks in their initial positions before the simulation begins 
    draw_blocks(xs, ws, hs, cs, w, h, "Block Simulation") 
    
    for step in range(num_steps):  #llop through each time step to update the block's position and velocities
        #update positions and velocities for the next timestep!!
        xs, vxs = next_timestep(xs, vxs, ws, hs, ms, w, h, dt, mu_k, e)
        #update visulization at specialized intervals
        if step % show_every == 0: #check whether it's time to redraw the blocks on the screen. (show_every determines how often the blcoks should be redrawn)
            draw_blocks(xs, ws, hs, cs, w, h, "Block Simulation") #redraws blocks at their new positions (xs) based on updated values from next_timestep
            plt.title(f"Time: {step * dt:.2f} seconds") #updates the title of the polot to display the time in the simulation calculated by step*dt
            plt.pause(0.01) #pause to show the update
        plt.show()
    pass



    
    
#### Script code
if __name__ == '__main__':
    # Code in this if-block executes only if this file is run as a script.
    # Code in this if-block will not execute if this module is imported.
    
    plt.close('all')  # Close all currently opened figure windows
    ### Add code below to test your functions ###
    # For each simulation case, set the initial conditions such that
    #  - the position of the blocks are in ascending order in the x positions array
    #  - the blocks initially do not overlap
    #  - the blocks should fit inside the bounding box
    
    #### Case A: 1 block for initial program development
    # Room size, block height/width/color, duration of time
    #ws = np.array([2.])   # array of one floating point value
    #hs = np.array([2.])
    #cs = ['brown']
    #ms = np.array([1.])
    #w = 10.
    #h = 5.
    #T = 10.
    #dt = 0.01
    
    # Initial position and velocity of block
    #xs = np.array([2.])
    #vxs = np.array([2.])
    
    # Draw
    #draw_blocks(xs, ws, hs, cs, w, h, "Draw 1 Block")

    
    #### Case B: 2 blocks for testing
   # xs = np.array([2., 6.])
    #ws = np.array([2., 2.])
    #cs = ['brown', 'slateblue']
    #vxs = np.array([0.0, -2.0])
    #ms = np.array([1.0, 1.0])
    #dt = 0.01
    #w = 10.0
    #h = 5.0
   # T = 15.0
    #draw_blocks(xs, ws, hs, cs, w, h, "Draw 2 Blocks")


    #### Include Simulation in testing
    #mu_k = 0.0  # No kinetic friction
    #e = 1.0     # Fully elastic collisions
    # simulate_motion(xs, vxs, ws, hs, ms, cs, dt, w, h, T, mu_k, e)
    
    
    ##### Case C: Fully elastic collisions, no kinetic friction
    # TODO: Write your case below to simulate 3 or more colliding
    # blocks of different sizes and masses.  mu_k = 0.01 and e = 1.0



    ##### Case D: Inelastic collisions and kinetic friction
    # TODO: Write your own case below to simulate 4 or more colliding
    # blocks of different sizes and masses. Try setting mu_k = 0.01
    # and e = 0.8 to test your implementation of kinetic friction and
    # inelastic collisions.
    # Four blocks with inelastic collisions and kinetic friction
xs = np.array([2., 5., 8., 11.])
ws = np.array([2., 2., 1., 1.5])
hs = np.array([2., 2., 2., 2.])
cs = ['brown', 'blue', 'green', 'red']
vxs = np.array([0.5, -1.0, 1.0, -0.5])
ms = np.array([1.0, 2.0, 0.5, 1.5])
dt = 0.01
w = 15.0
h = 5.0
T = 20.0
mu_k = 0.01  # Small kinetic friction
e = 0.8     # Inelastic collisions

simulate_motion(xs, vxs, ws, hs, ms, cs, dt, w, h, T, mu_k, e)


