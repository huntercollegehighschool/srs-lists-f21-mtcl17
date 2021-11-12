'''
*********
PROGRAM 2
*********
Define a function odd_reverse that takes a list as an argument. The function creates a new list containing only the elements in the odd indices (indices 1, 3, 5, ...) and then reverses it. The function returns that list.
'''
def odd_reverse(lst):
  listnew = []
  n = len(lst)-1
  while n>=0:
    if n%2 != 0:
      listnew.append(lst[n])
    n-=1
  return listnew
