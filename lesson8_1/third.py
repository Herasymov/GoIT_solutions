from datetime import time, datetime, timedelta, tzinfo
import pytz
d1 = datetime.now()
d2 = time(8, 15, 12, 0, pytz.UTC+2)
print(d2)
print(d1.strftime("%A/%B/%Y"))