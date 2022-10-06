import matplotlib.pyplot as plt
import rocket

min_angles_q3 = []
max_angles_q3= []
alpha_range= []
i=0.05

while i <= 0.321:
    alpha_range.append(i)
    min_angles_q3.append(rocket.launch_angle_range(2.0,i,0.04)[0])
    max_angles_q3.append(rocket.launch_angle_range(2.0,i,0.04)[1])
    i+=0.001

min_angles_q4 = []
max_angles_q4= []
ve_v0_range = []
j=1.41

while j <= 2.23607:
    ve_v0_range.append(j)
    min_angles_q4.append(rocket.launch_angle_range(j,0.25,0.04)[0])
    max_angles_q4.append(rocket.launch_angle_range(j,0.25,0.04)[1])
    j+=0.01 


print(alpha_range)
#print(min_angles_q3)
print(max_angles_q3)
#print(min_angles_q4)
#print(max_angles_q4)


plt.figure()
plt.plot(alpha_range,min_angles_q3,'r',label = 'Minimum')
plt.plot(alpha_range,max_angles_q3, label = 'Maximum')
plt.xlabel('alpha')
plt.ylabel('angle (degrees)')
plt.title('Alpha Value vs. Launch Angle for ve_v0 = 2.0 and tol_alpha = 0.04')
plt.legend()
plt.savefig('alpha_range.png')

plt.figure()
plt.plot(ve_v0_range,min_angles_q4, 'r',label = 'Minimum')
plt.plot(ve_v0_range,max_angles_q4, label = 'Maximum')
plt.xlabel('ve_v0_range')
plt.ylabel('angle (degrees)')
plt.title('Velocity Ratio Range vs. Launch Angle alpha = 0.25 and tol_alpha = 0.04')
plt.legend()
plt.savefig('ve_v0_range.png')

plt.show()