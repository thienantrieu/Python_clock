import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import latex_clock

if __name__ == '__main__':
    fig,ax = plt.subplots()
    animation = FuncAnimation(fig, latex_clock.clock, 1)
    plt.show()
