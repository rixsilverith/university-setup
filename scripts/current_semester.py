#!/usr/bin/python3
from sys import argv
from termcolor import colored
from config import Config

def get_current_semester():
    current_semester_dir = Config().get('current_semester_dir')
    current_semester = current_semester_dir[25]
    current_year = current_semester_dir[14]
    return { 'semester': current_semester, 'year': current_year, 'dir': current_semester_dir }

def update_current_semester(year, semester):
    current_semester_dir = '~/Uni/CompSci-{}/semester-{}'.format(year, semester)
    current_semester_dir = Config().update('current_semester_dir', current_semester_dir)
    return get_current_semester()
   
if __name__ == '__main__':
    if len(argv) > 1 and (argv[1] == '--update' or argv[1] == '-u'):
        current = update_current_semester(argv[2], argv[3])
        c_semester = current['semester']
        c_year = current['year']
        print(colored(f'==> You\'re now working on semester {c_semester} of year {c_year}.', 'green'))

    else:
        current = get_current_semester()
        semester = current['semester']
        year = current['year']
        print(colored(f'==> You\'re now working on semester {semester} of year {year}.', 'green'))
