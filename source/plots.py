import matplotlib.pyplot as plt
import rocket

min_angles_q3 = []
max_angles_q3= []
alpha_range= []
i=0.1

while i <= 1:
    alpha_range.append(i)
    min_angles_q3.append(rocket.launch_angle_range(2.0,i,0.04)[0])
    max_angles_q3.append(rocket.launch_angle_range(2.0,i,0.04)[1])
    i+=0.1

min_angles_q4 = []
max_angles_q4= []
ve_v0_range = []
j=2.0

while j <= 10:
    ve_v0_range.append(j)
    min_angles_q4.append(rocket.launch_angle_range(j,0.25,0.04)[0])
    max_angles_q4.append(rocket.launch_angle_range(j,0.25,0.04)[1])
    j+=0.1


print(alpha_range)
plt.subplot(111)
plt.plot(min_angles_q3,alpha_range,'ro')
plt.plot(max_angles_q3,alpha_range)

plt.subplot(112)
plt.plot(min_angles_q4,ve_v0_range)
plt.plot(max_angles_q4,ve_v0_range)
plt.ylabel('alpha')
plt.xlabel('angle (degrees)')
plt.show()