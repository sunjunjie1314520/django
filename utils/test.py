
for i in range(1, 6):
    print(i)

list1 = {'e': '5465', 'a': '56464'}

print(list1)
print(sorted(list1))

a = ['{0}={1}'.format(row, list1[row]) for row in sorted(list1)]

print('&'.join(a))
