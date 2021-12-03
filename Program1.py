'''
*********
PROGRAM 1
*********
Define a function number_of_odds that takes a list of integers as an argument. The function returns how an integer, how many odd numbers are in the list.
'''
def number_of_odds(lst):
  numodds = 0
  for i in lst:
    if i%2 != 0:
     numodds += 1
  return numodds
