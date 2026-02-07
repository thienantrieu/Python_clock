import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def clock(i):
    plt.clf()
    t = np.linspace(0,2*np.pi,100)

    plt.plot(np.cos(t),np.sin(t), color = 'k')
    plt.fill(np.cos(t),np.sin(t), color = (5/255, 4/255, 170/255))
    plt.text(0,-0.1, r'$ZrO_2$', horizontalalignment = 'center')

    for i in np.arange(0,1,0.1):
        l = np.linspace(-1+i,1-i,100)
        plt.plot(l,np.sin(10*t)/60+i,'k')
        plt.plot(l,np.sin(10*t)/60-i,'k')

    plt.text(0,0.6, r'$ \Omega$', color='w', size = 30, horizontalalignment = 'center')
    plt.text(0,0.5, 'Omega', color='w', size = 15, horizontalalignment = 'center')
    plt.text(0,0.25, 'Seamaster', color='w', size = 11,style = 'italic', horizontalalignment = 'center')
    plt.text(0,-0.4, 'CO-AXIAL', color='w', size = 10, horizontalalignment = 'center')
    plt.text(0, -0.5, 'MASTER CHRONOMETER', size = 10, color='w', horizontalalignment='center')
    plt.text(0, -0.6, '300m / 1000ft', size=10, color='w', horizontalalignment='center')

    for i in range(0,330,30):
        if i == 0:
            p = np.linspace(0.88,0.95,20)
            plt.plot(p,0*p,'w',linewidth =10)
        elif i == 180:
            p = np.linspace(-0.88,-0.95,20)
            plt.plot(p,0*p,'w', linewidth = 10)
        elif i == 90: 
            p = np.linspace(0.8,0.92,30)
            plt.plot(np.ones(p.shape)*0.032,p, 'w', linewidth = 10)
            plt.plot(np.ones(p.shape)*-0.032,p, 'w', linewidth = 10)
        elif i == 270:
            p = np.linspace(-0.95, -0.92, 20)
            plt.plot(0*p,p,'w', linewidth = 10)
        else:
            plt.plot(np.cos(np.deg2rad(i))*0.9,np.sin(np.deg2rad(i))*0.9,'wo',linewidth = 12)

    now = datetime.now()
    paiva = now.strftime("%d")
    s = now.second*6
    m = now.minute*6 + now.second/10
    h = now.hour*30 + now.minute/2

    # Day
    plt.text(0, -0.8, paiva,backgroundcolor = 'w',horizontalalignment = 'center')

    # Hour
    plt.quiver(0,0,-np.cos(np.radians(90+h)), np.sin(np.radians(90+h)), scale = 7, color = 'w',width = 0.01)

    # Minute
    plt.quiver(0,0,-np.cos(np.radians(90+m)), np.sin(np.radians(90+m)),scale = 6,color ='w', width = 0.01)

    # Second
    plt.quiver(0,0,-np.cos(np.radians(90+s)), np.sin(np.radians(90+s)), scale= 5, headwidth = 0.1, headlength = 0.1, width = 0.001, color = 'r')
    plt.axis('equal')
