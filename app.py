import json
import classes.camp as camp

def read_file(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
    return content


def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)

# ler o arquivo de texto
file = 'CAMP.txt'
content = read_file(file)

# cabecalhos
# headers = content[0].split('\t')

# gerando json a partir do txt
json_content = []
for line in content[1:]:
    line = line.strip('\n')
    # line_dict = {}
    # for i, header in enumerate(headers):
    #     field = None
    #     try:
    #         field = line.split('\t')[i]
    #     except:
    #         pass
    #     line_dict[header] = field
    line_dict = camp.fromText(line)
    json_content.append(line_dict)

# limpando o json e deixando somente os campos necessarios
sources = {}
for line in json_content:
    source = line.source_organism

    # se o campo nao existir cria um com valor 0
    if source not in sources:
        sources[source] = 0
    
    # somando o valor do campo
    sources[source] += int(line.length)

# transformando em uma lista em json
result = []
for key, value in sources.items():
    result.append({'field': key, 'value': value})

# escrevendo no arquivo json
write_file('CAMP.json', json.dumps(result, indent=4))