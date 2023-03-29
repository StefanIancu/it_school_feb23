class Animal:
    """Representation of pets."""
    
    def __init__(self, age, type, name, catch_phrase, status=None):
        self.age = age
        self.type = type
        self.name = name
        self.catch_phrase = catch_phrase
        self.status = status

    def walk(self):
        """Makes an animal walking."""
        print(f"{self.name} is walking...")

    def sleep(self):
        """Puts an animal to sleep."""
        print(f"{self.name} is sleeping...")

    def introduce(self):
        """A greeting and an introduction from the animal."""
        print(f"My name is {self.name}. I am a {self.type}, I am {self.age} years old and I {self.catch_phrase}")

    def get_animal_status(self):
        """Provides the animal emotional status."""
        if self.status:
            print(f"{self.name} is {self.status}!")
        else: 
            print(f"{self.name} is palm face.")

    def kill(self):
        """Makes an animal kill."""
        print(f"{self.name} is killing!")

    def murder(self, hunter, prey):
        print(f"{hunter} just killed {prey}")
        del prey
        
    
print("ANIMALS")

animal1 = Animal(12, "dog", "Lucky", "woof!", "happy")
animal2 = Animal(3, "cat", "Iris", "meow!", "angry")
animal3 = Animal(8, "snake", "Mike", "sss!")
animal4 = Animal(age=int(input("Age: ")), type=input("Type: "), name=input("Name: "), catch_phrase=input("Catch phrase: "))

animal1.introduce()
animal1.walk()
animal2.introduce()
animal2.sleep()
animal3.introduce()
animal3.kill()
animal4.introduce()

animal1.get_animal_status()
animal2.get_animal_status()
animal3.get_animal_status()
animal4.get_animal_status()



