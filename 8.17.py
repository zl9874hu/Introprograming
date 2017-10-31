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
    jer_num=int(input('Please put in jersey number:'))
    rank= int(input('Please input Rank:'))
    players[jer_num]= rank
    print()
    i+=1
sort_nums=sorted(players)#sorts players dictionary
print('ROSTER')
for player in sort_nums:#prints roster
    print('Jersey number: %d, '%player,end='')
    print('Rating:',players.get(player,'n/a'))
menu()
option=input('Choose an option:')
print('')
while option !='q':#list of options
    if option=='o':
          print('ROSTER')
          for player in sort_nums:
              print('Jersey number: %d, '%player,end='')
              print('Rating:',players.get(player,'n/a'))
    if option=='d':
        jer_num=int(input('Enter a jersey number'))
        del players[jer_num]
    if option=='u':
        jer_num=int(input('Enter a jersey number'))
        new_rank=int(input('Enter the new Rank:'))
        players[jer_num]=new_rank
    if option=='r':
        min_rank=int(input('Input minimum rank'))
        sort_nums=sorted(players)
        print()
        print('Above',min_rank)
        for player in sorted_nums:
            if min_rank<players(player):
                print('Jersey number: %d, '%player,end='')
                print('Rating:',players.get(player,'n/a'))
                
    if option=='a':
        jer_num= int(input('Please put in jersey number:'))
        rank= int(input('Please input Rank:\n'))
        players[jer_num]= rank
    menu()
    option=input('Choose an option:')  
#Finished menu loops and did roster printing-Derek
