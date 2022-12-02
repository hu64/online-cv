import matplotlib.pyplot as plt
import numpy as np


with plt.xkcd():

    fig = plt.figure()
    
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))


    citations_by_year = [3, 26, 37]
    y = np.cumsum(citations_by_year)
    x = ["2020", "2021", "2022"]

    ax.annotate(
        'HERE THE PHD IS \nDONE AND THE THALES \nADVENTURE STARTS',
        xy=("2021", 29), arrowprops=dict(arrowstyle='->'), xytext=("2021", 15))

    # ax.annotate(
    #     'Total number of citations is ' + str(np.sum(y)),
    #     xy=("2020", 35), xytext=("2020", 35))


    ax.plot(x, y)

    fig.text(
        0.5, 0.05,
        'Citations accumulated over time \nLast updated december 2022',
        ha='center')

plt.savefig('assets/images/citations.png')
