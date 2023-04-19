from datetime import datetime, timedelta

now = datetime.now()

ev1 = datetime(1998, 2, 28)

print(ev1.strftime("%a"))

delta = now - ev1 

# delta.days
# delta.total_seconds()
