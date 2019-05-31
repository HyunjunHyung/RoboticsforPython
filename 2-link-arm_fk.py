import numpy as np

l1 = 1.0
l2 = 1.5

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

print "x: ", x, "y: ", y