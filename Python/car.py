

class car:
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else: 
            self.tax = 0.12
    def display_all(self):
        print (self.price, self.speed, self.fuel, self.mileage,self.tax)


car1 = car(20000,120,"regular",300000)
car2 = car(1000,120,"regular",300000)
car3 = car(45000,120,"regular",300000)
car4 = car(60000,120,"regular",300000)
car5 = car(100000,120,"regular",300000)
car6 = car(2000,120,"regular",300000)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()



        