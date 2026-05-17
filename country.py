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
    
    # Comparar paises
    def comparar(self, otros: list):

        paises = [self] + otros

        print(
            f"{'País':15}"
            f"{'Población':15}"
            f"{'Área':15}"
            f"{'Densidad':15}"
        )

        for p in paises:

            print(
                f"{p.name:15}"
                f"{p.population:15,}"
                f"{p.area:15,.0f}"
                f"{p.density():15.2f}"
            )

        print("-" * 60)

        mayor_poblacion = max(
            paises,
            key=lambda p: p.population
        )

        mayor_area = max(
            paises,
            key=lambda p: p.area
        )

        mayor_densidad = max(
            paises,
            key=lambda p: p.density()
        )

        print(
            f"Mayor población : "
            f"{mayor_poblacion.name}"
        )

        print(
            f"Mayor área      : "
            f"{mayor_area.name}"
        )

        print(
            f"Mayor densidad  : "
            f"{mayor_densidad.name}"
        )

import requests

from requests.exceptions import (
    HTTPError,
    ConnectionError,
    Timeout
)

BASE = "https://restcountries.com/v3.1"

class CountryAPI:


    # Buscar por nombre
    def by_name(self, name):

        url = f"{BASE}/name/{name}"

        try:

            r = requests.get(
                url,
                timeout=5
            )

            r.raise_for_status()

            data = r.json()[0]

            return Country(data)

        except Timeout:
            print("La API tardó demasiado")

        except ConnectionError:
            print("Sin conexión")

        except HTTPError:
            print("País no encontrado")

        return None

    # Buscar por region
    def by_region(self, region):

        url = f"{BASE}/region/{region}"

        try:

            r = requests.get(
                url,
                timeout=5
            )

            r.raise_for_status()

            data = r.json()

            return [
                Country(pais)
                for pais in data
            ]

        except Timeout:
            print("La API tardó demasiado")

        except ConnectionError:
            print("Sin conexión")

        except HTTPError:
            print("Región no encontrada")

        return []


    def by_code(self, code):

        url = f"{BASE}/alpha/{code}"

        try:

            r = requests.get(
                url,
                timeout=5
            )

            r.raise_for_status()

            data = r.json()[0]

            return Country(data)

        except Timeout:
            print("La API tardó demasiado")

        except ConnectionError:
            print("Sin conexión")

        except HTTPError:
            print("País no encontrado")

        return None
