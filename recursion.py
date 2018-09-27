def power(x, y):
   if ((isinstance(x, str) or isinstance(y, str))):
       return 'error'
   if x == 0:
       return 0
   elif y == 0:
       return 1
   elif y < 0:
       y *= -1
       return 1/(x*power(x, y-1))
   else:
       return x*power(x, y-1)


print(power(2,4))
print(power('a', 'b'))
