import numpy as np
import matplotlib.pyplot as plt

l1 = 1.0
l2 = 1.5

x0 = 0
y0 = 0

joint_angle1 = 30 
joint_angle2 = 30

theta1 = joint_angle1*np.pi/180
theta2 = joint_angle2*np.pi/180

x1 = l1*np.cos(theta1)
y1 = l1*np.sin(theta1)
x2 = l2*np.cos(theta1+theta2)
y2 = l2*np.sin(theta1+theta2)

x = x1+x2
y = y1+y2

joint1 = plt.Circle((x0, y0), 0.025, color='r')
joint2 = plt.Circle((x1, y1), 0.025, color='r')
end_effector = plt.Circle((x, y), 0.025, color='r')

plt.ioff()
fig = plt.figure(1)
ax = fig.add_subplot(111)
        
ax.plot([x0, x1],[y0, y1])
ax.plot([x1, x],[y1, y])
ax.add_artist(joint1)
ax.add_artist(joint2)
ax.add_artist(end_effector)

ax.plot()
ax.set_xlim([-1,2])
ax.set_ylim([-1,2])
text = '('+str(round(x,3))+','+str(round(y,3))+')'
ax.text(x,y,text, fontsize=12)
plt.grid()
plt.show()





# plt.draw()
# plt.pause(10)
# ax.clear()




