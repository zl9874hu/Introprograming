translated_phone=[]#creates a blank list for use later
phone_num=input('What number you want to convert:')
while('-' not in phone_num) or (len(phone_num)!=12):#this forces the user to use the XXX-XXX-XXXX format
    phone_num=input("try again. phone numbers have 10 numbers and in \
XXX-XXX-XXXX format:")
phone_lower=phone_num.lower()#converts the phone number to lower thus preventing errors from capitalization
nums=list(phone_lower)
