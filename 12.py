pig_latin=[]#creates empty list
sentence=input('Input your sentance.')
words=sentence.split(' ')#splits sentence into words
for i in range(len(words)):
    word= words[i]
    word= word[1:] + word[0] + "ay"
    pig_latin.append(word)
pig_latin=' '.join(pig_latin)
print(sentence)
print(pig_latin)
#Derek did loop and print
