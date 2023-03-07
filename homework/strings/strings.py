# 1) Print firsts and last 10 chars from lorem variable.

lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."


print(lorem[:10])
print(lorem[-10:])

print("*" * 30)

# 2) Replace with "x" last char in each product_code_list element.  - UNFINISHED

product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf",
    "weee"
]

# for i in product_code_list:
#    i[3].replace("x")
#    print(i)

print("*" * 30)

# 3) Extract words from lorem variable and store them in a list.

words = lorem.split(" ")
words2 = []

for i in words:
    words2.append(i)

print(words2)

print("*" * 30)

# 4) Join product_code_list elements in a single string concatenated by ►

update = "►".join(product_code_list)

print(update)

print("*" * 30)

# 5) Extract the number from import_numbers variable.

import_numbers = "Today we had 280 clients."

split = import_numbers.split(" ")

nr_extras = int(split[3])

print(nr_extras)

print("*" * 30)

# 6) Print product_code_list elements with all letters capitalized and then just with first letter capitalized

product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf",
    "weee"
]

for i in product_code_list:
    print(i.upper())
    
for i in product_code_list:
    print(i.capitalize())


# 7) Find if lorem variable contains "," in fist 20 chars.

lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# for i in lorem[:20]:
#    lorem[:20].find("is")
   
print(lorem[:20].find(","))

print("*" * 30)

# 8) Using commit variable, print short-version commit number (11 chars) alongside username
#     EX: tester b84fc4703e7

commit = """commit 30c06bce50eeb7a8856e18df2dc64e76fec14cc9
Author: Dinu Mihai <mihai.dinu93@gmail.com>
Date:   Thu Jun 9 18:18:02 2022 +0300
    shuffle method"""

split1 = commit.split("\n")

split2 = split1[0].split(" ")

commit_id = split2[1][:11]

author = split1[1]

a1 = author.find(": ")
a2 = author.find("<")

user = split1[1][a1:a2].strip(": ")

print(user, commit_id)


print("*" * 30)

# 9) Replace the first 2 "e" in import_numbers - replaced them with "X".

import_numbers = "Today we had 280 clients."

print(import_numbers.replace("e", ("X")))

print("*" * 30)

#10) Group product codes from product_code_list in a dictionary by last char

product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf",
    "weee"
]

# product_code_dict = {

# }
    
# for item in product_code_list:


#12) print a justified word count for py_text variable - UNSURE

py_text = """Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
To find out more, start with The Python Tutorial. The Beginner's Guide to Python links to other introductory tutorials and resources for learning Python."""

cuvinte = py_text.split(" ")

print(len(cuvinte))

print("*" *30)

#13) print only the first sentence of py_text variable.

linii = py_text.split(". ")[0]

print(linii)