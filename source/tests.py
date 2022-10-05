import rocket
import numpy as np

#test result #1
print("Calculated value: " )
print(rocket.launch_angle_range(2.0,0.25,0.02))
print("Expected value:")



#test result arcsin
print("Calculated value: " )
print(rocket.arcsin(0.1))
print("Expected value:")
print(np.arcsin(0.1))



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
    alpha_min = alpha*(1 - tol_alpha)
    alpha_max = alpha*(1 + tol_alpha)

    under_root_min = (1-(alpha_min/(1+alpha_min))*(ve_v0**2)) 
    under_root_max = (1-(alpha_max/(1+alpha_max))*(ve_v0**2))

    if under_root_max or under_root_min < 0:
        return "Error, complex value detected, ensure that value under root is positive"

    right_side_min = (1+alpha_min)*np.sqrt(under_root_min)
    right_side_max = (1+alpha_max)*np.sqrt(under_root_max)
    
    phi_range = [np.arcsin(right_side_min),np.arcsin(right_side_max)]
    
    return phi_range
def tester(ve_v0, alpha, tol_alpha):
    tol = 1e-8
    
    if abs(launch_angle_range(ve_v0, alpha, tol_alpha)[0] - rocket.launch_angle_range(ve_v0, alpha, tol_alpha)[0]) < tol:
        print(f"Success for conditions = {ve_v0, alpha, tol_alpha}.")
    else:
        print(f"Failed, expected : {launch_angle_range(ve_v0, alpha, tol_alpha)}, actual : {rocket.launch_angle_range(ve_v0, alpha, tol_alpha)}")

tester(2.0,0.25,0.02)