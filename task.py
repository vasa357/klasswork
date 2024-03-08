class City:
    def __init__(self, name, population, country):
        self.name = name
        self.population = population
        self.country = country

    def display_info(self):
        print(f"{self.name} - це місто в {self.country} з населенням {self.population}.")

my_city = City("Київ", 2800000, "Україна")
my_city.display_info()
