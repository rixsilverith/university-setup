#!/usr/bin/python3
from sys import argv
from tabulate import tabulate
from termcolor import colored
from courses import Courses
from current_semester import get_current_semester

table_headers = ['Title', 'Short', 'Year', 'Semester', 'Group', 'Language']
table = []

def list_courses():
    for course in Courses():
        ci = course.info
        table_row = [ci['title'], ci['short'], ci['year'], ci['semester'], ci['group'], ci['lang']]
        table.append(table_row)

    current = get_current_semester()
    c_semester = current['semester']
    c_year = current['year']
    print(colored(f'==> Listing all courses from semester {c_semester} of year {c_year}.', 'green'))
    print(tabulate(table, table_headers, tablefmt='fancy_grid'))

def list_all_courses():
    print('Listing all courses...')
    Courses().read_all_files()

if __name__ == '__main__':
    if len(argv) > 1 and (argv[1] == '--all' or argv[1] == '-a'):
        list_all_courses()
    else:
        list_courses()
