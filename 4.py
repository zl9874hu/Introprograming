dict1={1:'a',2:'b',3:'c'}
dict2={3:9,4:'d',5:'e',6:'f'}
print(dict1,dict2)
print('get will return the value of a specified key an if it\
not exist it will print a desired message.',dict1.get(1,'N/A'), dict1.get(6,'N/A'))
print('pop will remove and returns the key value if the key\
does not exist itt will print a desired message.',dict1.pop(1,'N/A'),dict1)
dict1.update(dict2)
print('update merges two dictionaries and overwriting any keys from\
the original dictionary.',dict1)
dict2.clear()
print('clear empties a dictionary of its key-value pairs,',dict2)
