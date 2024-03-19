# write a program that automatically prints the solution to the FizzBuzz game. 
target=100
for number in range(1, target+1):
  #print(number)
  if number % 3 ==0:
    if number % 5 ==0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif number % 5 ==0:
    print("Buzz")
  else:
    print(number)
    
