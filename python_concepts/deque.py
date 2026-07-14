#A deque (double-ended queue) allows fast insertion and deletion from both ends.
#normal array This is O(n) because every element shifts.

from collections import deque

dq = deque([])


dq.append(2)
dq.appendleft(4)
dq.appendleft(3)
dq.append(5)

print(dq)