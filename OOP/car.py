class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price is: " + str(self.price)
        print "Speed: " +str(self.speed)
        print "Mileage: " +str(self.mileage)
        print "Fuel: " + self.fuel
        print "Tax: " + str(self.tax)
        return self
    
car1 = Car(88000,"120 mph","Full","22 mpg")
car1.display_all()

car2 = Car(2000,"50 mph","half","3 mpg")
car2.display_all()
