# 3. Scrieti o functie care returneaza daca unu nr. (reprezentan un an) este
# considerat an bisect.

def leap_year(year):
    """Calculate if a year is leap or not."""
    if year % 4 == 0 and year % 100 != 0:
        return "This is a leap year!"
    else:
        return "This is not a leap year!"
      
year_in = int(input("Choose a year: "))
print(leap_year(year_in))