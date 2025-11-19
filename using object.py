class Person( object): 
    def __init__(self, name, id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print(self.name)
        print(self.id_number)
class Employer(Person):   
    def __init__(self, name, id_number, salary, post):
        self.salary=salary
        self.post=post
        Person.__init__(self, name, id_number)     

a=Employer('rahul',886012, 20000, 'intern')
a.display()