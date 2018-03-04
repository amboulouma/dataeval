import json
import importlib
import os

algorithmes_test = __import__('algorithmes_test')

input_file = open('../donnees/culture/bibliotheques_erreurs.geojson')

warnings_file = open('../errors/warnings.json', 'w')
errors_file = open('../errors/errors.json', 'w')

data = json.load(input_file)

index_warnings = 0
index_errors = 0

warnings_file.write('{')
errors_file.write('{')
for _feature in data['features']:
    
    if not(algorithmes_test.test_code_postal(_feature['properties']['cod_postal'])):
        if _feature['properties']['cod_postal'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('Il y a des chances pour que la donnée suivante soit erronée:')
            errors_file.write('\'cod_postal\':\'' + str(_feature['properties']['cod_postal']) + '\'Qu\'en pensez-vous ?')
            errors_file.write('Voici des informations de contexte qui peuvent vous aider:')
            errors_file.write(str(_feature['properties'])[1:-1].replace('"','\''))
            errors_file.write("\",")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('Il y a des chances pour que la donnée suivante soit erronée:')
            warnings_file.write('\'cod_postal\':\'' + str(_feature['properties']['cod_postal']) + '\'Qu\'en pensez-vous ?')
            warnings_file.write('Voici des informations de contexte qui peuvent vous aider:')
            warnings_file.write(str(_feature['properties'])[1:-1].replace('"','\''))
            warnings_file.write("\",")

    if not(algorithmes_test.test_mail(str(_feature['properties']['courriel']))):
        if _feature['properties']['courriel'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('Il y a des chances pour que la donnée suivante soit erronée:')
            errors_file.write('\'courriel\':\'' + str(_feature['properties']['courriel']) + '\'Qu\'en pensez-vous ?')
            errors_file.write('Voici des informations de contexte qui peuvent vous aider:')
            errors_file.write(str(_feature['properties'])[1:-1].replace('"','\''))
            errors_file.write("\",")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('Il y a des chances pour que la donnée suivante soit erronée:')
            warnings_file.write('\'courriel\':\'' + str(_feature['properties']['courriel']) + '\'Qu\'en pensez-vous ?')
            warnings_file.write('Voici des informations de contexte qui peuvent vous aider:')
            warnings_file.write(str(_feature['properties'])[1:-1].replace('"','\''))
            warnings_file.write("\",")
    
    if not(algorithmes_test.test_url(str(_feature['properties']['site_inter']))):
        if _feature['properties']['site_inter'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('Il y a des chances pour que la donnée suivante soit erronée:')
            errors_file.write('\'site_inter\':\'' + str(_feature['properties']['site_inter']) + '\'Qu\'en pensez-vous ?')
            errors_file.write('Voici des informations de contexte qui peuvent vous aider:')
            errors_file.write(str(_feature['properties'])[1:-1].replace('"','\''))
            errors_file.write("\",")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('Il y a des chances pour que la donnée suivante soit erronée:')
            warnings_file.write('\'site_inter\':\'' + str(_feature['properties']['site_inter']) + '\'Qu\'en pensez-vous ?')
            warnings_file.write('Voici des informations de contexte qui peuvent vous aider:')
            warnings_file.write(str(_feature['properties'])[1:-1].replace('"','\''))
            warnings_file.write("\",")
    
    if not(algorithmes_test.test_telephone(str(_feature['properties']['telephone']))):
        if _feature['properties']['telephone'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('Il y a des chances pour que la donnée suivante soit erronée:')
            errors_file.write('\'telephone\':\'' + str(_feature['properties']['telephone'])[:-1] + '\'Qu\'en pensez-vous ?')
            errors_file.write('Voici des informations de contexte qui peuvent vous aider:')
            errors_file.write(str(_feature['properties'])[1:-1].replace('"','\''))
            errors_file.write("\",")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('Il y a des chances pour que la donnée suivante soit erronée:')
            warnings_file.write('\'telephone\':\'' + str(_feature['properties']['telephone'])[:-1] + '\'Qu\'en pensez-vous ?')
            warnings_file.write('Voici des informations de contexte qui peuvent vous aider:')
            warnings_file.write(str(_feature['properties'])[1:-1].replace('"','\''))
            warnings_file.write("\"")

warnings_file.write('"0":""')
warnings_file.write('}')
errors_file.write('"0":""')
errors_file.write('}')
    
input_file.close()
errors_file.close()