import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def clock(i):
    t = np.linspace(0,2*np.pi,1000)
    plt.clf()
    now = datetime.now()
    s = now.second*6
    m = now.minute*6 + now.second/10
    h = now.hour*30 + now.minute/2

    marker = [r'$ e^0 $', 
        r'$ \sqrt{4} $',
        r'$ \frac{d}{dt}3x $',
        r'$ 2^2 $',
        r'$ 10-5 $',
        r'$ 6x-4 = 32 $',
        r'$ \sqrt{49} $',
        r'$ \frac{16}{2} $',
        r'$ 3^2 $',
        r'$ 4+3 \times 2 $',
        r'$ \sqrt{121} $',
        r'$ 2 \times 3!  $']

    for i in range(1,13):
       plt.text(np.sin(i*np.pi/6)*0.85, np.cos(i*np.pi/6)*0.85, marker[i-1], horizontalalignment = 'center')

    plt.fill(np.cos(t),np.sin(t), 'fuchsia')
    plt.plot(np.cos(t),np.sin(t), 'k')

    # Hour
    plt.quiver(0,0,-np.cos(np.radians(90+h)), np.sin(np.radians(90+h)), scale = 7, headwidth = 0.1, headlength = 0.1)

    # Minute
    plt.quiver(0,0,-np.cos(np.radians(90+m)), np.sin(np.radians(90+m)),scale = 6, headwidth = 0.1, headlength = 0.1)

    # Second
    plt.quiver(0,0,-np.cos(np.radians(90+s)), np.sin(np.radians(90+s)), scale= 5, headwidth = 0.1, headlength = 0.1, width = 0.001)
    plt.axis('equal')
    plt.pause(0.99)
