class MathDojo(object):
  def __init__(self):
    self.results =  0
  def add(self, *nums):
    for num in nums:
      if isinstance(num, (list)):
        for exes in num:
          self.results += exes
      else:
        self.results += num
    return self
  def subtract(self, *nums):
    for num in nums:
      if isinstance(num, (list)):
        for exes in num:
          self.results -= exes
      else:
        self.results -= num
    return self
md1 = MathDojo()
# print md1.add(2).add(2,5).subtract(3,2).results

md2 = MathDojo()
print md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).results
