catalog = {
    "Ana": [10, 8, 8],
    "Marius": [6, 8, 7], 
    "Ion": [4, 5, 6]
}

# for v, k in catalog.items():
#     print(v, k)

for k, v in catalog.items():
    media = sum(v) / len(v)
    print(k, media)






