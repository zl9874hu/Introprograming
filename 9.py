def letter_counter(string):
    vowels=['a','e','i','u']
    if ' ' in string:
        string=string.replace(' ','')
    num_lett=len(string)
    for letter in vowels:
        string=string.replace(letter,'')
    num_cons=len(string)
    num_vowels=num_lett-num_cons
    return num_vowels, num_cons

string=input('Please put in a string:')
vow,cons=letter_counter(string)
letter_counter(string)
print('There are',vow,'vowels, and',cons,'consonants.')
#Return and print/input done by Derek
