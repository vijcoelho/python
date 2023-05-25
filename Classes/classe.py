class Pessoa:
  def __init__(self):
    self.name = input("\n\tEnter your name:")
    self.age = int(input("\n\tEnter your age:"))

  def hello(self):
    print("\nHello "+ self.name)

  def Age_verificator(self):
    if self.age < 18:
      print("\nYou cant enter in this concert, you are not 18.")
    else: print("\nYou can enter, go ahead.")
 

p1 = Pessoa()

p1.hello()

p1.Age_verificator()
