import time

now = time.time()

now_tm = time.gmtime(now)

print(f"Evenimentul s-a intamplat in anul {now_tm.tm_year}, luna {now_tm.tm_mon}, ziua {now_tm.tm_mday}.")


print(time.strftime("Data %d.%m.%Y Ora %H:%M", now_tm))
print(time.strftime("%c", now_tm))
#08.12.2020 12:12