omara = { "zgornji_predal": ["žeblji", "lepilo", "trak"], "spodnji_predal": [ {"orodje": "kladivo", "teza": 2}, {"orodje": "klešče", "teza": 1} ] }
print(omara["zgornji_predal"][1])
print(omara["spodnji_predal"][0]["teza"])
print(omara["spodnji_predal"][1]["orodje"])

sistem = { "strezniki": [ {"ime": "srv1", "stanje": "running"},
                          {"ime": "srv2", "stanje": "down", "napaka": {"koda": 503, "opis": "unavailable"}} ],
                            "okolje": { "cpu": [35, 42, 38], "pomnilnik": {"lokalno": 60, "oddaljeno": {"poraba": 90, "opozorilo": "HIGH"}} } }
#Izpiši opozorilo: "HIGH"
print(sistem["okolje"]["pomnilnik"]["oddaljeno"]["opozorilo"])

#Izpiši kodo napake: 503
print(sistem["strezniki"][1]["napaka"]["koda"])

#Izpiši drugo meritev CPU (42)
print(sistem["okolje"]["cpu"][1])

knjiznica = { "oddelek_a": [ {"naslov": "Python 101", "leto": 2020}, {"naslov": "Algoritmi", "leto": 2018} ],
              "oddelek_b": { "revije": ["Science", "Nature", "IEEE"],
                             "stanje": {"odprto": True, "nadstropje": 2} } }
#Izpiši niz: "Nature"
print(knjiznica["oddelek_b"]["revije"][1])

#Izpiši številko: 2018
print(knjiznica["oddelek_a"][1]["leto"])

#Izpiši številko nadstropja: 2
print(knjiznica["oddelek_b"]["stanje"]["nadstropje"])

trgovina = { "artikli": [ {"ime": "mleko", "cena": 1.2},
                          {"ime": "kruh", "cena": 1.5}, {"ime": "sir", "cena": 3.8} ], 
                          "zaloga": { "hladilnik": {"kos": 20, "status": "OK"}, 
                                     "polica": {"kos": 5, "status": "LOW"} } }

#Izpiši status: "LOW"
print(trgovina["zaloga"]["polica"]["status"])

#Izpiši ceno artikla "sir" (3.8)
print(trgovina["artikli"][2]["cena"])

#Izpiši število kosov v hladilniku (20)
print(trgovina["zaloga"]["hladilnik"]["kos"])