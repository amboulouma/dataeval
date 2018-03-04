import json
import importlib

algorithmes_test = __import__('algorithmes_test')

input_file = open('../donnees/culture/bibliotheques.geojson')
errors_file = open('../errors/errors.json', 'w')

data = json.load(input_file)

errors_counter = 0

for _feature in data['features']:
    
    if not(algorithmes_test.test_code_postal(_feature['properties']['cod_postal'])):
        errors_file.write(_feature['properties']['cod_postal'])
        errors_file.write('Warning in "cod_postal" in property with gid: ' + _feature['properties']['gid'] + '\n\n')
        errors_counter += 1

    if not(algorithmes_test.test_mail(str(_feature['properties']['courriel']))):
        errors_file.write('Warning in "courriel" in property with gid: ' + str(_feature['properties']['gid']) + '\n')
        errors_file.write('Warning "courriel": ' + str(_feature['properties']['courriel'])+'\n\n')
        errors_counter += 1

errors_file.write('Total warnings found: ' + str(errors_counter) + '\n')
input_file.close()
errors_file.close()