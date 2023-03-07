#formatare cu %

template = "This product is: %s "

name = "Mihai"
print("Name: %s" % name)

#formatare F-Strings

user_info = {
    "first_name": "mihai",
    "last_name": "dinu",
    "address": "Bucharest",
    "country": "ro"
}

doc1 = (f"Subsemnatul {user_info['first_name'].capitalize()} " 
      f"{user_info['last_name'].capitalize()}")

print(doc1)


name = input("Name:")

print(f"Numele tau este: {name.upper}")