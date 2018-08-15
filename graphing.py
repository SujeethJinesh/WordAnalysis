import plotly.graph_objs as go
import plotly
from math import exp


def plot_most_common(most_common, num_words):
    number_of_most_common = 100

    keys = ["{} ({}%)".format(word, round(value / num_words * 100, 1)) for word, value in
            most_common.most_common(number_of_most_common)]
    values = [value for _, value in most_common.most_common(number_of_most_common)]

    line_data = go.Scatter(
        x=keys,
        y=values,
        name="# of Occurrences Trend"
    )

    bar_data = go.Bar(
        x=keys,
        y=values,
        name="# of Occurrences Visualized"
    )

    start_data_point = 2
    end_data_point = number_of_most_common - 1

    y1 = values[start_data_point]
    y2 = values[end_data_point - 1]
    y3 = values[int(end_data_point / 2)]
    x1 = start_data_point
    x2 = end_data_point
    x3 = int(end_data_point / 2)

    # y = alpha * e^-x + beta
    alpha = (y2 - y1) / (exp(-x2) - exp(-x1))
    beta = y1 - alpha * exp(-x1)
    # base = ((y3 - beta)/alpha)**-x3
    log_values = []

    for x in range(1, len(keys) + 1):
        log_values.append(alpha * exp(-x) + beta)

    log_data = go.Scatter(
        x=keys,
        y=log_values
    )

    data = [line_data, bar_data, log_data]

    plotly.offline.plot(data, filename='top_10_common_words.html')
