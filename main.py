
for numbs in range(0,101):
  if numbs % 3 == 0:
    if numbs % 5 == 0:
      print("FizzBuzz")
    else:
      print("Fizz")
  if numbs % 5 == 0:
    print("Buzz")
  else:
    print(numbs)
