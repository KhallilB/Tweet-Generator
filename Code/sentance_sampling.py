import dictogram
import random


def weighted_word(histogram):
    random_word = ''
    total_of_weights = sum(histogram.values())
    random_weight = random.randrange(total_of_weights)

    for key, value in histogram.items():
        if random_weight - value < 0:
            random_word = key
            break
        else:
            random_weight -= value

    return random_word


def markov_chain(tokens):
    markov_links = {}
    previous_word = None
    for token in tokens:
        if token not in markov_links:
            markov_links[token] = dictogram.Dictogram()
        if previous_word is not None:
            markov_links[previous_word].add_count(token)
        previous_word = token
    return markov_links


def markov_jump(link, length):
    sentence = ''
    current_word = None
    for _ in range(length):
        if current_word is None or len(link[current_word]) == 0:
            current_word = random.choice(list(link.keys()))
            sentence += ' ' + current_word
        else:
            set_of_possibities = link[current_word]
            next_word = weighted_word(set_of_possibities)
            sentence += ' ' + next_word
            current_word = next_word

    return sentence
