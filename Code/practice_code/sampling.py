import random
import sys
import histograms


def random_word(histogram):
    '''Generates a random word without using weights'''
    random_word = ''
    random_index = random.randrange(len(histogram))
    random_word += histogram[random_index][0]
    return random_word


def weighted_random_word(histogram):
    '''Generates random words based on how often they appear'''
    random_word = ''
    weights = 0
    for items in histogram:
        weights += items[1]
    random_weight = random.randrange(weights)
    index = 0
    while random_weight >= 0:
        random_word = histogram[index][0]
        random_weight -= histogram[index][1]
        index += 1
    return random_word


def test_probability(histogram):
    ''' 
    Tests the probability of word ocurrances in
    the histogram that gets passed through
    '''
    words = ''
    for i in range(10000):
        words += ' ' + weighted_random_word(histogram=histogram)
    test_histogram = histograms.histogram_counts(words)
    sample_amount = 25
    index = len(test_histogram) - 1
    while sample_amount > 0 and index >= 0:
        for entry in test_histogram[index][1]:
            if sample_amount > 0:
                printline = entry + ' = '
                printline += str(test_histogram[index][0])
                print(printline)
                sample_amount -= 1
        index -= 1


if __name__ == '__main__':
    path = sys.argv[1]
    with open(path, 'r') as file:
        source_text = file.read()
    source_histogram = histograms.histogram_tuples(source=source_text)
    word = weighted_random_word(histogram=source_histogram)
    print(word)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    test_probability(source_histogram)
