from country import CountryAPI


api = CountryAPI()

# Juan
japan = api.by_name("japan")
uruguay = api.by_name("uruguay")
argentina = api.by_name("argentina")
nepal = api.by_name("nepal")

# Jose
jordan = api.by_name("jordan")
oman = api.by_code("OM")
spain = api.by_name("spain")
egypt = api.by_name("egypt")

print(oman)

japan.comparar([
    uruguay,
    argentina,
    nepal,
    jordan,
    oman,
    spain,
    egypt
])