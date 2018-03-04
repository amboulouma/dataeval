import json
import importlib
import random

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
            errors_file.write('\'cod_postal\':\'' + str(_feature['properties']['cod_postal']))
            errors_file.write('<br>Voici des informations de contexte qui peuvent vous aider:<br>')
            properties = str(_feature['properties'])[1:-1].replace('"','\'')
            errors_file.write(properties.replace(',', ',<br>').split(',')[1])
            errors_file.write(properties.replace(',', ',<br>').split(',')[2])
            errors_file.write(properties.replace(',', ',<br>').split(',')[4])
            errors_file.write(properties.replace(',', ',<br>').split(',')[5])
            errors_file.write("\",")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('\'cod_postal\':\'' + str(_feature['properties']['cod_postal']))
            warnings_file.write('<br>Voici des informations de contexte qui peuvent vous aider:<br>')
            warnings_file.write(properties.replace(',', ',<br>').split(',')[1])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[2])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[4])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[5])
            warnings_file.write("\",")

    if not(algorithmes_test.test_mail(str(_feature['properties']['courriel']))):
        if _feature['properties']['courriel'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('\'courriel\':\'' + str(_feature['properties']['courriel']))
            errors_file.write('<br>Voici des informations de contexte qui peuvent vous aider:<br>')
            properties = str(_feature['properties'])[1:-1].replace('"','\'')
            errors_file.write(properties.replace(',', ',<br>').split(',')[1])
            errors_file.write(properties.replace(',', ',<br>').split(',')[2])
            errors_file.write(properties.replace(',', ',<br>').split(',')[3])
            errors_file.write(properties.replace(',', ',<br>').split(',')[4])
            errors_file.write(properties.replace(',', ',<br>').split(',')[5])
            errors_file.write("\",")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('\'courriel\':\'' + str(_feature['properties']['courriel']))
            warnings_file.write('<br>Voici des informations de contexte qui peuvent vous aider:<br>')
            warnings_file.write(properties.replace(',', ',<br>').split(',')[1])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[2])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[3])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[4])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[5])
            warnings_file.write("\",")
    
    if not(algorithmes_test.test_url(str(_feature['properties']['site_inter']))):
        if _feature['properties']['site_inter'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('\'site_inter\':\'' + str(_feature['properties']['site_inter']))
            errors_file.write('<br>Voici des informations de contexte qui peuvent vous aider:<br>')
            properties = str(_feature['properties'])[1:-1].replace('"','\'')
            errors_file.write(properties.replace(',', ',<br>').split(',')[1])
            errors_file.write(properties.replace(',', ',<br>').split(',')[2])
            errors_file.write(properties.replace(',', ',<br>').split(',')[3])
            errors_file.write(properties.replace(',', ',<br>').split(',')[4])
            errors_file.write(properties.replace(',', ',<br>').split(',')[5])
            errors_file.write("\",")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('\'site_inter\':\'' + str(_feature['properties']['site_inter']))
            warnings_file.write('<br>Voici des informations de contexte qui peuvent vous aider:<br>')
            warnings_file.write(properties.replace(',', ',<br>').split(',')[1])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[2])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[3])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[4])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[5])
            warnings_file.write("\",")
    
    if not(algorithmes_test.test_telephone(str(_feature['properties']['telephone']))):
        if _feature['properties']['telephone'] != None:
            index_errors += 1
            errors_file.write('"' + str(index_errors) + '":"')
            errors_file.write('\'telephone\':\'' + str(_feature['properties']['telephone']).replace('\n',' '))
            errors_file.write('<br>Voici des informations de contexte qui peuvent vous aider:<br>')
            properties = str(_feature['properties'])[1:-1].replace('"','\'')
            errors_file.write(properties.replace(',', ',<br>').split(',')[1])
            errors_file.write(properties.replace(',', ',<br>').split(',')[2])
            errors_file.write(properties.replace(',', ',<br>').split(',')[3])
            errors_file.write(properties.replace(',', ',<br>').split(',')[4])
            errors_file.write("\",")
        else:
            index_warnings += 1
            warnings_file.write('"' + str(index_warnings) + '":"')
            warnings_file.write('\'telephone\':\'' + str(_feature['properties']['telephone']).replace('\n',' '))
            warnings_file.write('<br>Voici des informations de contexte qui peuvent vous aider:<br>')
            warnings_file.write(properties.replace(',', ',<br>').split(',')[1])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[2])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[3])
            warnings_file.write(properties.replace(',', ',<br>').split(',')[4])
            warnings_file.write("\"")

warnings_file.write('"0":""')
warnings_file.write('}')
errors_file.write('"0":""')
errors_file.write('}')
    
input_file.close()
errors_file.close()