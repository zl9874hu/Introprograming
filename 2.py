list1=[1,2,3,4,5,6,7,8,9,0,33,23,23]
list2=['a','b','c','d','e','f','g','h','i','j','k','l']
print('list 1 is all numbers',list1)
print('list 2 is all letters',list2)
print('sum adds all the elements together',sum(list1))
list1.append(300)
print('.append adds an item or items to the end of a list.',list1)
list2.insert(2,'z')
print('.insert will insert an item in a list before the specicified position.',list2)
list1.remove(300)
print('.remove will remove the first item in a list that matches the specified item.',list1)
print('.pop() removes and returns the last item (or at specified index) in a list.',list2.pop(),list2)
list2.sort()
print('.sort will sort a list in an ascending order',list2)
list1.reverse()
print('.reverse will reverse the list',list1)
print('.index returns the index with the first item with the designated value.',list1.index(0))
print('.count counts the number of items with the esignated value.',list1.count(23))

