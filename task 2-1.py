list1 = list()
list2 = list()

print("Enter the corresponds to the 1st line: ")
for i in range (3): list1.append(input())

print("Enter the corresponds to the 2nd line: ")
for i in range (3): list2.append(input())

l1 = int(list1[0])/int(list1[1]) #first line
l2 = int(list2[0])/int(list2[1]) #second line

if l1 == l2: print("True")
else: print("False")
