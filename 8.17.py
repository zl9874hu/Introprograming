def menu():#function for printing the menu
    print()
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print('')
players={}#blank dcitonary
i=1#loop varible
while i <= 5:
sort_nums=sorted(players)#sorts players dictionary
print('ROSTER')
for player in sort_nums:#prints roster
menu()
option=input('Choose an option:')
print('')
while option !='q':#list of options
    if option=='o':
    if option=='d':
    if option=='u':
    if option=='r':
    if option=='a':
