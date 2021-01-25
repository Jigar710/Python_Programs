class Celsius:
 a = 100
 def __init__(self, temperature=0):
  self.temperature = temperature

 def to_fahrenheit(self):
  return (self.temperature * 1.8) + 32
	
human = Celsius()
lst = dir(human)
print(lst)

print(human.__dict__)
print(human.__dict__['temp'])

d = {'a':100}
print(d['a'])