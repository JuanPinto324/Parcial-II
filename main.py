from country import Country


data = {
    "name": {
        "common": "Argentina"
    },
    "capital": ["Buenos Aires"],
    "population": 46735004,
    "area": 2780400,
    "region": "Americas"
}

pais = Country(data)

print(pais)
