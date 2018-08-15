import codecs
import nltk
from collections import Counter
import pickle


def open_text(filename='war-and-peace.txt'):
    try:
        with open('processed_dict.pickle', 'rb') as handle:
            words = pickle.load(handle)
        with open('num_words.pickle', 'rb') as handle:
            num_words = pickle.load(handle)
    except (OSError, IOError) as e:
        words = {}
        num_words = 0
        with codecs.open(filename, encoding='utf-8') as text:
            for line in text:
                line = line.encode('ascii', 'ignore')
                for word in nltk.word_tokenize(line.decode('utf-8').lower()):
                    if word.isalpha():
                        num_words += 1
                        if word in words.keys():
                            words[word] += 1
                        else:
                            words[word] = 1

        with open('processed_dict.pickle', 'wb') as handle:
            pickle.dump(words, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open('num_words.pickle', 'wb') as handle:
            pickle.dump(num_words, handle, protocol=pickle.HIGHEST_PROTOCOL)

    most_common = Counter(words)
    return words, num_words, most_common
