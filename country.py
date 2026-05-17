class Country:

    #Constructor

    def __init__(self, data: dict):

        self.name = data["name"]["common"]

        self.capital = data.get(
            "capital",
            ["—"]
        )[0]

        self.population = data.get(
            "population",
            0
        )

        self.area = data.get(
            "area",
            0
        )

        self.region = data.get(
            "region",
            "—"
        )

    #Densidad
    def density(self):

        if self.area == 0:
            return 0

        return self.population / self.area


    #String del objeto
    def __str__(self):

        return (
            f"{self.name} ({self.region})\n"
            f"  Capital: {self.capital}\n"
            f"  Población: {self.population:,}\n"
            f"  Área: {self.area:,} km²\n"
            f"  Densidad: {self.density():.2f} hab/km²"
        )