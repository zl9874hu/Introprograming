def letter_counter(string):
    vowels=['a','e','i','u']
    if ' ' in string:
        string=string.replace(' ','')
    num_lett=len(string)
    for letter in vowels:
        string=string.replace(letter,'')
    num_cons=len(string)
    num_vowels=num_lett-num_cons
