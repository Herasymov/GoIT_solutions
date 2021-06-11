d = {}
d['Hello'] = 'World'
print(d)
d[1] = 2
print(d)
d['qwerty'] = 5
print(d)
d[(1, 3)] = 3
print(d)
d[2] = [1, 2]
print(d)
d[1] = 5
print(d)

print(d[1])
print(d.get(1, "Error"))
print(list(d.keys()))
print(list(d.values()))



