#Сгенерировать словарь: {1:5, 2:4, 3:0, 4:2, 5:1}
print({i: 6-i if i != 3 else 0 for i in range(1, 6)})
#почему не катят такие методы?
d = {i: j for i in range(1, 6) for j in range(0, 5)}
print(d[0])
d2 = dict(zip(range(1, 6), range(0, 5))) # doesn't work
print(d, d2, sep='\n')
# Сгенерировать список[1, 2, 1, 1, 2, 3, 1, 2, 3]
#[1, 2, 1, 1, 2, 3, 1, 2, 3]
print([i % 3+1 if i != 2 else 1 for i in range(9)])
#discard vs remove
s = {1, 2, 3}
s.remove(2)

