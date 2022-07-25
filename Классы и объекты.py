class House():
    """описание дома"""
    def __init__(self, street, number):
        """свойства дома"""
        self.street = street
        self.number = number
        self.age = 1

    def build(self):
        """строит дом"""
        print("Дом на улице " + self.street + " под номером " + str(self.number) + " построен")

    def age_of_house(self, year):
        """возраст дома"""
        self.age += year
House1 = House("Московская", 20)
House2 = House("Московская", 21)

print(House2.number)
House1.build()
print(House1.age)

House1.age_of_house(5)
print(House1.age)


class ZagorodnieDoma(House):
    """Загородные дома"""
    def __init__(self, district, number):
        super().__init__(self,number)
        self.disrict = district

HouseG = ZagorodnieDoma("Улица Пушкина", "Дом Колотушкина")
print(HouseG.disrict)
