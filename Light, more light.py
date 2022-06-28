# light-more-ligh
from math import sqrt

while True:
  num = int(input())
  if num == 0:
    break
  div = sqrt(num)
  print("yes" if div == int(div) else "no")

  /*
Input:-
3
6241
8191
0

Output:-
no
yes
no
*/
