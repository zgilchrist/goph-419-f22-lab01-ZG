"""Driver script for Assignment #1"""

import matplotlib.pyplot as plt
import numpy as np

import rocket

def main():
    """Main function"""
    ###########
    #Question 2
    ###########

    print('Computed value of min and max launch angles respectively:')
    print(rocket.launch_angle_range(2.0,0.25,0.02))
    print('\nTrue value of min and max laucnh angles computed using numpy:')

    ###########
    #Question 3
    ###########
    
    #initialize arrays for first figure
    min_angles_q3 = []
    max_angles_q3= []
    alpha_range= []
    i=0.05

    #iterate through values to get a range of plot values
    while i <= 0.321:
        alpha_range.append(i)
        min_angles_q3.append(rocket.launch_angle_range(2.0,i,0.04)[0])
        max_angles_q3.append(rocket.launch_angle_range(2.0,i,0.04)[1])
        i+=0.001
    
    #plot of alpha_range vs angle
    plt.figure()
    plt.plot(alpha_range,min_angles_q3,'r',label = 'Minimum')
    plt.plot(alpha_range,max_angles_q3, label = 'Maximum')
    plt.xlabel('alpha')
    plt.ylabel('angle (degrees)')
    plt.title('Alpha Value vs. Launch Angle for ve_v0 = 2.0 and tol_alpha = 0.04')
    plt.legend()
    plt.savefig('alpha_range.png')
    
    ############
    #Question #4
    ############
    
    #initialize arrays for second figure
    min_angles_q4 = []
    max_angles_q4= []
    ve_v0_range = []
    j=1.41

    #2.23607
    #iterate through values to get a range of plot values
    while j <= 2.2:
        ve_v0_range.append(j)
        min_angles_q4.append(rocket.launch_angle_range(j,0.25,0.04)[0])
        max_angles_q4.append(rocket.launch_angle_range(j,0.25,0.04)[1])
        j+=0.01 

    #plot of velocity ratio range vs angle
    plt.figure()
    plt.plot(ve_v0_range,min_angles_q4, 'r',label = 'Minimum')
    plt.plot(ve_v0_range,max_angles_q4, label = 'Maximum')
    plt.xlabel('ve_v0_range')
    plt.ylabel('angle (degrees)')
    plt.title('Velocity Ratio Range vs. Launch Angle for alpha = 0.25 and tol_alpha = 0.04')
    plt.legend()
    plt.savefig('ve_v0_range.png')

    plt.show()

if __name__ == "__main__":
        main()