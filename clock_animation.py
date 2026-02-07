import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import lateksii
import seamaster

if __name__ == '__main__':
    fig = plt.figure() 
    animation = FuncAnimation(fig, lateksii.clock, 1)
    # animation = FuncAnimation(fig, seamaster.clock, 1)
    plt.show()
