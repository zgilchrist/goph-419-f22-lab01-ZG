import numpy as np

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

    #calculate values under the RHS root
    under_root_min = (1-(alpha_min/(1+alpha_min))*(ve_v0**2)) 
    under_root_max = (1-(alpha_max/(1+alpha_max))*(ve_v0**2))

    #Check for negative values under root and exit program if found
    assert under_root_max > 0 and under_root_min > 0, "Complex value found, ensure values under the root are positive"

    #Compute value on RHS of equation in full using numpy.sqrt
    right_side_min = (1+alpha_min)*np.sqrt(under_root_min)
    right_side_max = (1+alpha_max)*np.sqrt(under_root_max)
    
    #Enforce parameters of launch constraints and exit gracefully otherwise
    assert right_side_min <= 1 and right_side_min > 0, 'Values passed to arcsin function must be less than 1 and greater than 0 for acceptable launch constraints' 
    assert right_side_max <= 1 and right_side_max > 0, 'Values passed to arcsin function must be less than 1 and greater than 0 for acceptable launch constraints' 
    
    #Calls arcsin function to calculate angle of launch and uses min and max alpha to place min and max angle into a numpy array of length 2
    phi_range = np.array([arcsin(right_side_min),arcsin(right_side_max)])
    
    #Return array to caller
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
    #Initialize loop variables
    result = 0
    sign = False
    eps_a = 1.0
    eps_s = 1.e-5
    n = 1
    fact_n = 1
    
    #converts x to positive for purposes of the loop algorithm
    if x < 0:
        sign = True
        x =- x

    #loop that ends once the stopping criterion of five digits is met
    while eps_a > eps_s:
        numerator = (2*x)**(2*n)
        denominator = n**2*(factorial_2n(n))/(fact_n**2)
        term = numerator/denominator
        result += term
        n += 1
        fact_n *= n
        eps_a = abs(term/result)
    result = 0.5*result
    result = np.sqrt(result)

    #converts x back to negative if it was negative in the first place
    if sign == True:
        result = -result

    #return result to caller
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
    n *= 2 #initialize n to be equal to 2n
    result = n #make initial value equal to n
    while n > 1: #multiply initial n by (n-1) terms repeatably until n reaches 1 to get our result
        result *= (n-1)
        n -= 1
    return result