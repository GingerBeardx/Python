class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print self.price, self.max_speed, self.miles
    def ride(self):
        print "Riding..."
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        return self
        
bike1 = Bike(200,"25 mph")
bike2 = Bike(300,"30 mph")
bike3 = Bike(250,"20 mph")

print bike1.ride().ride().ride().reverse().displayinfo()
print bike2.ride().ride().reverse().reverse().displayinfo()
print bike3.reverse().reverse().reverse().displayinfo()