travel_log = [
    {"country": "Russia", "Visits": ["Moscow", "Saint Petersburg"], "total": 12},
    {"country": "France", "Visits": ["paris", "Lille", "Dijan"], "total": 14},
]


def add_new_country(name, visit, count):

    new_dict = {}

    new_dict["country"] = name
    new_dict["Visits"] = visit
    new_dict["total"] = count

    travel_log.append(new_dict)


add_new_country("Germany", ["Berlin", "Hamburg", "Stuttgart"], "2")

print(travel_log)
