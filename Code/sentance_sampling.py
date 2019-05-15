import dictogram
import queue
import random

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

def markov_path(token_list, order):
    markov_map = {}
    starting_items = []
    for n in range(order):
        starting_items.append(token_list[n])

    state_tracker = queue.Queue(size=order, items=starting_items)
    state = tuple(state_tracker.items())
    markov_map[state] = dictogram.Dictogram()

    for index in range(order, len(token_list)):
        new_token = token_list[index]
        state_tracker.enqueue(new_token)
        new_state = tuple(state_tracker.items())
        if new_state not in markov_map:
            markov_map[new_state] = dictogram.Dictogram()
        markov_map[state].add_count(new_state)
        state = new_state
    return markov_map

def markov_walk(path, distance, start_stop_tokens):
    sentence = ''
    START_TOKEN = start_stop_tokens[0]
    STOP_TOKEN = start_stop_tokens[1]

    state = (START_TOKEN)

    for step in range(distance):
        current_word = state[0]
        if current_word == START_TOKEN:
            keys = list(path.keys())
            start_states = []
            for entry in keys:
                if START_TOKEN == entry[0]:
                    start_states.append(entry)
            state = random.choice(start_states)
            set_of_possibities = path[state]
            state = word(set_of_possibities)
            current_word = state[0]
            current_word = current_word.capitalize()
            
        set_of_possibities = path[state]
        state = word(set_of_possibities)

        if current_word == STOP_TOKEN:
            sentence += '.'
        else:
            if current_word == 'i':
                sentence += ' ' + current_word.upper()
            else: 
                sentence += ' ' + current_word
    return sentence
