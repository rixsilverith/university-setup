#!/usr/bin/python3
from pathlib import Path
from config import Config
import os
import locale
import re
import subprocess

locale.setlocale(locale.LC_TIME, "es_ES.utf8")

def num2filename(num):
    return 'topic_{0:02d}.tex'.format(num)

def filename2num(filename):
    return int(str(filename).replace('.tex', '').replace('topic_', ''))

class Topics(list):
    def __init__(self, course):
        self.course = course
        self.root = course.path
        self.master_file = self.root / 'master.tex'
        list.__init__(self, self.read_files())

    def read_files(self):
        files = self.root.glob('topic_*.tex')
        return sorted((Topic(file, self.course) for file in files), key=lambda l: l.number)

    @staticmethod
    def get_header_footer(filepath):
        part = 0
        header = ''
        footer = ''

        with open(filepath) as file:
            for line in file:
                if 'topics end here' in line:
                    part = 2

                if part == 0:
                    header += line
                if part == 2:
                    footer += line

                if 'topics start here' in line:
                    part = 1
        return (header, footer)

    def update_topics_in_master(self, r):
        header, footer = self.get_header_footer(self.master_file)
        body = ''.join(' ' * 4 + r'\input{' + num2filename(number) + '}\n' for number in r)
        self.master_file.write_text(header + body + footer)

    def new_topic(self):
        if len(self) != 0:
            new_topic_number = self[-1].number + 1
        else:
            new_topic_number = 1

        new_topic_path = self.root / num2filename(new_topic_number)
        new_topic_path.touch()
        new_topic_path.write_text('\\topic{New topic}{New topic}\n')

        if new_topic_number == 1:
            self.update_topics_in_master([1])
        else:
            self.update_topics_in_master([new_topic_number - 1, new_topic_number])

        self.read_files()
        return Topic(new_topic_path, self.course)

    def compile_master(self):
        result = subprocess.run(
            ['latexmk', '-f', '-interaction=nonstopmode', str(self.master_file)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            cwd=str(self.root)
        )

class Topic():
    def __init__(self, file_path, course):
        with open(file_path) as file:
            for line in file:
                topic_match = re.search(r'topic\{(.*)\}\{(.*)\}', line)
                if topic_match:
                    break;

        title = topic_match.group(2)

        self.file_path = file_path
        self.number = filename2num(file_path.stem)
        self.title = title
        self.course = course

    def edit(self):
        subprocess.Popen([
            'konsole', '--separate', '--hold', '-e',
            f'vim {str(self.file_path)}'
        ])

        #subprocess.run(['vim', '--servername uam', '--remote-silent', str(self.file_path)])
