# University setup for Computer Science
> Hey! Welcome to my university setup repository. Here you'll find a set of scripts I use to manage my lecture notes and coursework on computer science and maths, as well as some files like `preamble.tex` ment to improve the note-taking experience in LaTeX.
>
> These scripts carry out tasks from automatically creating all the necessary files and folders for a new course to compiling all of the notes of a specific course and backing them up on the cloud.
>
> If you feel curious, a collection of all my lecture notes can be found [here](rixsilverith.io/lecture-notes).

### Work directory and course structure
Before I begin explaining what task each script does I must talk about how is the work directory and how is each course structured. The work directory is just the folder where I keep all my university related files. It's structured as follows:
```
Uni
├── CompSci-1
│   ├── semester-1
│   │   ├── preamble.tex
│   │   ├── CALC1
│   │   ├── COMPB
│   │   ├── ...
│   │   └── PROG1
│   └── semester-2
│       ├── preamble.tex
│       ├── CALC2
│       └── ...
├── CompSci-2
├── CompSci-3
└── ...
```
As you can see, each year is represented its respective folder named `CompSci-x`, where x is the year. A year is split into two semesters, represented by the `semester-1` and `semester-2` folders, which both contains the courses directories of the semester. Here, the `preamble.tex` is worth of mention. It contains the preamble included in all of my LaTeX files. 

*Note: If you're reading this, I assume you know, at least, what is LaTeX. If not, the [latex-project.org](https://www.latex-project.org/) website is a good starting point.*

As I mentioned earlier, the semester folders contain the course directories of that semester. Each of them is structured in the very same way:

```
semester-1
├── CALC1
│   ├── info.yaml
│   ├── master.tex
│   ├── topic_01.tex
│   ├── topic_02.tex
│   ├── ...
│   └── figures
│       ├── uam.png
│       ├── lagrange-theorem.png
│       └── ...
├── COMPB
└── ...
```
Here, we must point out the `info.yaml` and `master.tex` files. The first one contains information about a course; it's title, short, in which group I am and the language in which the course is taken.
```yaml
title: Calculus I
short: CALC1
group: 119
```
*Note: The semester and year is which is taken course, as well as the language, are parsed from the group number. In my university the three numbers (four, in case of practical courses) represents the semester, year and group, respectively. In this case, the group '9' refers to the english group. In practical courses, such as Computer Lab, another number is added, which represents the practice group.*

Secondly, the `master.tex` is in charge of bundling up all the topics of the course into a single file, the one that will be compiled by LaTeX compiler.  Here is the content of the `master.tex` file:

```latex
\documentclass[a4paper, twoside, 11pt]{article}
\input{../preamble.tex}
\graphicspath{{./figures}}

\begin{document}
\ntitle{Calculus I (CALC1 119) notes}{First year}{First semester}
\begin{figure}[htbp]
	\centerline{\includegraphics[width=0.45\textwidth]{uam.png}}
\end{figure}
\vskip2cm
\tableofcontents

% topics start here
\input{topic_01.tex}
\input{topic_02.tex}
...
% topics end here
\end{document}
```
A topic file contains the following information:
```latex
\topic{Axiomatic definition of \R}{Axiomatic definition of \R}
```
I know, you might be wondering why the heck there's exactly the same text in both arguments of the `\topic` command. In a few words it's a hacky solution to a problem related to multiline topic titles. The first argument is the text that's displayed at the beginning of the topic, while the second is the one displayed in both the page headers and the table of contents. In case the title is long enough you might want to insert line breaks in the first one and no line breaks in the second. Let me show a brief example.
```latex
\topic{Matrices and systems of \\ linear equations}{Matrices and systems of linear equations}
```
In this example, a line break will be inserted in the title beginning a new topic. If we didn't have the second argument, where no line breaks are being inserted, those line breaks in the first argument would also be displayed in both the page headers and the table of contents. And we don't want that, at least, I don't. So, the solution that came to my mind were to use the text in the first argument to display the title at the beginning of the topic and the second one to display that title without line breaks in the page header and the table of contents. You can examine the definition of the `\topic` command in the `preamble.tex` file. If you come across another, more elegant or not so hacky solution to this problem, feel free to do a pull request to this repo.

*Note: Each topic of a course can be thought as a 'lecture', but in reality they're not actually the same.*

### Getting started and configuration
TODO: Use Simple X HotKey Daemon to keybind scripts.

### Scripts for note-taking
### `init_course.py`

### `courses.py`
In this file the `Course` and `Courses` classes are defined. The later is just a list of `Course`s in the `Uni` folder, while the former represents a course directory. A `Course` has a `short`, a `path` and an `info` property, a Python dictionary from which you can retrieve information about the course. This info is collected from the `info.yaml` file in the course folder. You can also access the course topics by reading the `topics` property, which is a `Topics` object (a list of `Topic`s).

You can get a specific `Course` from the `Courses` object given its `short` using the `get(course_short)` method from the `Courses` class. Here's an example:
```python
course = Courses().get('CSTRUCT')
print(course.info['title'])
# Output: Computer Structure
```

### `topics.py`

### `config.py`

### `compile_sync_notes.py`

### `rofi.py`

### `rofi_notes.py`

### `rofi_edit_topic.py`

### `util.py`

### Scripts to improve programming workflow
### `compile_c_and_run.py`

