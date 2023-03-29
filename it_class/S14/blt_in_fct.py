# all - true daca toate valorile din lista evalueaza True 
print(all([0, True]))

#any - true daca oricare element este True
print(any([True, False, False]))

#map
init_list = [4, 56, 7, 5, 45]
new_list = map(lambda x: x **2, init_list)     #retunreaza map object
new_list2 = [x ** 2 for x in init_list]      #returneaza lista 
print(new_list)

print(type(new_list))
print(type(new_list2))

#enumerate   - returneaza enumerate object 
print(enumerate(init_list))
for i in enumerate(init_list):
    print(f"Index: {i[0]} ... valoare {i[1]}")


#divmod - returneaza si catul si restul  

cat = 10 // 3
rest = 10 % 3

cat, rest = divmod(10, 3)   #unpack fiind tuplu 
print(f"Catul este egal cu {cat} si restul egal cu {rest}")

#zip -

names = ["alex", "elena", "victor"]
ids = ["2223", "3333", "4444"]

zp = zip(names, ids)

print(dict(zp))

