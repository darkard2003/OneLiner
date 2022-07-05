FILENAME = 'webpage'
FILETYPE = 'html'
REPLACE_DOUBLEQUOTE = True


with open(f'./input/{FILENAME}.{FILETYPE}', 'r') as file:
    data = file.read().split('\n')

def onLine():
    with open(f'./output/{FILENAME}.txt', 'w') as output:
        for line in data:
            line = line.lstrip()
            for word in line:
                if REPLACE_DOUBLEQUOTE:
                    if word == '"':
                        print(word)
                        word = f'\{word}'
                        print(word)
                output.write(word)
        

if __name__ == '__main__':
    onLine()
    
