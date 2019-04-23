import dictogram
import random


def weighted_word(histogram):
    random_word = ''
    weights = sum(histogram.values())
    random_weight = random.randrange(weights)

    for key, value in histogram.items():
        if random_weight - value < 0:
            random_word = key
            break
        else:
            random_weight -= value

    return random_word


def markov_chain(tokens):
    markov_chain = {}
    previous_word = None
    for token in tokens:
        if token not in markov_chain:
            markov_chain[token] = dictogram.Dictogram()
        if previous_word is not None:
            markov_chain[previous_word].add_count(token)
        previous_word = token
    return markov_chain


def markov_jump(link, length):
    sentance = ''
    current_word = None
    for _ in range(length):
        if current_word is None or len(link[current_word]) == 0:
            current_word = random.choice(list(link.keys()))
            sentance += ' ' + current_word
        else:
            possiblities = link[current_word]
            next_word = word(possiblities)
            sentance += ' ' + next_word
            current_word = next_word
        return sentance
