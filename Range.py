##1)To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.


for x in range(2, 6):
  print(x)

##2))The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Example
# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

  #####3))
for x in range(6):
  print(x)
else:
  print("Finally finished!")

###4)))
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.


##################5))))))
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
