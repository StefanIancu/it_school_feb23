#how to add elements and their appeareance from a string in a dict 
#from stack overflow


def count(string):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


print(count("bbasudbasd"))