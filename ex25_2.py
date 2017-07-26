import ex25_1

sentence = "All good things come to those who wait."
words = ex25_1.break_words(sentence)
print words

sorted_words = ex25_1.sort_words(words)
print sorted_words

ex25_1.print_first_word(words)
ex25_1.print_last_word(words)

ex25_1.print_first_word(sorted_words)
ex25_1.print_last_word(sorted_words)

sorted_words = ex25_1.sort_sentence(sentence)
print sorted_words

ex25_1.print_first_and_last(sentence)
ex25_1.print_first_and_last_sorted(sentence)