d = {'восток': 0, 'запад': 0, 'север': 0, 'юг': 0}
for i in range(int(input())):
    n = input().split()
    d[n[0]] += int(n[1])
print(d['восток'] - d['запад'], d['север'] - d['юг'], end=' ')