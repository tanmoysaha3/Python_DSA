from collections import deque


def tribonacci1(self, n: int) -> int:
    queue = deque([0,1,1])
    if (n < 2):
        return queue[n]
    cout=3
    while(cout<=n):
        queue.append(sum(queue))
        queue.popleft()
        cout+=1
    return queue[-1]

n = 25
print(tribonacci1(0,n))


# Uisng List - Same memory on LC
def tribonacci2(self, n: int) -> int:
    queue = [0,1,1]
    cout=3
    while(cout<=n):
        queue.append(sum(queue))
        queue.pop(0)
        cout+=1
    return queue[-1]

n = 25
print(tribonacci1(0,n))