from datetime import datetime
from time import strftime

# now = datetime.now()
# print(now)

now2 = strftime("%d.%m, %H:%M")
zbor = "22:30"
luna = "30.06"

start_time = datetime.strptime(now2, "%d.%m, %H:%M")
end_time = datetime.strptime(f"{luna}, {zbor}", "%d.%m, %H:%M")

delta = end_time - start_time

sec = delta.total_seconds()

hours = round(sec / (60 * 60))

print(f"Diferenta dintre {now2} si {luna}, {zbor} este de {hours} ore.")
print(hours <= 24)

