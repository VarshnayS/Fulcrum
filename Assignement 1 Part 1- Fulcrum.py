
#Part 1 using recursion:

# Defined the function, enabling me to call it back again in the middle of the code with the function '-1', so that the number of 'bottles' decreases to zero. 
# Conditions enabled me to print two separate statements for the conditions when there are no bottles left and when there are bottles left.

def drink_bottles_recursively(bottles):
  if bottles == 0:
    print('There are no bottles left')

  else:
    print('There are', bottles, 'left')
    drink_bottles_recursively(bottles - 1)

drink_bottles_recursively(99)

# #Part 1 using while loops:

#The while loop repeats until the value of 'bottle' is no longer greater than zero, after which it will break and enter the following if condition which will print that 'There are no bottles left'.

def drink_bottles_using_while_loops(bottles):
  while bottles > 0:
    print('There are', bottles, 'left')
    bottles -= 1

  if bottles == 0:
    print('There are no bottles left')


drink_bottles_using_while_loops(99)

#Part 1 using for loops:

#The for loop follows the range from 99 to 0 in decrementally through by -1, after which it will break the loop and print that 'There are no bottles left'

def drink_bottles_using_for_loops(bottles):
  for bottle in range(bottles, 0, -1):
    print('There are', bottle, 'bottles')
  print('There are no bottles left')


drink_bottles_using_for_loops(99)
