ticket = {
    "s_plecare": "Bucuresti Nord",
    "s_sosire": "Iasi",
    "data_plecare": "27.02.2023",
    "data_sosire": "27.02.2023",
    "ora_plecare": "19:30",
    "ora_sosire": "23:30",
    "pret": 98.45,
    "loc": True, 
    "vagon": "2",
    "scaun": "34"
}

print("=" * 70)
print("{:-^70}".format(ticket["s_plecare"]))
print("Data plecare:{:>57}".format(ticket["data_plecare"]))
print("Ora plecare:{:>58}".format(ticket["ora_plecare"]))
print("{:-^70}".format(ticket["s_sosire"]))
print("Data sosire:{:>58}".format(ticket["data_sosire"]))
print("Ora sosire:{:>59}".format(ticket["ora_sosire"]))

if ticket["loc"]:
    print("{:*^70}".format(" Detalii loc "))
    print("{:^68}".format(f"Vagon: {ticket['vagon']} "))
    print("{:^68}".format(f"Scaun: {ticket['scaun']} "))
    print("*" * 70)


print("=" * 70)
