import re


def histogram(source):
    # initializing empty dictionary
    histogram_dict = {}
    # split the source into seperate words
    # on whitespace then iterate over them
    for word in source.split():
        if word in histogram_dict:
            histogram_dict[word] += 1
        else:
            histogram_dict = 1

    return histogram_dict


def histogram_lists(source):
    # initilize empty list
    histogram_list = []
    # split the source into seperate words
    # on whitespace then iterate over them
    text = source.split()
    text.sort()
    while len(text) > 0:
        count = 0
        match = True
        index = len(text) - 1
        word = text[index]
        while match and index > 0:
            if word == text[index]:
                count += 1
                index -= 1
            else:
                match = False
        histogram_list.append([word, count])
        del text[-(count):]
    return histogram_list


def histogram_tuples(source):
    # initilize empty list
    histogram_tuple = []
    # split the source into seperate words
    # on whitespace then iterate over them
    text = source.split()
    text.sort()
    while len(text) > 0:
        count = 0
        match = True
        index = len(text) - 1
        word = text[index]
        while match and index > 0:
            if word == text[index]:
                count += 1
                index -= 1
            else:
                match = False
        histogram_tuple.append((word, count))
        del text[-(count):]
    return histogram_tuple


def remove_punctuation(pattern, source):
    for pat in pattern:
        return(re.findall(pat, source))


def unique_words(histogram):
    unique_entries = len(list(histogram))
    return unique_entries


def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return "Error: Word not found"


if __name__ == '__main__':
    file = open('gutenberg.txt', 'r')
    source = file.read()
    pattern = ['[^!.?]+']
    punc_translation = (" ".join(remove_punctuation(pattern, source)))
    # histogram
    text_histogram = histogram_lists(source=punc_translation)
    text_unique_words = unique_words(histogram=text_histogram)
    his_word_frequency = frequency(word="his", histogram=text_histogram)

    print('\'his\' appears {} times. Also we found {} unique words.'.format(
        his_word_frequency, text_unique_words))
