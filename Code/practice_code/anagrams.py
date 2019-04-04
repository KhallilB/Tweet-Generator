def words_list():
    '''gets words to use'''

    words = {}  # storing the words in a dictionary

    with open('/usr/share/dict/words') as f:
        for line in f:
            word = line.strip()
            words[word] = 1

        return words


def anagram_dict(words):
    '''
    splitting words into a list and checking list if they
    sort more than one word, if so that is added to anagram
    dictionary which will be used as keys
    '''

    anagram_dict = {}

    for word in words:
        # breaking string into a list and then sorting them alphabetically then join them
        sorted_word = ''.join(sorted(list(word)))
        # appending word to list if they match
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    return anagram_dict


def anagrams_from_dict(word, anagram_dict):
    '''
    checks the list for key pairs with more than 2
    values, returns true. If only one key value pair
    returns false
    '''

    key = ''.join(sorted(list(word)))

    if key in anagram_dict:
        values = anagram_dict[key]
        if len(values) >= 2:
            return True
    return False


def get_all_anagrams(words, anagram_dict):
    '''
    checks if a word is an anagram it saves
    it to a list.
    '''

    anagrams = []  # saving anagrams in list

    for word in words:
        if anagrams_from_dict(word, anagram_dict):
            anagrams.append(word)
    return anagrams


def find_anagrams(word, anagram_dict):
    '''finds key returns a set of anagrams'''

    key = ''.join(sorted(list(word)))
    if key in anagram_dict:
        return set(anagram_dict[key]).difference(set([word]))

    return set([])


word_dict = words_list()
test_anagram_dict = anagram_dict(word_dict.keys())

everything = get_all_anagrams(word_dict, test_anagram_dict)
print(everything)
print(len(everything), 'ANAGRAMS!')

daKeys = 'organ'
print('the anagrams of', daKeys, 'are',
      find_anagrams(daKeys, test_anagram_dict))
