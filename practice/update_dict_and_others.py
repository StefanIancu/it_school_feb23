dic1 = {
    "name" : "Bogdan",
    "phone" : "6666",
    "email" : "N/A"
}

dic2 = {
    "name" : "Stefan",
    "phone" : "5555"
}

print(dic1)
# print(dic2)

dic1 |= dic2    #combine two dicts ---- cel din dreapta va face overwrite celui din stanga

print(dic1)
# print(dic2)

# for k, v in dic1.items():
#     print(k, v)

# for k in dic1.keys():
#     print(k)

# for v in dic1.values():
#     print(v)




    