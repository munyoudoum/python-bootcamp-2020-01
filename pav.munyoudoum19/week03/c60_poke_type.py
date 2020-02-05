import requests
import json


def poke_type(types):
    res = []
    r = requests.get('https://raw.githubusercontent.com/Biuni\
        /PokemonGO-Pokedex/master/pokedex.json').json()
    for poke in r["pokemon"]:
        if poke["type"] == types or poke["type"][0] == types:
            res.append((poke["id"], poke["name"]))
        if len(poke["type"]) == 2 and len(types) != 2:
            if poke["type"][1] == types[0]:
                res.append((poke["id"], poke["name"]))
    return res
