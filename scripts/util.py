#!/usr/bin/python3
import os
import yaml
import subprocess
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

def printa(text, color = 'green', full = False):
    if full:
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

"""
def load_course_info(path):
    with open(path) as file:
        return yaml.load(file, Loader=yaml.FullLoader)

def touch_course_info(course_dir, title, short, group, lang):
    course_info_dir = Path(os.path.join(course_dir, 'info.yaml')).expanduser()
    subprocess.run(['touch', course_info_dir])

    s = get_semester_from_dir(course_info_dir)
    course = {
        'title': title,
        'short': short,
        'year': s['year'],
        'semester': s['semester'],
        'group': group,
        'lang': lang
    }

    with open(course_info_dir, 'w') as file:
        yaml.dump(course_info_dir, file, sort_keys=False)

def touch_course_mastertex(course_dir, title, short, group, lang):
    course_mastertex_dir = Path(os.path.join(course_dir, 'master.tex')).expanduser()
    subprocess.run(['touch', course_mastertex_dir])
    s = get_semester_from_dir(course_dir)

    mastertex_template = [r'\documentclass[a4paper, twoside, 11pt]{article}',
                          r'\input{../preamble.tex}',
                          r'\graphicspath{{./figures/}}',
                          r'',
                          r'\begin{document}',
                          fr'   \makenotestitle{{title} ({short} {group}) notes}',
                          r'    \begin{figure}[htbp]',
                          r'        \centerline{\includegraphics[width=0.45\textwidth]{uam.png}}',
                          r'    \end{figure}',
                          r'    \vskip2cm',
                          r'    \tableofcontents',
                          r'',
                          fr'   % topics start here',
                          fr'   % topics end here',
                          r'\end{document}'
                         ]

    with open(course_mastertex_dir, 'w') as file:
        file.write('\n'.join(mastertex_template))
"""
