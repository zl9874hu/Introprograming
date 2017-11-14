class Employee:
    def __init__(self,name,id_num,dept,title):
        self.name=name
        self.id_num=id_num
        self.dept=dept
        self.title=title


susan=Employee('Serena Meyers','47899', 'Law', 'Vice President')
mark=Employee('Mathew Jones', '39119', 'IT', 'Phone Handler')
joy=Employee('Dayami Rogers', '81774', 'Manufacturing', 'Techinican')
employees=[susan , mark , joy]
for e in employees:
    print('Name:',e.name)
    print('ID:',e.id_num)
    print('Department:',e.dept)
    print('Title:',e.title)
    print()
