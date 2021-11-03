n = int(input())
i = 0

while i <= n+1:
    if (2 ** i) <= (n*n):
        i += 1
    
    else:
        print(i-1)
        break

