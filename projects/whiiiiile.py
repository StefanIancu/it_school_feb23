def get_user_choice(prompt : str) -> bool: 
    while True:
        choice = input(prompt)
        if choice.lower() not in ("y", "n"):
            print("Not a valid answer. Please choose 'y' or 'n'!")
        else:
            return choice.lower() == "y"
        

# get_user_choice("Digits? [y/n]")
# get_user_choice("Symbols? [y/n]")




parola = "VVzz12345"

result = "".join(dict.fromkeys(parola))

print(result)