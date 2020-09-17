#!/usr/bin/python3
from courses import Courses
from util import printa

print('==============================')
course_title = input('--> Title: ')
course_short = input('--> Short: ')
group = input('--> Group: ')
lang = input('--> Language: ')
print('==============================')

Courses.init_course(course_title, course_short, group, lang)
printa(f'Successfully created {course_title}!', 'green', True)
