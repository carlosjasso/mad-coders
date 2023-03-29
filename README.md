# nst-mad-coders-docs

This project holds the static site generator tool used to render the NST CoE Mad Coders documents.

## 🛠 Tools information

- [Python](https://python.org) - programming language
- [Pelican](https://getpelican.com/) - static site generator
- [VSCode](https://code.visualstudio.com/) - text editor

## ⚙ Setup

This project has been built on top of python 3.11.2 on linux. To set it up:

- Run on a python [venv](https://docs.python.org/3/library/venv.html)
  - create venv: `python3 -m venv .venv`
  - source venv: `source .vevn/bin/activate`
  - verify venv is active: `which python`
    > Expected output: `<working-dir-path>/.venv/bin/python`
- In VSCode, it's recommended to set the python interpreter to point to the venv via `ctrl` + `shift` + `p` > `Python: Select Interpreter`
