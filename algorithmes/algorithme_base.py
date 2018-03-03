import json
import importlib

algorithmes_test = __import__('algorithmes_test')

input_file = open('../donnees/culture/bibliotheques.geojson')
errors_file = open('../errors/errors.json', 'w')

data = json.load(input_file)

for _feature in data['features']:
    if algorithmes_test.test_code_postal(_feature['properties']['cod_postal']):
        continue
    else:
        errors_file.write(_feature['properties']['cod_postal'])


input_file.close()
errors_file.close()