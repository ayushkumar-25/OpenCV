'''l = []
for i in range(int(input())):
    name = input()
    value = int(input())
    l.append([name, value])
print(l)'''
n = int(input())
l = [[input(), int(input())] for _ in range(2)]
print(l)
