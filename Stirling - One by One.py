import math

while True:
 try:
  number = float(input("Input number that you want to search it's inverse factorial :"))
  if number < 1:
   print("Input number bigger than 1")
  else:
   break
 except:
  print("Input integer number")

while True:
 try:
  digit_approx = int(input("Input want to have many digits behind the comma : "))
  if digit_approx < 1:
   print("Input number bigger than 1")
  else:
   break
 except:
  print("Input integer number")

res = 0
factor = 0

def f(x):
 return math.sqrt((2*x+1/3)*math.pi)*(x/math.e)**x

while factor<=digit_approx:
 if f(res) <= number:
  res = res + 10**(-factor)
 elif f(res) >= number:
   res = res-10**(-factor)
   factor += 1

print(f"The number is {res}")