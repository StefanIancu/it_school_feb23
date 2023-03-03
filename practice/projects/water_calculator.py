print("START")
print("Soft app that calculates your daily water cost")

print("-" * 30)

print("Hi. How would you like me to call you?:)")
nume = input("Answer: ")

print("Nice to meet you, " + nume + "!")

print("-" * 30)

print("How much water do you drink daily?")
litri_apa = int(input("Answer: "))


print("-" * 30)


if litri_apa >= 2.0:
    print("Congrats " + nume + " you are drinking enough water. Now check this out!")
    saptamanal = litri_apa * 7
    lunar = litri_apa * 30
    print("You are drinking about " + str(saptamanal) + " litres on a week and\
          about" + str(lunar) + " litres on a month")
if litri_apa < 2.0:
    print("Hmm, maybe you should consider drinking more water, " + nume + ".")
    saptamanal = litri_apa * 7
    lunar = litri_apa * 30
    print("You are drinking about " + str(saptamanal) + " litres on a week and\
          about" + str(lunar) + " litres on a month")
    
print("-" * 30)    

print("Now that we know how much water do you drink, let's see how much is one\
    liter.")

print("Choose the answer that suits you best!")

intrebari = [
    "Where do you get your daily water source? A - public water supply / B - market",
    "Have you ever considered to change your water source? A - I didn't / B - I did",
    "If your answer was yes, did anyone influenced you in that direction? A - Yes / B- No",
    "Do you ever think about the environment or pollution? A - Yes / B- No"
]

raspunsuri_pozitive = [
    "A", "a"
]

raspunsuri_negative = [
    "B", "b"
]

lista_puncte_pozitive = []
lista_puncte_negative = []

for intrebare in intrebari:
    print("*" * 15)
    print(intrebare)

    raspuns = input("Answer: ")
    

    if raspuns == raspunsuri_pozitive[0] or raspunsuri_pozitive[1]:
        lista_puncte_pozitive.append("*")
        print("Thank you.")
    else:
        print("Great.")



# baza_date = {
#     "Name": "x",
#     "Age": 1,
#     "Occupation": "y" 
# }

if len(lista_puncte_pozitive) > 2:
    print("Your score is great so far " + nume + "!")

cost_litru_market = 0.89
cost_litru_eu = cost_litru_market / 4.92
cost_litru_us = cost_litru_market / 4.64
cost_litru_uk = cost_litru_market / 5.56

print("In 2023 in Romania, let's take the price of 0.89 lei per litre.")

print("Where are you staying right now, " + nume + "?" + " A - Europe / B - US / C - UK")

country = input("Answer: ")

if country == "A" or country == "a":
    print("Great, so in Europe that's about " + str(round(cost_litru_eu)) + " euro.")
elif country == "B" or country ==  "b":
    print("Great, in the United States that's about " + str(cost_litru_us) + " dollars.")
elif country == "C" or country == "c":
    print("Great, in the United Kingdom that's about " + str(cost_litru_uk) + " pounds.")   
else:
    print("Sorry, that's not an answer. Try again typing the items above. ")

print("-" * 30)

print("As a quick recap, you told me that you drink " + str(litri_apa) + " litres on a day.")
print("Your eco-score was " + str(len(lista_puncte_pozitive)) + ".")

if len(lista_puncte_pozitive) >= 2:
    print("which makes it a great score!") 

print("You told me you are from " + country + ".")

print("-" * 30)

print("Is this correct? Y or N")

raspuns_recapitulare = input("Answer: ")


if raspuns_recapitulare == "Y" or raspuns_recapitulare == "y":
    print("That's great, " + nume)
elif raspuns_recapitulare == "N" or raspuns_recapitulare == "n":
    print("Hmm, that means I missed something. That's unusual.")
    print("Would you mind starting again, " + nume + "? Y / N")
    raspuns_restart = input("Answer: ")

    if raspuns_restart == "N" or raspuns_restart == "n":
        print("Got it, moving on then.")
    elif raspuns_restart == "Y" or raspuns_restart == "y":
        print("Please restart the program.") 

cost_mc = 4.5

print("Did you know that the cost of 1000 litres of potable water in Bucharest is " + str(cost_mc) + "? Y / N")

raspuns_cost_mc = input("Answer: ")

if raspuns_cost_mc == "Y" or raspuns_cost_mc == "y":
    print("Hah, that means you are paying your own bills!")
elif raspuns_cost_mc == "N" or raspuns_cost_mc == "n":
    print("Right, neither did I. Check this crazy math exercise out!")

print("With the price you your in your country for ONE litre you can buy instead 1000 litres")

hhgfhhfty
    


        



# repara conversia monedei sa fie user friendly 
# repara printul de la liniile 68-69
# repara inputul de la linia 110 sa arate tara si nu litera variantei alese. 

