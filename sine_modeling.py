# Program source: https://www.geeksforgeeks.org/plotting-sine-and-cosine-graph-using-matloplib-in-python/

def plot_sine():
    #Importing required library
    import numpy as np
    import matplotlib.pyplot as plt

    # Creating x axis with range and y axis with Sine
    # Function for Plotting Sine Graph
    x = np.arange(0, 5*np.pi, 0.1)
    y = np.sin(x)

    # Plotting Sine Graph
    plt.plot(x, y, color='green')
    plt.show()

if __name__ == "__main__":
    plot_sine()