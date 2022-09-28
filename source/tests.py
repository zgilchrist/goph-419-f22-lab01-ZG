import rocket
import numpy

#test result #1
print("Calculated value: " )
print(rocket.launch_angle_range(2.0,-0.25,0.02))
print("Expected value:")



#test result #2
print("Calculated value: " )
print(rocket.arcsin(10,0.1))
print("Expected value:")
print(numpy.arcsin(0.1))