#enter your count_vowels function here:

def count_vowels(input_string):
    output = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for letter in input_string:
        for vowel in output:
            if letter==vowel:
                output[vowel] += 1
    return output