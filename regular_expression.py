import re

fhandle = open('regex_sum_191.txt','r')
list_numbers_string = list()
for line in fhandle:
    if re.search('[0-9]+', line):
        dummy = re.findall('[0-9]+',line)
        if len(dummy) > 1:
            [list_numbers_string.append(i) for i in dummy]
            continue
        list_numbers_string.append(dummy[0])

list_numbers_float = list()
list_numbers_float = [int(i) for i in list_numbers_string]
print(sum(list_numbers_float))
