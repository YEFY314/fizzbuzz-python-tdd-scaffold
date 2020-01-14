def canBedivide(dividend, *dividor):
  result = True
  for i in dividor:
    if int(dividend) % int(i) !=0:
      result = False
  return result


def fizzBuzz(num=100):
  result = []
  for i in range(int(num)):
    i = i+1
    if canBedivide(i, 3, 5):
      temp = "FizzBuzz"
    elif canBedivide(i, 3):
      temp = "Fizz"
    elif canBedivide(i, 5):
      temp = "Buzz"
    else:
      temp = i
    print(temp)
    result.append(temp)
  return result

fizzBuzz()