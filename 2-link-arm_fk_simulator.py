import numpy as np
import matplotlib.pyplot as plt

l1 = 1.0; l2 = 1.5
x0 = 0; y0 = 0

joint_angle1_list = [0,0,15,30,45,60] 
joint_angle2_list = [0,60,45,30,15,0]

theta_list = []

for theta1, theta2 in zip(joint_angle1_list, joint_angle2_list):
    theta_list.append([theta1*np.pi/180, theta2*np.pi/180])

print theta_list

for theta in theta_list:
    x1 = l1*np.cos(theta[0])
    y1 = l1*np.sin(theta[0])
    x2 = l2*np.cos(theta[0]+theta[1])
    y2 = l2*np.sin(theta[0]+theta[1])

    x = x1+x2
    y = y1+y2

    joint1 = plt.Circle((x0, y0), 0.025, color='r')
    joint2 = plt.Circle((x1, y1), 0.025, color='r')
    end_effector = plt.Circle((x, y), 0.025, color='r')

    plt.ion()
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    
    ax.plot([x0, x1],[y0, y1])
    ax.plot([x1, x],[y1, y])
    ax.add_artist(joint1)
    ax.add_artist(joint2)
    ax.add_artist(end_effector)

    ax.plot()
    ax.set_xlim([-1,3])
    ax.set_ylim([-1,3])
    text = '('+str(round(x,3))+','+str(round(y,3))+')'
    ax.text(x,y,text, fontsize=12)
    plt.grid()
    
    plt.draw()
    plt.pause(2)
    ax.clear()









