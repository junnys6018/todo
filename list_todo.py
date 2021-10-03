import json

# number of leading spaces to print before each line
SPACES = 2

color_map = {
    'low': '\033[92m',
    'med': '\033[93m',
    'high': '\033[91m'
}

with open('todo.json') as f:
    todo = json.load(f)

def key_func(item):
    pri = {
        'low': 0,
        'med': 1,
        'high': 2
    }
    return (pri[item['priority']], item['tag'])

# sort by priority, then by tag
todo.sort(key=key_func)

max_tag_len = max([len(item['tag']) for item in todo])

for item in todo:
    line = color_map[item['priority']] + ' ' * SPACES
    line += item['tag']
    line += ' ' * (max_tag_len - len(item['tag'])) + ' '
    line += item['title']
    line += '\033[0m'

    print(line)
    if item['message']:
        print('\033[90m' + ' ' * SPACES + '- ' + item['message'] + '\033[0m')
