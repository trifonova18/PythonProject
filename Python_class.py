class House():
    """описание дома"""
    def __init__(self, street, number):
        """свойства дома"""
        self.street = street
        self.number = number

    def build(self):
        """строит дом"""
        print("Дом на улице " + self.street + " под номером " + str(self.number) + " построен.")
House1 = House("Московская", 20)
House2 = House("Московская", 21)

House1.build()