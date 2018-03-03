import json
input_file = input()
file = open(input_file,'r')
num_line = 0
for line in file:
    num_line += 1
    print('Error in line ' + str(num_line) + ': ' + line + '\n')
file.close()