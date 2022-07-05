FILENAME = 'sample'
FILETYPE = 'txt'

with open(f'{FILENAME}.{FILETYPE}', 'r') as file:
    data = file.read()


with open(f'./output/{FILENAME}.txt', 'w') as output:
    for line in data:
        for word in line:
            if word == '\n':
                word = ' '
            output.write(word)
