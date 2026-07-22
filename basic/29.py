class student:
    def __init__(self , name):
       self.name = name

    def average (self,marks1, marks2 ,marks3):
        self.average = (marks1+marks2+marks3)/3
        print(self.name ,"your average is:", self.average)

s1 = student("divyanshu")
s1.average(10,100,20)