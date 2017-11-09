class Employee:
    def __init__(self,name,id_num,dept,title):
        self.name=name
        self.id_num=id_num
        self.dept=dept
        self.title=title


susan=Employee('Susan Meyers','47899', 'Accounting', 'Vice President')
mark=Employee('Mark Jones', '39119', 'IT', 'Programmer')
joy=Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
employees=[susan , mark , joy]
for e in employees:
    print('Name:',e.name)
    print('ID:',e.id_num)
    print('Department:',e.dept)
    print('Title:',e.title)
    print()
