import random


def rearrange_words(sentence):  # Fisher-Yates Shuffle Implemented.
    # get the length of the sentence being passed
    sentence_length = len(sentence) - 1
    for i in range(sentence_length, 0, -1):  # range(start, stop, step)
        random_num = random.randint(0, i)  # generates random number
        if random_num == i:
            continue
        # swap it index of words around - trade places
        sentence[i], sentence[random_num] = sentence[random_num], sentence[i]
    return sentence


def main():
    words_list = "How Now Brown Cow".split()
    print(rearrange_words(words_list))


if __name__ == "__main__":
    main()
