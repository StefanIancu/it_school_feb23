import sys

# user_input = input("Introdu string: ")

# print(user_input[::-1])

if sys.version_info.major < 3:
    print(f"Versiunea {sys.version_info.major} nu este suportata!")
   

print("hello")

# sys.exit(1)
try:
    print(sys.argv[1] * int(sys.argv[2]))
except IndexError:
    print("Argumentul nu exista.")
    sys.exit(1)
except ValueError:
    print("Tip argument incorect.")
    sys.exit(1)

print("bye")


