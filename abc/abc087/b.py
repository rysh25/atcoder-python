A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for a in range(A+1):
    for b in range(B+1):
        c = X - 500*a - 100*b
        if c >= 0 and c <= C*50:
            ans += 1

print(ans)

