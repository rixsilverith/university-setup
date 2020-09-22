#!/usr/bin/python3
from courses import Courses
from rofi import rofi
from rofi_courses import rofi_courses, sorted_courses

sorted_course_index = rofi_courses()
topics = sorted_courses[sorted_course_index].topics
sorted_topics = sorted(topics, key=lambda l: -l.number)

options = [
    '{number: >2}. {title}      <b><span size="x-small" rise="2000"> {course_short} {group} </span></b>'.format(
        number = topic.number,
        title = topic.title,
        course_short = topic.course.info['short'],
        group = topic.course.info['group']
    ) for topic in sorted_topics
]

key, index, selected = rofi('Select topic', options, [
    '-lines', 6,
    '-markup-rows',
    '-kb-row-down', 'Down',
    '-kb-custom-1', 'Ctrl+n'
])

if key == 0:
    sorted_topics[index].edit()
elif key == 1:
    new_topic = topics.new_topic()
    new_topic.edit()

