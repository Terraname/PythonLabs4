
# a = [1, 2, 3, 4, 5]
a = []
print("Enter N")
n = int(input())
for i in range(n):
    a.append(int(input()))
print(a)
b = []
for n in a:
    if n % 2 == 0:
        b.append(n)
print(b)
