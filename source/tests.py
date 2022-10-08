import numpy as np

import rocket

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

    assert under_root_max > 0 and under_root_min > 0, "Complex value found, ensure values under the root are positive"

    right_side_min = (1+alpha_min)*np.sqrt(under_root_min)
    right_side_max = (1+alpha_max)*np.sqrt(under_root_max)
    
    phi_range = [np.arcsin(right_side_min),np.arcsin(right_side_max)]
    
    return phi_range
def tester(ve_v0, alpha, tol_alpha):
    tol = 1e-4
    
    if abs(launch_angle_range(ve_v0, alpha, tol_alpha)[0] - rocket.launch_angle_range(ve_v0, alpha, tol_alpha)[0]) < tol:
        print(f"Success for conditions = {ve_v0, alpha, tol_alpha}.")
    else:
        print(f"Failed, expected : {launch_angle_range(ve_v0, alpha, tol_alpha)}, actual : {rocket.launch_angle_range(ve_v0, alpha, tol_alpha)}")

tester(2.0,0.25,0.02)
tester(3,0.1,.04)
tester(5,0.1,.04) #supposed to fail here

#test result launch
print("Calculated value of angle range: " )
print(rocket.launch_angle_range(2.0,0.25,0.02))
print("Expected value or angle range:")
print(launch_angle_range(2.0,0.25,0.02))


#test result arcsin
print("Calculated value of arcsin() to five correct digits: " )
print(rocket.arcsin(0.1))
print("Expected value of arcsin():")
print(np.arcsin(0.1))