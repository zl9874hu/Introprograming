encode_dict={'A':'Q','B':'W','C':'E','D':'R','E':'T','F':'Y',
     'H':'U','I':'I','J':'P','K':'A','L':'S','M':'D',
     'N':'F','O':'G','P':'H','Q':'J','R':'K','S':'L',
     'T':'Z','U':'X','V':'C','W':'V','X':'B','Y':'N','Z':'M'}
decode_dict={'M':'Z','N':'Y','B':'X','V':'W','C':'V',
              'X':'U','Z':'T','L':'S','K':'R','J':'Q','H':'P','G':'O',
              'F':'N','D':'M','S':'L','A':'K',
              'P':'J','I':'I','U':'H','Y':'F','T':'E',
              'R':'D','E':'C','W':'B','Q':'A'}#flips the key-value pairs of encode_dict
#Replaces alphabet with qwerty
def encode(sentence):#encodes the sentence
    encoded=[]#creates blank list
    string=sentence.replace(' ','-')#replaces spaces with a place holder
    string=string.upper()#turns letters to uppercase
    string=list(string)#splits string by letter
    for i in string:
        if encode_dict.get(i,'N/a') != 'N/a':#if the result of get is not n/a
            encoded.append(encode_dict.get(i,'N/a'))#adds the value of i to the dict
        else:
            encoded.append(i)#
    encoded=''.join(encoded)#joins the list
    encoded=encoded.replace('-',' ')#replaces - with a space
    return encoded
def decode(sentence):
    decoded=[]
    string=sentence.replace(' ','-')#replaces spaces with a place holder
    string=string.upper()#turns letters to uppercase
    string=list(string)#splits string by letter
    for i in string:
        if decode_dict.get(i,'N/a') != 'N/a':#if the result of get is not n/a
            decoded.append(decode_dict.get(i,'N/a'))#adds the value of i to the dict
        else:
            decoded.append(i)
    decoded=''.join(decoded)
    decoded=decoded.replace('-',' ')
    return decoded
option=input('1 for encoding\n\
2 for decode a previously encoded message\n\
3 to decode a new sentence\nq to quit\n:')#decided to make a menue
while option != 'q':#user quits by inputting q
    if option == '1':
        sentence=input('Enter a message you wish to encode.')
        print('Your message is:\n',sentence)
        encoded=encode(sentence)
        print('your coded message is:\n',encoded)
        option=input('1 for encoding\n\
2 for decode a previously encoded message\n\
3 to decode a new message\n\q to quit\n:')
    elif option == '2':
        sentence=encoded#is able to decode a previously encoded message
        print('your encoded message is:\n',encoded)
        decoded=decode(sentence)
        print('Your secret message is:\n',decoded)
        option=input('1 for encoding\n\
2 for decode a previously encoded message\n\
3 to decode a new message\nq to quit\n:')
    elif option == '3':
        sentence=input('Enter a message you wish to decode.')
        print('your encoded message is:\n',sentence)
        decoded=decode(sentence)
        print('Your secret message is:\n',decoded)
        option=input('1 for encoding\n\
2 for decode a previously encoded message\n\
3 to decode a new message\nq to quit\n:')
