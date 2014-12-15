import splitStringFunction

sentence = "All good things comes to those who wait."
words = splitStringFunction.break_words(sentence)

# ['All', 'good', 'things', 'comes', 'to', 'those', 'who', 'wait.']
print(words)


sorted_words = splitStringFunction.sort_words(words)

#['All', 'comes', 'good', 'things', 'those', 'to', 'wait.', 'who']
print(sorted_words)

splitStringFunction.print_first_word(words)

splitStringFunction.print_last_word(words)


splitStringFunction.print_first_word(sorted_words)

splitStringFunction.print_last_word(sorted_words)
