class employee:
    def __init__(self , role , dept , salary):
        self.role = role
        self.dept= dept 
        self.salary = salary

    def showDETAILS(self):
        print("role" , self.role)
        print("dept" , self.dept)
        print("salary" , self.salary)
    
class engineer(employee):
    def __init__(self, name , age):
        self.name = name
        self.age = age
        super().__init__("engineer" , "development" , 50000)

el = engineer("divyanshu" , 22 )
engineer.showDETAILS(el)


        

        