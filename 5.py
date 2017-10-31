translated_phone=[]#creates a blank list for use later
phone_num=input('What number you want to convert:')
while('-' not in phone_num) or (len(phone_num)!=12):#this forces the user to use the XXX-XXX-XXXX format
    phone_num=input("try again. phone numbers have 10 numbers and in \
XXX-XXX-XXXX format:")
phone_lower=phone_num.lower()#converts the phone number to lower thus preventing errors from capitalization
nums=list(phone_lower)
for i in range(len(nums)):
    if nums[i] in 'abc':
        translated_phone.append('2')
    elif nums[i] in 'def':
        translated_phone.append('3')
    elif nums[i] in 'ghi':
        translated_phone.append('4')
    elif nums[i] in 'jkl':
        translated_phone.append('5')
    elif nums[i] in 'mno':
        translated_phone.append('6')
    elif nums[i] in 'pqrs':
        translated_phone.append('7')
    elif nums[i] in 'tuv':
        translated_phone.append('8')
    elif nums[i] in 'wxyz':
        translated_phone.append('9')
    else:
        translated_phone.append(nums[i])
#Loop by Derek
translated_phone=''.join(translated_phone)
print(phone_num)
print(translated_phone)
#print here by Derek
