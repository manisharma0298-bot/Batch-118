# marks=[90,55,33,22,78,99,20,80,70,40,30]
# for i in range(len(marks)):
#     if marks[i] % 2 == 0:
#         print(marks[i])

number = int(input("Enter the number:"))
i = 0
while i < 11:
    print(number * i)
    i += 1

for i in range(1, 20, 2):
    print(i, end=" ")
