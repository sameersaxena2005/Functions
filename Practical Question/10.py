# Remove Vowels from a String Using filter():

def remove_vowels(s):
    return "".join(filter(lambda x: x.lower() not in "aeiou", s))

print(remove_vowels("Hello World"))
