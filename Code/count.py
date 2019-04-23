import dictogram


def generate(tokens):
    histogram = dictogram.Dictogram(tokens)
    return histogram
