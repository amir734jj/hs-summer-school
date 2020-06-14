def fahrenheit_to_celsius(n):
  raise Exception("Not implemented")

def celsius_to_fahrenheit(n):
  raise Exception("Not implemented")


for i in range(0, 100, 17):
  if celsius_to_fahrenheit(fahrenheit_to_celsius(i)) != i:
    raise Exception("Test failed")

print("Test passed")