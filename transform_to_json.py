# This app transform table in txt to json
# The fields of table are separated by tab
# The first line is the header
# The first column is the key

# read file CAMP.txt
# write file CAMP.json


import json


def read_file(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
    return content


def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


def transform_to_json(content):
    headers = content[0].split('\t')
    json_content = []
    for line in content[1:]:
        line = line.strip('\n')
        line_dict = {}
        for i, header in enumerate(headers):
            field = None
            try:
                field = line.split('\t')[i]
            except:
                pass
            line_dict[header] = field
        json_content.append(line_dict)
    return json_content


def main():
    file_name = 'CAMP.txt'
    content = read_file(file_name)
    json_content = transform_to_json(content)
    write_file('CAMP.json', json.dumps(json_content, indent=4))


if __name__ == '__main__':
    main()