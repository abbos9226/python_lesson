def reverse_string(text):
    reversed=''
    for a in text:
        reversed=a+reversed
    print(reversed)

def count_vowels(word):
    vowels = ['a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O']  # List of vowels
    count = 0
    for char in word:  
        if char in vowels:  
            count += 1
    return count

