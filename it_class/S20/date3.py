import time


# event_time = "Data 12.04.2023 Ora 16:49"
# ev_tm = time.strptime(event_time, "%d.%M.%Y %H:%M")

ev1 = "20-02-2023 10:11"
ev2 = "22-02-2023 12:45"


ev1_tm = time.strptime(ev1, "%d-%m-%Y %H:%M")
ev2_tm = time.strptime(ev2, "%d-%m-%Y %H:%M")

# while True:
#     print("Extrag cursul euro")
#     time.sleep(10)
