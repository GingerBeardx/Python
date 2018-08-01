class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Milage: {}".format(self.milage)
        print "Tax: {}".format(self.tax)
        return "***********************"

car1 = Car(2000, "35 mph", "Full", "15mpg")
print car1.display_all()

car2 = Car(2000, "5 mph", "Not Full", "105mpg")
print car2.display_all()

car3 = Car(2000, "15 mph", "Kind of Full", "95mpg")
print car3.display_all()

car4 = Car(2000, "25 mph", "Full", "25mpg")
print car4.display_all()

car5 = Car(2000, "45 mph", "Empty", "25mpg")
print car5.display_all()

car6 = Car(20000000, "35 mph", "Empty", "15mpg")
print car6.display_all()