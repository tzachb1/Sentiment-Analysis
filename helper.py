import matplotlib.pyplot as plt

def plot_graph(x_values, y_values, title, xlabel=None, ylabel=None, type=None):
    # if x_values are string labels, convert it to integer range (and apply lables later with xticks)
    x_ticks_labels = None
    if isinstance(x_values[0], (basestring)):
        x_ticks_labels = list(x_values)
        x_values = range(1, len(x_ticks_labels)+1)

    if type is None:
        plt.plot(x_values, y_values)
    else:
        plt.plot(x_values, y_values, type)

    # set x ticks if they were string labels
    if x_ticks_labels is not None: plt.xticks(x_values, x_ticks_labels)

    plt.title(title)
    if xlabel is not None: plt.xlabel(xlabel)
    if ylabel is not None: plt.ylabel(ylabel)
    #x_dif = (x_values[-1] - x_values[0]) * 0.3
    #plt.xlim([x_values[0] - x_dif, x_values[-1] + x_dif])

    #y_dif = (max(y_values) - min(y_values)) * 0.3
    #plt.ylim([min(y_values) - y_dif, max(y_values) + y_dif])
    plt.margins(0.25)
    plt.show()

def plot_several(series_arr, legend_arr, title, xlabel, ylabel):
    for series in series_arr:
        plt.plot(series)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend(legend_arr, loc='best')
    plt.show()

