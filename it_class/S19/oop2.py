class Employee:

    def __init__(self, first_name, last_name, email, gross_salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gross_salary = gross_salary
        self.__ssm_signed = False

    def sign_ssm(self):
        self.__ssm_signed = True

    def sign_presence(self):
        pass

    def get_net_salary(self):
        return self.__gross_salary

    def pay(self):
        print(f"Amount to transfer: {self.get_net_salary()}")


class FullTimeEmployee:
   


class Contractor:
  


class NoTaxEmployee:
   


class PartTimeEmployee(Employee):

    def pay(self):    
        print("Hours per day worked: 4")
        return super().pay()

    
    


employees = [

    FullTimeEmployee("Ionut", "Sergiu", "test@test.com", 3000),
    Contractor("Ionut", "Zmeu", "test@test.com", 6000),
    PartTimeEmployee("Dan", "Pavel", "test@test.com", 4000),
    NoTaxEmployee("Marian", "Sena", "test@test.com", 5000)
    
]


for emp in employees:
    emp.pay()



#python permite mosteniri multiple
#MRO - method resolution order - algoritmul de mosteniri 
#mostenire diamond 

