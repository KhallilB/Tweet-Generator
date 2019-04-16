import sampling
import histograms

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    source = 'gutenberg.txt'
    with open(source, 'r') as file:
        source = file.read()
    source_histogram = histograms.histogram_tuples(source=source)
    sentance = ''
    for i in range(10):
        sentance += ' ' + sampling.weighted_random_word(source_histogram)
    return sentance
