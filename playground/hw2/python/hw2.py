class Place:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def distance(self, other_place):
        # TODO
        return self.latitude - other_place.latitude

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'


class City(Place):
    def __init__(self, name, zipcode, latitude, longitude):
        self.name = name
        self.zipcode = zipcode
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'{self.name} ({self.zipcode}) {self.latitude}, {self.longitude}'


class State:
    def __init__(self, name, cities):
        self.name = name
        self.cities = cities

    def __str__(self):
        str = self.name

        for city in self.cities:
            str = f'{str} \n {city.name} ({city.zipcode}) {city.latitude}, {city.longitude}'

        return str


franklin = Place(10, 20)
shorewood = Place(20, 10)

print(franklin)
print(shorewood)

print(franklin.distance(shorewood))

milwaukee = City("Milwaukee", 12345, 10, 20)
chicago = City("Chicago", 54321, 20, 10)

print(milwaukee)
print(chicago)

wisconsin = State("Wisconsin", [milwaukee, chicago])
print(wisconsin)
