def reverse_words(sentence):
    words = sentence.split()
    
    reversed_words = words[::-1]
    
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

input_sentence = input()
reversed_sentence = reverse_words(input_sentence)
print(f"{reversed_sentence}")
