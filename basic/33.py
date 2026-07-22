class order:
    def __init__(self , name , price):
        self.name = name
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

o1 = order("order1" , 1000)
o2 = order("order2" , 200)
print(o1 > o2)        
