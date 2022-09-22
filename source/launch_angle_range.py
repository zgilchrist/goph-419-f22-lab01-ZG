from unittest import result
import math

import numpy

def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Description of function.
    Parameters
    ----------
    Returns
    -------
    """
    phi_range = 0
    right_side = (1+alpha)*numpy.sqrt(1-(alpha/(1+alpha))*(ve_v0**2))
    return phi_range

def arcsin(n,x):
    """Description of function.
    Parameters
    ----------
    Returns
    -------
    """
    #Check that i is greater than or equal to one
    result = 0
    sign = False
    
    if x < 0:
        sign = True

    for i in range(1,n+1):
        denominator = i**2*((math.factorial(2*i))/((math.factorial(i))**2))
        numerator = (2*x)**(2*i)
        result +=numerator/denominator
    result = 0.5*result
    result = numpy.sqrt(result)

    if sign == True:
        result = -result


    return result

def main():
    """Main function"""
    print("Hello World!, This is the start of assignment #1")
    print(arcsin(10,-.4))
    print(numpy.arcsin(-.4))

if __name__ == "__main__":
    main()