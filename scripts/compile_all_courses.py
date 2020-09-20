#!/usr/bin/python3
from courses import Courses
from config import Config
#from util import init_out_dir
from pathlib import Path
from os import path
from shutil import copyfile
from util import printa

out_dir = path.join(Config().get('root_dir'), 'out')
compiled_notes_dir = path.join(out_dir, 'compiled-notes')
source_notes_dir = path.join(out_dir, 'source-notes')

#if not path.isdir(out_dir):
    #init_out_dir()

for course in Courses():
    print('-------------------------------------------------------------')
    printa(f'Compiling {course.info["title"]} master.tex file...')
    topics = course.topics
    topics.compile_master()

    printa(f'Copying \'{course.info["title"]} ({course.info["short"]}).pdf\' to {compiled_notes_dir}...')
    compiled_master_path = path.join(course.path, 'master.pdf')
    dst_compiled_master_path = path.join(compiled_notes_dir, f'{course.info["title"]} ({course.info["short"]}).pdf')
    copyfile(Path(compiled_master_path).expanduser(), Path(dst_compiled_master_path).expanduser())
    #os.rename(path.join(compiled_notes_dir, 'master.pdf'), path.join(compiled_notes_dir, f'{course.info["title"]} ({course.info["short"]}).pdf'))

    #printa(f'Copying master.tex -> {course.info["short"]}.tex to {source_notes_dir}...')
    #source_master_path = path.join(course.path, 'master.tex')
    #dst_source_master_path = path.join(source_notes_dir, f'{course.info["short"]}.tex')
    #copyfile(source_master_path, dst_source_master_path)
