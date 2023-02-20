print("Very short quiz game made by STI on 17-02-2023:)")

nume = input("Numele tau este: ")

print("Salut " + nume + ", te rugam sa raspunzi cu 'T' (True) sau 'F' (False) la urmatoarele intrebari:")
print("Quiz-ul va cuprinde 5 intrebari scurte, deci nu ar trebui sa dureze mult!")


lista_intrebari = [
    "Ai peste 16 ani?", 
    "Asculti muzica?",
    "Iti plac filmele?",
    "Mergi in parc?",
    "Desenezi des?"
]


lista_raspunsuri = [
    ["T", "F"]
]

lista_puncte = []

for intrebare in lista_intrebari:
    print("=" * 20)
    print()
    print(intrebare)

    raspuns_1 = input("Raspuns: ")
    for valoare in lista_raspunsuri:
    
        if raspuns_1 == valoare[0]:
            print("Super, ai un punct!")
            lista_puncte.append("*")
    
        else:
            print("Mergem mai departe!")

print()
print("Multumim, " + nume + "! Ai acumulat " + str(len(lista_puncte)) + " puncte.")
print()

print("Jocul a luat sfarsit!")









