#!/usr/bin/python3
from courses import Courses
from topics import num2filename
from config import Config
from pathlib import Path
from os import path, mkdir
from shutil import copyfile
from util import printa, copydir

out_dir = path.join(Config().get('root_dir'), 'out')
courses_dir = path.join(out_dir, 'src')
courses_dir_path = Path(courses_dir).expanduser()

compiled_notes_dir = path.join(out_dir, 'lecture-notes')
#source_notes_dir = path.join(out_dir, 'source-notes')

if not path.isdir(courses_dir_path):
    mkdir(courses_dir_path)

for course in Courses():
    ci = course.info
    title, short, group = ci['title'], ci['short'], ci['group']

    print('-------------------------------------------------------------')
    printa(f'Compiling {title} master.tex file...')
    topics = course.topics
    topics.compile_master()

    printa(f'Copying \'{title} ({short} {group}).pdf\' to {compiled_notes_dir}/...')
    compiled_master_path = path.join(course.path, 'master.pdf')
    dst_compiled_master_path = path.join(compiled_notes_dir, f'{title} ({short} {group}).pdf')
    copyfile(Path(compiled_master_path).expanduser(), Path(dst_compiled_master_path).expanduser())

    # Copy the source folder of the course
    printa(f'Copying {course.path} to {courses_dir}/{title} ({short} {group})/...')
    dst = path.join(courses_dir, f'{title} ({short} {group})')
    if not path.isdir(Path(dst).expanduser()):
        mkdir(Path(dst).expanduser())

    master_file = path.join(course.path, 'master.tex')
    info_file = path.join(course.path, 'info.yaml')
    figures_folder = path.join(course.path, 'figures')
    for t in topics:
        topic_file = Path(t.file_path).expanduser()
        topic_dest_file = Path(path.join(dst), num2filename(t.number)).expanduser()
        copyfile(topic_file, topic_dest_file)

    copyfile(Path(master_file).expanduser(), Path(path.join(dst, 'master.tex')).expanduser())
    copyfile(Path(info_file).expanduser(), Path(path.join(dst, 'info.yaml')).expanduser())
    copydir(Path(figures_folder).expanduser(), Path(path.join(dst, 'figures')).expanduser())

    #source_master_path = path.join(course.path)
    #dst_source_master_path = path.join(source_notes_dir, course.info["short"], 'master.tex')
    #copyfile(Path(source_master_path).expanduser(), Path(dst_source_master_path).expanduser()):
