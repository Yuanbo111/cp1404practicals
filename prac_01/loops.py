# . Odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Print n stars on one line
n = int(input("Number of stars: "))
for i in range(n):
    print("*", end='')
print()

# d. Print n lines of increasing stars
number = int(input("Enter a number: "))

for i in range(1, number + 1):
    print('*' * i)