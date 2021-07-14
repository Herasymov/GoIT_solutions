from datetime import datetime, timedelta
d1 = datetime.now()
count = 0
while datetime.now() - d1 <= timedelta(seconds=5):
    count += 1
print(count)