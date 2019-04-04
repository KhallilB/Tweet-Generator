import random
import sys


def get_dict_words():
    '''
    Gets user words from system dictonary opens file 
    and splits it into a list
    '''
    with open('/usr/share/dict/words') as dictionary_file:
        # option of .readlines()
        dictionary_words = dictionary_file.read()

        return dictionary_words.splitlines()


def user_input():
    ''' only allows user to input a number'''
    user_input = sys.argv[1]
    if type(user_input) != 'int':
        return 'Enter a number.'
    else:
        return user_input


def arrange_random(input_num, list_words):
    '''
    Generates a random word list using words
    from file
    '''
    file_len = len(get_dict_words())
    words_list = []
    sentance = ""

    while input_num != 0:
        rand_num = random.randint(0, file_len)
        words_list.append(list_words[rand_num] + " ")
        list_words.pop(rand_num)
        input_num -= 1

    return sentance.join(words_list)


if __name__ == "__main__":
    list_words = get_dict_words()
    input_num = int(sys.argv[1])
    print(arrange_random(input_num, list_words))
