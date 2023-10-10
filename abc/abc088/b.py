N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

alice = 0
bob = 0
for i, a in enumerate(A):
    if i % 2 == 0:
        alice += a
    else:
        bob += a

print(alice - bob)
