class Car(object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def gas(self):
        if self.fuel == 100:
            print "Gas is full"
        if self.fuel < 100 and self.fuel > 50:
            print "Gas is more than halfway full"
        if self.fuel == 50:
            print "Gas is halfway full"
        if self.fuel < 50:
            print "Gas is less than halfway full"
        if self.fuel == 0:
            print "Gas is empty"
        return self
    def tax(self):
        if self.price > 10000:
            print "tax = .15"
        else: 
            print "tax = .12"
        return self
    def display_all(self):
        print self.price, self.speed,"mph", self.fuel, self.mileage,"mpg"
        return self


car1 = Car(10000, 120, 50, 30)
car1.tax().display_all().gas()

car2 = Car(50000, 160, 25, 15)
car2.tax().display_all().gas()

car3 = Car(30000, 140, 0, 20)
car3.tax().display_all().gas()

car4 = Car(5000, 90, 100, 15)
car4.tax().display_all().gas()

car5 = Car(40000, 130, 75, 18)
car5.tax().display_all().gas()

car6 = Car(35000, 160, 40, 12)
car6.tax().display_all().gas()
