class India():
    def capital(self):
        print("New delhi is the capital of India")

    def language(self):
        print("Hindi is the most widrly spoken languqge in India")

    def type(self):
        print("India is a developing country")

class Usa():
    def capital(self):
        print("Washington, Dc. is the capital of Usa")

    def language(self):
        print("Englishis the primary  languqge in Usa")

    def type(self):
        print("usa is a developed country")


obj_ind=India()
obj_usa=Usa()

for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()