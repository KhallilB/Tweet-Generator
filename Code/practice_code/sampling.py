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
    while random_weight > 0:
        random_word = histogram[index][0]
        random_weight -= histogram[index][1]
        index += 1
    return random_word


def test_probability(histogram):
    words = ''
    for i in range(10000):
        words += ' ' + weighted_random_word(histogram=histogram)
    test_histogram = histograms.histogram_lists(words)
    sample_amount = 20
    index = len(test_histogram) - 1
    while sample_amount > 0 and index > 0:
        print_text = test_histogram[index][0][1]
        print_text += str(test_histogram[index][0])
        print(print_text)
        index -= 1
        sample_amount -= 1


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        source_text = file.read()
    source_histogram = histograms.histogram_lists(source=source_text)
    word = weighted_random_word(histogram=source_histogram)
    print(word)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    test_probability(histogram=source_histogram)
