class AirplaneTicket:
    pass

#instantiere
tk1 = AirplaneTicket()
tk2 = AirplaneTicket()

print(type(tk1))
print(type(tk2))
print(type(AirplaneTicket))

print(isinstance(tk1, AirplaneTicket))
print(isinstance(AirplaneTicket, AirplaneTicket))

#stergere obiect
del tk1  
print(tk1)

