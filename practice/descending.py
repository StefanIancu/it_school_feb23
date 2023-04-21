#functie care ia un numar si il returneaza cu cifrele aranjate descrescator 
# pt a l returna crescator, sterge parametrul reverse din linia 8



def descending_order(num):
    num_list = [int(i) for i in str(num)]          #transform numarul intr-o lista de cifre int
    sorted_list = sorted(num_list, reverse=True)         #sortez lista de cifre descrescator
    # sorted_list2 = [int(x) for x in sorted_list]            
    string_list = [str(i) for i in sorted_list]         #transform lista de cifre int in str
    final = int("".join(string_list))                       #transform lista de str intr-un numar
    print(type(final))
    return final

print(descending_order(647123))

