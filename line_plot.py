import pandas as pd
import matplotlib.pyplot as plt

def line_plot(df, name):
    fig = plt.figure()
    fig.set_figwidth(11)
    plt.margins(x=0.009)
    plt.plot(df, color = 'red')
    plt.ylabel('Price')
    plt.xlabel('Trading Day')
    plt.title(f'Price for {name} over time')
    plt.savefig(f'Graphs\{name}')
    plt.close()