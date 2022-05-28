class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def m_name(self):
    print("Hello my name is " + self.name)
    
  def m_age(self):
    print("Hello my name is " + str(self.age))

p1 = Person("John", 36)
p1.m_name()
p1.m_age()