#!/usr/bin/python3
from rofi import rofi
from courses import Courses
import subprocess

courses = Courses()
sorted_courses = sorted(courses, key=lambda l: l.info['title'])

course_list = [
    '{course_title}      <b><span size="x-small" rise="2000"> {course_short} {group} </span></b>'.format(
        course_title = course.info['title'],
        course_short = course.info['short'],
        group = course.info['group']
    ) for course in sorted_courses
]


def rofi_courses():
    code, index, selected = rofi('Select course', course_list, [
        '-no-custom',
        '-markup-rows',
        '-lines', 8
    ])

    if index >= 0:
        return index

if __name__ == '__main__':
    index = rofi_courses()
    master_pdf = sorted_courses[index].path / 'master.pdf'
    subprocess.run(['zathura', master_pdf])
