S = input()

c_count = 0
for i, s in enumerate(S):
    if i == 0:
        if s != "A":
            print("WA")
            exit()
    elif 2 <= i <= len(S) - 2:
        if s == "C":
            if c_count > 0:
                print("WA")
                exit()
            c_count += 1
    elif not s.islower():
        print("WA")
        exit()

if c_count == 0:
    print("WA")
    exit()

print("AC")
