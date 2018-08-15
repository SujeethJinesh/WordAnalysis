import plotly.graph_objs as go
import plotly


def plot_most_common(most_common, num_words):
    number_of_most_common = 100

    keys = ["{} ({}%)".format(word, round(value / num_words * 100, 2)) for word, value in
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

    start_data_point = 0
    log_values = []

    for x in range(1, len(keys) + 1):
        log_values.append(values[start_data_point]/x)

    log_data = go.Scatter(
        x=keys,
        y=log_values,
        name="Expected Theoretical"
    )

    data = [line_data, bar_data, log_data]

    plotly.offline.plot(data, filename='top_x_common_words.html')
