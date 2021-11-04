row = int(input("Enter the no. of rows: "))
column = int(input("Enter the no. of columns: "))
stage = [[] for i in range(row)]
end = True

for i in range (row):
    for j in range (column):
        stage[i].append(input())

print(*stage, sep='\n')

for i in range(0, column):
    for j in range(1, row):
        if int(stage[j][i]) <= int(stage[j-1][i]):
            end = False
            break
    
if end == True : print('\n' "True")
else : print('\n' "False")
