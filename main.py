from graphing import plot_most_common
from word_analysis import open_text


def analysis():
    words, num_words, most_common = open_text()
    plot_most_common(most_common, num_words)


if __name__ == '__main__':
    analysis()
