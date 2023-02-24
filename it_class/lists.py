# list = [324, 345, 536, 64]

# print(list[3])

# print(len(list))

# print(list[len(list) -1])  # pt a obtine ultimul element din lista respectiva 

# print(list[-1]) #iei elementele de la coada catre capat: -1 ultimul, -2 penultimul etc.

# index_dorit = 3

# if len(list) < index_dorit:
#      print("elementul de pe pozitia", index_dorit, "este", list[index_dorit])
# else:
#      print("Indexul", index_dorit, "nu exista")

# print("END")


# for i in list:
#     print(i)

# lista_indx = range(len(list))

# # for i in lista_indx:
# #     print("Index", i, " Valoarea:", list[i])


# for i in enumerate(list):
#     print("Index", i[0], " Valoarea:", i[1])



# print(list)
# del list[0]
# print(list)


# list1=[]

# print(list1)
# print(len(list1))

# list1.append("Stefan")

# print(list1)
# print(len(list1))

# lista0 = []
# alfabet = range(65, 91)

# # for litera in alfabet:
# #     print(litera, end=' ')

# for element in alfabet:
#     lista0.append(chr(element))

# print(lista0)


# REMOVE


# temp = [12, 22, 31, 41, 22, 0]
# to_remove = 22

# print(to_remove in temp)   #asa verifici daca un element exista intr-o lista

# while to_remove in temp:
#     temp.remove(to_remove)

# print(temp)

# if 0 in temp:
#     print("S-a produs inghet!")



# COUNT

# temp = [22, 12, 32, 22, 0]

# verifier = 22

# print(verifier, "apare de ", temp.count(22), "ori")

# if 22 in temp:
#     print("Afara e canicula")
#     if temp.count(22) > 1:
#         print("E canicula mereu!")


# REVERSE

# temp1 = temp.copy()
# temp1.reverse()

# print(temp)
# print(temp1)



# MIN - MAX 

# print("Temperatura maxima este ", max(temp))
# print("Temperatura minima este " , min(temp))


# students = ["Mihai", "Andrei", "Maria"]
# temp = [22, 12, 32, 22, 0]


# # print(max(students))
# # print(min(students))

# # SORTED FUNCTION AND .SORT METHOD 

# # temp_sorted = sorted(temp)

# # print(temp)
# # print(temp_sorted)

# #pt descendent = sorted(temp, reverse=True)

# temp.sort()

# print(temp)

# words = ['Python', 'is', 'an', 'easy', 'to', 'learn', 'powerful', 'programming', 'language', 'It', 'has', 'efficient', 'high-level', 'data', 'structures', 'and', 'a', 'simple', 'but', 'effective', 'approach', 'to', 'object-oriented', 'programming', 'Python’s', 'elegant', 'syntax', 'and', 'dynamic', 'typing', 'together', 'with', 'its', 'interpreted', 'nature', 'make', 'it', 'an', 'ideal', 'language', 'for', 'scripting', 'and', 'rapid', 'application', 'development', 'in', 'many', 'areas', 'on', 'most', 'platforms', 'The', 'Python', 'interpreter', 'and', 'the', 'extensive', 'standard', 'library', 'are', 'freely', 'available', 'in', 'source', 'or', 'binary', 'form', 'for', 'all', 'major', 'platforms', 'from', 'the', 'Python', 'web', 'site', 'https://www.python.org', 'and', 'may', 'be', 'freely', 'distributed', 'The', 'same', 'site', 'also', 'contains', 'distributions', 'of', 'and', 'pointers', 'to', 'many', 'free', 'third', 'party', 'Python', 'modules', 'programs', 'and', 'tools', 'and', 'additional', 'documentation', 'The', 'Python', 'interpreter', 'is', 'easily', 'extended', 'with', 'new', 'functions', 'and', 'data', 'types', 'implemented', 'in', 'C', 'or', 'C++', '(or', 'other', 'languages', 'callable', 'from', 'C)', 'Python', 'is', 'also', 'suitable', 'as', 'an', 'extension', 'language', 'for', 'customizable', 'applications', 'This', 'tutorial', 'introduces', 'the', 'reader', 'informally', 'to', 'the', 'basic', 'concepts', 'and', 'features', 'of', 'the', 'Python', 'language', 'and', 'system', 'It', 'helps', 'to', 'have', 'a', 'Python', 'interpreter', 'handy', 'for', 'hands-on', 'experience', 'but', 'all', 'examples', 'are', 'self-contained', 'so', 'the', 'tutorial', 'can', 'be', 'read', 'off-line', 'as', 'well', 'For', 'a', 'description', 'of', 'standard', 'objects', 'and', 'modules', 'see', 'The', 'Python', 'Standard', 'Library', 'The', 'Python', 'Language', 'Reference', 'gives', 'a', 'more', 'formal', 'definition', 'of', 'the', 'language', 'To', 'write', 'extensions', 'in', 'C', 'or', 'C++', 'read', 'Extending', 'and', 'Embedding', 'the', 'Python', 'Interpreter', 'and', 'Python/C', 'API', 'Reference', 'Manual', 'There', 'are', 'also', 'several', 'books', 'covering', 'Python', 'in', 'depth', 'This', 'tutorial', 'does', 'not', 'attempt', 'to', 'be', 'comprehensive', 'and', 'cover', 'every', 'single', 'feature', 'or', 'even', 'every', 'commonly', 'used', 'feature', 'Instead', 'it', 'introduces', 'many', 'of', 'Python’s', 'most', 'noteworthy', 'features', 'and', 'will', 'give', 'you', 'a', 'good', 'idea', 'of', 'the', 'language’s', 'flavor', 'and', 'style', 'After', 'reading', 'it', 'you', 'will', 'be', 'able', 'to', 'read', 'and', 'write', 'Python', 'modules', 'and', 'programs', 'and', 'you', 'will', 'be', 'ready', 'to', 'learn', 'more', 'about', 'the', 'various', 'Python', 'library', 'modules', 'described', 'in', 'The', 'Python', 'Standard', 'Library']

# print(words.count("is"))

# for word in words:

#     print(word, "...", words.count(word))

# MATRICI

matrix = [
    ["Ionel", [4, 3, 2, 6]],
    ["Alex", [9, 8, 7, 1]],
    ["Dan", [10, 4, 9, 9]],
    ["Claudiu", [9, 5, 2, 8]]
]


for i in matrix:
    print(i[0], "media", sum(i[1]) / len(i[1]))

media_aritmetica = sum(i[1]) / len(i[1])

for i in matrix:
    if media_aritmetica <= 5.0:
        print("Corigent este: ", i[0])
        # print("Topul elevilor este: ", i[1].sort)  de verificat aici topul elevilor in functie de medie? 
    else:
        print("Nu este nici un corigent!")




