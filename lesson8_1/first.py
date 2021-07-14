from datetime import datetime
d1 = datetime.now()
my_dict = {'milk': datetime(year=2021, month=6, day=30),
'butter': datetime(year=2021, month=8, day=2),
'jogurt': datetime(year=2021, month=7, day=12)}
answer = []
for key, val in my_dict.items():
    if val >= d1:
        answer.append(key)
print(answer)