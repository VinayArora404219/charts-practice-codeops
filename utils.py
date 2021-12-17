import matplotlib.pyplot as plt
import numpy as np


def draw_bar_chart(x_axis_list, y_axis_list, x_axis_label='', y_axis_label='', title='', font=None):
    """
    function that allows to draw bar chart easily

    :param x_axis_list: list of data to be shown on x-axis of bar graph
    :param y_axis_list: list of data to be shown on y-axis of bar graph
    :param x_axis_label: label on x-axis
    :param y_axis_label: label on y-axis
    :param title: Title of bar graph
    :param font: font of labels on either side of bar graph
    """
    x_axis_length = np.arange(len(x_axis_list))
    plt.bar(x_axis_length, y_axis_list, 0.4, label='Cryptocurrencies')
    plt.xticks(x_axis_length, x_axis_list)
    plt.xlabel(x_axis_label, fontdict=font)
    plt.ylabel(y_axis_label, fontdict=font)
    plt.title(title)
    plt.legend()
    plt.show()


def draw_pie_chart(labels, data, title=''):
    """
    function that allows to draw pie chart easily

    :param data: represents the array of data values to be plotted,
        the fractional area of each slice is represented by data/sum(data).
        If sum(data)<1, then the data values returns the fractional area directly,
        thus resulting pie will have empty wedge of size 1-sum(data).
    :param labels: labels is a list of sequence of strings which sets the label of each wedge.
    :param title: Title of pie chart
    """
    plt.pie(data, labels=labels, autopct='%1.2f%%')
    plt.title(title)
    plt.show()
