
import dictogram
import random

START_TOKEN = '\u0391' # Greek 'Alpha'
STOP_TOKEN = '\u03a9' # Greek 'Omega'

def word(histogram):
    random_word = ''
    sum_of_weights = sum(histogram.values())
    random_weight = random.randrange(sum_of_weights)

    for key, value in histogram.items():
        if random_weight - value < 0:
            random_word = key
            break
        else:
            random_weight -= value
    
    return random_word

def markov_path(token_list):
    markov_map = {}
    previous_word = START_TOKEN
    for token in token_list:
        if token not in markov_map:
            markov_map[token] = dictogram.Dictogram()
        markov_map[previous_word].add_count(token)
        previous_word = token
    return markov_map

def markov_walk(path, distance):
    sentence = ''
    current_word = START_TOKEN
    for step in range(distance):
        if current_word == START_TOKEN:
            current_word = random.choice(list(path.keys()))
            current_word = current_word.capitalize()
        else:
            set_of_possibities = path[current_word]
            current_word = word(set_of_possibities)
        if current_word == STOP_TOKEN:
            sentence += '.'
        elif current_word != START_TOKEN:
            if current_word == 'i':
                sentence += ' ' + current_word.upper()
            else: 
                sentence += ' ' + current_word
            current_word = current_word.lower()
    return sentence
