class Animal(object):
  def __init__(self, name):
    self.name = name
    self.health = 100
  def walk(self):
    self.health -= 1
    return self
  def run(self):
    self.health -= 5
    return self
  def display_health(self):
    print "Name: {}".format(self.name)
    print "Health: {}".format(self.health)
    return "******************************"

class Dog(Animal):
  def __init__(self, name):
    super(Dog, self).__init__(name)
    self.health = 150
  def pet(self):
    self.health += 5
    return self

class Dragon(Animal):
  def __init__(self, name):
    super(Dragon, self).__init__(name)
    self.health = 170
  def fly(self):
    self.health -= 10
    return self
  def display_health(self):
    print "I am a Dragon"
    super(Dragon, self).display_health()
    return "******************************"


animal1 = Animal("Fred")
print animal1.walk().walk().walk().run().run().display_health()

animal2 = Dog("Stitch")
print animal2.walk().walk().walk().run().run().pet().display_health()

anmial3 = Dragon("Balthazor")
print anmial3.fly().display_health()