def fizzbuzz(n):
    fizzes = []
    buzzes = []
    fizzbuzzes = []
    printable = ""
    for i in range(1, n + 1):
        mod_3 = i % 3 == 0
        mod_5 = i % 5 == 0
        mod_35 = mod_3 and mod_5

        if mod_35:
            printable += "\nFizzBuzz"
            fizzbuzzes.append(i)
        elif mod_5:
            printable += "\nBuzz"
            buzzes.append(i)
        elif mod_3:
            printable += "\nFizz"
            fizzes.append(i)
        else:
            printable += f"\n{i}"

    return printable, fizzes, buzzes, fizzbuzzes


def reverse_str(str):
    if not str:
        return str
    return str[::-1]


def word_freq_counter(sentence):
    # Given a sentence, return a dict of how many times each word appears
    # Case-insensitive: "The" and "the" count as the same word

    dictionary = dict()

    if sentence:
        words = ""
        # clean up sentence - remove punctuations.
        for i, c in enumerate(sentence.upper()):
            if c.isalnum() or c.isspace():
                words += c

        for word in words.split():
            dictionary[word] = dictionary.get(word, 0) + 1

    return dictionary
