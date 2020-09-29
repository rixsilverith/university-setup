#!/usr/bin/python3
import yaml
import shutil
from pathlib import Path
from termcolor import colored

def load_yaml(path):
    with open(path, 'r') as file:
        return yaml.load(file, Loader=yaml.FullLoader)

def dump_yaml(path, content):
    with open(path, 'w') as file:
        yaml.dump(content, file, sort_keys=False)

def copydir(src, dest):
    try:
        shutil.copytree(src, dest)
    except shutil.Error as e:
        print(colored(f'Dir not copied. Error: {e}', 'red'))
    except OSError as e:
        print(colored(f'Dir not copied. Error: {e}', 'red'))

def printa(text, color = 'green', full_color = False):
    if full_color:
        print(colored(f'==> {str(text)}', color))
    else:
        print(colored('==>', color), text)

def parse_group_code(group_code):
    parsed = {}
    gc = str(group_code)
    if gc[0] == '1':
        parsed['semester'] = 1
    elif gc[0] == '2':
        parsed['semester'] = 2
    
    if gc[1] == '1':
        parsed['year'] = 1
    elif gc[1] == '2':
        parsed['year'] = 2
    elif gc[1] == '3':
        parsed['year'] = 3
    elif gc[1] == '4':
        parsed['year'] = 4

    if gc[2] == '9':
        parsed['lang'] = 'English'
    else:
        parsed['lang'] = 'Spanish'

    return parsed

num_to_text = {
    '1': 'First',
    '2': 'Second',
    '3': 'Third',
    '4': 'Fourth'
}
