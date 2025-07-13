from pokemondata import Gen3Save
from pokemondata import Gen3Pokemon
import json

mysave = Gen3Save("POKEMON.sav")

ret = []

for pokemon in mysave.boxes:

	item = {}
	item['name'] = pokemon.name
	item['trainer'] = pokemon.trainer
	item['level'] = pokemon.level
	item['species'] = pokemon.species
	item['nature'] = pokemon.nature
	item['moves'] = pokemon.moves
	item['exp'] = pokemon.exp
	item['ivs'] = pokemon.ivs

	ret.append(item)

print((json.dumps(ret)))

