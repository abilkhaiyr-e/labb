def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

user_input = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(user_input)
print("Reversed sentence:", reversed_sentence)