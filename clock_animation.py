import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import lateksii

if __name__ == '__main__':
    fig,ax = plt.subplots()
    animation = FuncAnimation(fig, lateksii.clock, 1)
    plt.show()

