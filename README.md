# University setup for Computer Science
![GitHub](https://img.shields.io/github/license/rixsilverith/university-setup?style=flat-square)
> Hey! Welcome to my university setup repository. Here you'll find a set of scripts I use to manage my lecture notes and coursework on computer science and maths, as well as some files like `preamble.tex` ment to improve the note-taking experience in LaTeX.
>
> These scripts carry out tasks from automatically creating all the necessary files and folders for a new course to compiling all of the notes of a specific course and backing them up on the cloud.
>
> If you feel curious, a collection of all my lecture notes can be found [here](github.com/rixsilverith/uni-notes-cw).

### Getting started and configuration
<details>
<summary><b>Download this repository</b></summary>
Begin by cloning this repo in your computer. I encourage you to use the [GitHub CLI](https://github.com/cli/cli):
```bash
gh repo clone rixsilverith/university-setup
```
You can always do it the classical way by running
```bash
git clone https://github.com/rixsilverith/university-setup.git
```
</details>
<details>
<summary><b>Installing Rofi</b></summary>
You'll need [Rofi]() installed in your system for the main scripts to run properly. If you haven't installed it yet, you'll want to do it now. Otherwise, most of the scripts will just don't work.
</details>
<details>
<summary><b>Installing Simple X HotKey Daemon</b></summary>
In order to run some scripts efficiently, you'll need to keybind some of them. A great tool to achieve this is [Simple X HotKey Daemon](https://github.com/baskerville/sxhkd), or *sxhkd* for short. Once it's installed in your machine copy the `sxhkd` folder inside the `university-setup` directory and paste it in your system's configuration folder, which in Arch Linux corresponds to `~/.config/`. If you pasted this folder in any other directory you should edit the path after the `-c` flag in the `launch.sh` file inside it and write where you put the `sxhkd` folder. Then, add the `launch.sh` file to your autorun so you have your keybinds available since the system start.
</details>
<details>
<summary><b>Other dependencies</b></summary>
Of course, it's essential to have [Python]() installed in your system in order to run Python scripts.
</details>
<details>
<summary><b>Configuration and customization</b></summary>
Inside the `university-setup` you just downloaded you'll find the `config.yaml` file. This is the main configuration file from which most of the scripts will retrieve data. Here's its content:
```yaml
root_dir: ~/Uni
pdf_viewer: zathura
```
You should replace the `root_dir` key value with the path to the folder in which you'll place all your university related files: lecture notes, coursework, slides, etc. This folder must be structured as it's shown in the next section (`root_dir` folder and course structure). The default PDF viewer to open the compiled LaTeX files is Zathura, but you can use the one of your choice by changing the `pdf_viewer` key to the name of its executable file.
</details>

### `root_dir` folder and course structure
<details>
<summary><b>`root_dir` folder structure</b></summary>
The `root_dir` (`Uni`) folder is the one containing all the university related files, from lecture notes to coursework and random slides and PDFs. In order for the scripts to work properly this folder should be structured as it's shown below.
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
Each year of the bachelor is represented by its respective folder named `CompSci-x`, where x is the year. A year is split into two semesters, represented by the `semester-1` and `semester-2` folders, which both contains the courses directories of corresponding to that semester. Here, the `preamble.tex` file is worth of mention. It contains the preamble included in all of the LaTeX files.
</details>

<!--
*Note: If you're reading this, I assume you know, at least, what is LaTeX. If not, the [latex-project.org](https://www.latex-project.org/) website is a good starting point.* 
-->

<details>
<summary><b>Course structure</b></summary>
As I mentioned earlier, the `semester-1` and `semester-2` folders contain the courses I'm taking on each of the semesters. A course is structured as it's shown below.
```
semester-2
├── CALC2
│   ├── notes
│   │   ├── master.tex
│   │   ├── topic_01.tex
│   │   ├── topic_02.tex
│   │   └── ...
│   ├── coursework
│   │   ├── ps_01_1.tex
│   │   ├── ps_01_2.tex
│   │   ├── ps_02_1.tex
│   │   └── ...
│   └── figures
│       ├── uam.png
│       ├── divergence-theorem.svg
│       └── ...
├── CSTRUCT
└── ...
```
Here, we must point out the `info.yaml` and `master.tex` files. The first one contains information about a course; it's title, short, in which group I am, the class/lab where it's taken and a reference to the course guide.
```yaml
title: Computer Basics
short: COMPB
groups:
    lectures: 119
    lab: 1191
c_guide: ~/Uni/CompSci-1/semester-1/COMPB/course_guide.pdf
```
The semester and year is which course is taken, as well as the language, are parsed from the group number. In my university the three numbers (four, in case of practical courses) represents the semester, year and group, respectively. In practical courses, such as Computer Lab, another number is added, which represents the practice group.

Secondly, the `master.tex` file is in charge of bundling up all the topics of the course into a single file, the one that will be compiled by LaTeX compiler.  Here is the content of the `master.tex` file:

```latex
\documentclass[a4paper, twoside, 11pt]{article}
\input{../preamble.tex}
\graphicspath{{./figures}}

\begin{document}
\title{Calculus I (CALC1 119) notes}{First year}{First semester}
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
</details>

### Scripts
<details>
<summary><b>`init_course.py`</b></summary>
Inititalize a new course given a title, a short and a group code. The course folder will be created on the semester and year parsed from the group code, as well as the language. The default path for the course guide is `~/Uni/CompSci-x/semester-x/course_short/course_guide.pdf`, and it should be changed manually in case of need.
</details>

<details>
<summary><b>`courses.py`</b></summary>
In this file the `Course` and `Courses` classes are defined. The later is just a list of `Course`s in the `Uni` folder, while the former represents a course directory. A `Course` has a `short`, a `path` and an `info` property, a Python dictionary from which you can retrieve information about the course. This info is collected from the `info.yaml` file in the course folder. You can also access the course topics by reading the `topics` property, which is a `Topics` object (a list of `Topic`s).

You can get a specific `Course` from the `Courses` object given its `short` using the `get(course_short)` method from the `Courses` class. Here's an example:
```python
course = Courses().get('CSTRUCT')
print(course.info['title'])
# Output: Computer Structure
```
</details>

<details>
<summary><b>`topics.py`</b></summary>
*Work in progress.*
</details>

<details>
<summary><b>`config.py`</b></summary>
Defines the `Config` class, which acts as a helper to interact with the `config.yaml` file.
</details>

<details>
<summary><b>`compile_sync_notes.py`</b></summary>
*Work in progress.*
</details>

<details>
<summary><b>`rofi.py`</b></summary>
A wrapper function for Rofi.
</details>

<details>
<summary><b>`rofi_notes.py`</b></summary>
*Work in progress.* 
</details>

<details>
<summary><b>`rofi_edit_topic.py`</b></summary>
*Work in progress.*
</details>

<details>
<summary><b>`util.py`</b></summary>
Some utility functions.
</details>

<details>
<summary><b>`compile_c_and_run.py`</b></summary>
*Work in progress.* The idea is to use a global `gccr` command to compile and run C programs.
</details>
