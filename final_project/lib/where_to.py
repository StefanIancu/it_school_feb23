import csv
from pathlib import Path
from fpdf import FPDF
from ticket import PlaneTicket
ROOT = Path(__file__).parent
from skeleton import DESTINATIONS_AND_PRICES

#to implement back method that takes the user back to main menu

class WhereToGo:

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title
    
    def see_list_of_destinations(self):
        print("List of destinations")
        with open('destinations.csv') as fin:
            reader = csv.reader(fin.readlines())
    
        for line in reader:
            print(line[0])

    def download_brochure(self):
        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size = 15)



        pdf.cell(200, 10, txt = "BROCHURE",
         ln = 1, align= "C")
        

        pdf.cell(150, 10, txt=f"{reader}",
            ln = 2, align = "R")
        
        # for k, v in DESTINATIONS_AND_PRICES.items():
        #     pdf.cell(150, 10, txt=f"To {k.title}, price ${v}",
        #              ln=2.)


        # pdf.cell(200, 10, txt = f"Mr./Mrs. {ticket.name}",
        #  ln = 3, align= "L")
        # pdf.cell(150, 10, txt=f"Seat number: {ticket.seat}",
        #  ln = 4, align="L")

        # pdf.cell(150, 10, txt=f"Departure date: {ticket.date}",
        #  ln = 5, align="R")
        # pdf.cell(150, 10, txt=f"Destination: {ticket.destination}",
        #  ln = 6, align="R")


        pdf.cell(100, 10, txt="Thank you for choosing to fly with us!",
         ln = 10, align="C")

        pdf.output("planeticket.pdf")




w = WhereToGo("Title")

# try:
#     w.see_list_of_destinations()
# except OSError as err:
#     print(err)

ticket = PlaneTicket(1, "Stefan Iancu", 45, "15.07.2023", "Budapest")
ticket2 = PlaneTicket(1, "Daniel Gheorghe", 46, "11.07.2023", "Rome")
ticket3 = PlaneTicket(1, "Andreea Savu", 47, "19.07.2023", "Tokyo")


# w.see_list_of_destinations()