auto = {
    "marca": "Audi",
    "model": "A4",
    "usi": 4
}

CAR_TEMPLATE = "Detin o masina marca: {} model: {} si are: {} usi."

print(CAR_TEMPLATE.format(
    auto["marca"], auto["model"], auto["usi"]
))

