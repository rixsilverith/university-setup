#!/usr/bin/python3
import os
import subprocess
from termcolor import colored
from pathlib import Path
from config import Config
from current_semester import get_current_semester
from util import load_yaml, dump_yaml, num_to_text, copydir, printa, parse_group_code
from topics import Topics

class Courses(list):
    def __init__(self):
        self._courses = []
        list.__init__(self, self.read_all_files())

    def read_files(self):
        current_semester_dir = Path(Config().get('current_semester_dir')).expanduser()
        course_directories = [x for x in current_semester_dir.iterdir() if x.is_dir()]
        self._courses = [Course(path) for path in course_directories]
        return sorted(self._courses, key=lambda c: c.short)

    def read_all_files(self):
        root_dir = Path(Config().get('root_dir')).expanduser()
        for course_info_file in root_dir.glob('**/*.yaml'):
            course_dir = str(course_info_file).replace('/info.yaml', '')
            self._courses.append(Course(Path(course_dir).expanduser()))
        return sorted(self._courses, key=lambda c: c.short)

    def get(self, course_short):
        for course in self:
            if course.short == course_short.upper():
                return course

    @staticmethod
    def init_course(course_title, course_short, group, lang):
        current_semester_dir = Path(Config().get('current_semester_dir')).expanduser()
        course_dir = Path(os.path.join(current_semester_dir, course_short)).expanduser()
        if not os.path.isdir(course_dir):
            os.mkdir(course_dir)

        Course.init_info(course_dir, course_title, course_short, group, lang)
        Course.init_topics_master(course_dir, course_title, course_short, group, lang)
        Course.init_figures(course_dir)

class Course():
    def __init__(self, path):
        self.path = path
        self.short = path.stem
        self.info = load_yaml(path / 'info.yaml')
        self._topics = None

    @property
    def topics(self):
        if not self._topics:
            self._topics = Topics(self)
        return self._topics

    @staticmethod
    def init_info(course_dir, course_title, course_short, group, lang):
        printa('Creating \'info.yaml\'...')
        course_info_file = Path(os.path.join(course_dir, 'info.yaml')).expanduser()
        info = parse_group_code(str(group))

        course_info = {}
        course_info['title'] = str(course_title)
        course_info['short'] = str(course_short)
        course_info['year'] = info['year']
        course_info['semester'] = info['semester']
        course_info['group'] = int(group)
        course_info['lang'] = str(info['lang'])
        dump_yaml(course_info_file, course_info)

    @staticmethod
    def init_topics_master(course_dir, course_title, course_short, group, lang):
        printa('Creating \'master.tex\' from template...')
        course_master_dir = Path(os.path.join(course_dir, 'master.tex')).expanduser()
        subprocess.run(['touch', course_master_dir])
        current_semester = get_current_semester()['semester']
        current_year = get_current_semester()['year']
        current_semester_text = '{} semester'.format(num_to_text[current_semester])
        current_year_text = '{} year'.format(num_to_text[current_year])

        template = [r'\documentclass[a4paper, twoside, 11pt]{article}',
                    r'\input{../preamble.tex}',
                    r'\graphicspath{{./figures/}}',
                    r'',
                    r'\begin{document}',
                    fr'\makenotestitle{{{course_title} ({course_short} {group}) notes}}{{{current_year_text}}}{{{current_semester_text}}}',
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

        with open(course_master_dir, 'w') as file:
            file.write('\n'.join(template))

    @staticmethod
    def init_figures(course_dir):
        printa('Copying default \'figures\' folder...')
        course_figures_dir = Path(os.path.join(course_dir, 'figures')).expanduser()
        course_figures_template_dir = Path('../figures').expanduser()
        copydir(course_figures_template_dir, course_figures_dir)
        #subprocess.run(['cp', '-r', course_figures_template_dir, course_figures_dir])

        #os.mkdir(course_figures_dir)
