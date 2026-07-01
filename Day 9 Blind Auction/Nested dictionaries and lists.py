
dict_countries = {
    "France" : ["Nantes", "Bordeaux", "Toulouse"]
}

print(dict_countries["France"][1])


regions = ["marina alta",["Denia", "Jávea", "Calpe"]]

print(regions[0], regions[1][1])

travel_log = {
    "France" : {
        "places" : ["Nantes", "Bordeaux", "Toulouse"],
        "times visited": 3
},
    "Germany" : {
        "Places" : ["Hamburg", "Stuttgart", "Frankfurt"],
        "times visited": 5
    }
}

print(travel_log["Germany"]["Places"][1])