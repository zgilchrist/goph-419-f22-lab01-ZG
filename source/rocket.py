from unittest import result
import math

import numpy

def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Description of function.
    Parameters
    ----------
    ve_v0: float
        The value of the ratio of escape velocity to initial velocity

    alpha: float
        Max altitude of rocket

    tol_alpha: float
        Alpha's level of tolerance.
    Returns
    -------
    array
        A tuple of min and max launch angles
    """
    
    #correct alpha for given tolerances for its min and max threshold
    alpha_min = alpha*(1 - tol_alpha)
    alpha_max = alpha*(1 + tol_alpha)

    under_root_min = (1-(alpha_min/(1+alpha_min))*(ve_v0**2)) 
    under_root_max = (1-(alpha_max/(1+alpha_max))*(ve_v0**2))

    assert under_root_max > 0 and under_root_min > 0, "Complex value found, ensure values under the root are positive"

    
    #if under_root_max < 0 or under_root_min < 0:
    #    print(under_root_max)
     #   print(under_root_min)
      #  return "Error, complex value detected, ensure that value under root is positive"

    right_side_min = (1+alpha_min)*numpy.sqrt(under_root_min)
    right_side_max = (1+alpha_max)*numpy.sqrt(under_root_max)
    
    phi_range = [arcsin(right_side_min),arcsin(right_side_max)]
    
    return phi_range

def arcsin(x):
    """Calculates value of arcsin(x) for a given x value.
    Parameters
    ----------
    x: float
        The argument of the arcsin function.
    Returns
    -------
    float
        The resultant value of the arcsin function.
    """
    #Check that i is greater than or equal to one
    result = 0
    sign = False
    eps_a = 1.0
    eps_s = 1.e-16
    n = 1
    fact_n = 1
    
    if x < 0:
        sign = True

    while eps_a > eps_s:
        numerator = (2*x)**(2*n)
        denominator = n**2*(factorial_2n(n))/(fact_n**2)
        term = numerator/denominator
        result += term
        n+=1
        fact_n *= n
        eps_a=abs(term/result)
    result = 0.5*result
    result = numpy.sqrt(result)

    if sign == True:
        result = -result


    return result

def factorial_2n(n):
    """Helper function for arcsin(x) to find the value of (2n)!
    Parameters
    ----------
    n: int
        The argument of (2n)!
    Returns
    -------
    int
        The resultant value of (2n)!
    """
    n*=2 #initialize n to be equal to 2n
    result = n #make initial value equal to n
    while n>1: #multiply initial n by (n-1) terms repeatably until n reaches 1 to get our result
        result*=(n-1)
        n-=1
    return result