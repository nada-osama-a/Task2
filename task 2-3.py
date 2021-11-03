n = int(input("Enter the number of elements you want in your list: "))
num = []
even = 0
odd = 0

for i in range(n):
    num.append(input())


for i in num[:]:
    if int(i) % 2 == 0:
        even += int(i)
        
    else: odd += int(i)

ans = [even, odd]
print(ans)
