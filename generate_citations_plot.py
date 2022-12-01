import matplotlib.pyplot as plt
import numpy as np


with plt.xkcd():

    fig = plt.figure()
    
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))


    y = [3, 26, 37]
    x = ["2020", "2021", "2022"]

    ax.annotate(
        'HERE THE PHD IS DONE \nAND THE THALES ADVENTURE \nSTARTS',
        xy=("2021", 26), arrowprops=dict(arrowstyle='->'), xytext=("2021", 18))

    ax.annotate(
        'Total number of citations is ' + str(np.sum(y)),
        xy=("2020", 35), xytext=("2020", 35))


    ax.plot(x, y)

    fig.text(
        0.5, 0.05,
        'Citations over time, last updated december 2022',
        ha='center')

plt.savefig('assets/images/citations.png')
