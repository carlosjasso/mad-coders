# Mad Coders

This project holds the documents and tools needed to generate the Mad Coders website.

## 🛠 Tools information

- [Python](https://python.org) - programming language
- [Pelican](https://getpelican.com/) - static site generator
- [VSCode](https://code.visualstudio.com/) - text editor

## ⚙ Setup

This project requires python 3.7+. To set it up:

- It's recommended to use a python [venv](https://docs.python.org/3/library/venv.html)
  - install the module with the command `pip install virtualenv --upgrade`
  - setup the virtual environment with the command `python3 -m venv .venv`
- In VSCode, it's recommended to set the python interpreter to point to the virtual environment via `Command Palette` > `Python: Select Interpreter`

## 💻 Project automated tasks

Execute `python3 tasks.py` to see available CLI options or checkout the [tasks.json](.vscode/tasks.json) file to see what VSCode tasks are available to be executed from the Command Palette.

> _**Note:**_ VSCode Tasks will use the selected python interpreter.
