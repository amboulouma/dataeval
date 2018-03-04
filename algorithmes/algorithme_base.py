import json
import importlib

algorithmes_test = __import__('algorithmes_test')

input_file = open('../donnees/culture/bibliotheques.geojson')
# input_file = open('../donnees/culture/college_prives.geojson')


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
            errors_file.write('Il y a des chances pour que la donnée suivante soit erronée:\n')
            errors_file.write('\'cod_postal\':\'' + str(_feature['properties']['cod_postal']) + '\'\nQu\'en pensez-vous ?\n\n')
            errors_file.write('Voici des informations de contexte qui peuvent vous aider:\n')
            errors_file.write(str(_feature['properties']))
            errors_file.write("\",\n")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('Il y a des chances pour que la donnée suivante soit erronée:\n')
            warnings_file.write('\'cod_postal\':\'' + str(_feature['properties']['cod_postal']) + '\'\nQu\'en pensez-vous ?\n\n')
            warnings_file.write('Voici des informations de contexte qui peuvent vous aider:\n')
            warnings_file.write(str(_feature['properties']))
            warnings_file.write("\",\n")

    if not(algorithmes_test.test_mail(str(_feature['properties']['courriel']))):
        if _feature['properties']['courriel'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('Il y a des chances pour que la donnée suivante soit erronée:\n')
            errors_file.write('\'courriel\':\'' + str(_feature['properties']['courriel']) + '\'\nQu\'en pensez-vous ?\n\n')
            errors_file.write('Voici des informations de contexte qui peuvent vous aider:\n')
            errors_file.write(str(_feature['properties']))
            errors_file.write("\",\n")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('Il y a des chances pour que la donnée suivante soit erronée:\n')
            warnings_file.write('\'courriel\':\'' + str(_feature['properties']['courriel']) + '\'\nQu\'en pensez-vous ?\n\n')
            warnings_file.write('Voici des informations de contexte qui peuvent vous aider:\n')
            warnings_file.write(str(_feature['properties']))
            warnings_file.write("\",\n")
    
    if not(algorithmes_test.test_url(str(_feature['properties']['site_inter']))):
        if _feature['properties']['site_inter'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('Il y a des chances pour que la donnée suivante soit erronée:\n')
            errors_file.write('\'site_inter\':\'' + str(_feature['properties']['site_inter']) + '\'\nQu\'en pensez-vous ?\n\n')
            errors_file.write('Voici des informations de contexte qui peuvent vous aider:\n')
            errors_file.write(str(_feature['properties']))
            errors_file.write("\",\n")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('Il y a des chances pour que la donnée suivante soit erronée:\n')
            warnings_file.write('\'site_inter\':\'' + str(_feature['properties']['site_inter']) + '\'\nQu\'en pensez-vous ?\n\n')
            warnings_file.write('Voici des informations de contexte qui peuvent vous aider:\n')
            warnings_file.write(str(_feature['properties']))
            warnings_file.write("\",\n")
    
    if not(algorithmes_test.test_telephone(str(_feature['properties']['telephone']))):
        if _feature['properties']['telephone'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('Il y a des chances pour que la donnée suivante soit erronée:\n')
            errors_file.write('\'telephone\':\'' + str(_feature['properties']['telephone']) + '\'\nQu\'en pensez-vous ?\n\n')
            errors_file.write('Voici des informations de contexte qui peuvent vous aider:\n')
            errors_file.write(str(_feature['properties']))
            errors_file.write("\",\n")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('Il y a des chances pour que la donnée suivante soit erronée:\n')
            warnings_file.write('\'telephone\':\'' + str(_feature['properties']['telephone']) + '\'\nQu\'en pensez-vous ?\n\n')
            warnings_file.write('Voici des informations de contexte qui peuvent vous aider:\n')
            warnings_file.write(str(_feature['properties']))
            warnings_file.write("\",\n")

warnings_file.write('}\n')
errors_file.write('}\n')
    
input_file.close()
errors_file.close()