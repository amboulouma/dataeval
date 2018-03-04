import json
import importlib

algorithmes_test = __import__('algorithmes_test')

input_file = open('../donnees/culture/bibliotheques.geojson')
errors_file = open('../errors/errors.json', 'w')

data = json.load(input_file)

index = 0
errors_file.write('{')
for _feature in data['features']:
    
    if not(algorithmes_test.test_code_postal(_feature['properties']['cod_postal'])):
        index += 1
        errors_file.write('"' + str(index) + '":"')
        errors_file.write('Warning in "cod_postal" in property with gid: ' + _feature['properties']['gid'] + '\n\n')
        errors_file.write('Warning "cod_postal": ' + _feature['properties']['cod_postal'] + '\n\n')
        errors_file.write('},')

    if not(algorithmes_test.test_mail(str(_feature['properties']['courriel']))):
        index += 1
        errors_file.write('"' + str(index) + '":"')
        errors_file.write('Il y a des chances pour que la donnée suivante soit erronée:\n')
        errors_file.write('\'courriel\':\'' + str(_feature['properties']['courriel']) + '\'\nQu\'en pensez-vous ?\n\n')
        errors_file.write('Voici des informations de contexte qui peuvent vous aider:\n')
        errors_file.write(str(_feature['properties']))
        errors_file.write("\",\n")

errors_file.write('},\n')
    
input_file.close()
errors_file.close()