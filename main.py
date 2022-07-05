FILENAME = 'webpage'
FILETYPE = 'html'

with open(f'./input/{FILENAME}.{FILETYPE}', 'r') as file:
    data = file.read()


with open(f'./output/{FILENAME}.txt', 'w') as output:
    for line in data:
        line = line.lstrip()
        for word in line:
            output.write(word)
