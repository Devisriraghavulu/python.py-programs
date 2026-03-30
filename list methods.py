a=[1,2,3,34]
a.append(18)
print(a)

b=[1,2,34,45]
b.insert(1,55)
print(b)

a.remove(1)
print(a)

a.pop(1)
print(a.index(2))

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.clear()
print(a)