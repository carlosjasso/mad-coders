# Mad Coders

This project holds the documents and tools needed to generate the Mad Coders website.

## 🤓 Technicalities

### 🛠 Tools information

- [Python](https://python.org) - programming language
- [Pelican](https://getpelican.com/) - static site generator
- [VSCode](https://code.visualstudio.com/) - text editor

### ⚙ Setup

This project requires python 3.7+. To set it up:

- It's recommended to use a python [venv](https://docs.python.org/3/library/venv.html)
  - install the module with the command `pip install virtualenv --upgrade`
  - setup the virtual environment with the command `python3 -m venv .venv`
- In VSCode, it's recommended to set the python interpreter to point to the virtual environment via `Command Palette` > `Python: Select Interpreter`
- Install python required packages with the command `pip install -r requirements.txt`

### 💻 Project automated tasks

Execute the `python3 -m tasks` command to see the available CLI options or check out the [tasks.json](.vscode/tasks.json) file to see what VSCode tasks are available to be executed from the Command Palette.

> 💡 VSCode Tasks will use the selected python interpreter.

---

## 🎯 Generalities

### 📝 Pelican article frontmatter properties

There are several properties that can be set on an article's frontmatter to provide Pelican with metadata. Some of those properties are:

```yaml
---
title: Example # Title of the article or page
date: 2023-05-25T23:50:39+00:00 # Creation date in UTC timezone and ISO-8601 format
modified: 2023-05-25T23:50:39+00:00 # Modification date in UTC timezone and ISO-8601 format
tags: example, article, placeholder # Content tags, separated by commas
keywords: HTML, CSS, JavaScript # Content keywords, separated by commas (HTML content only)
category: example # Content category (one only — not multiple)
slug: article-slug-example #Identifier used in URLs and translations
author: Author Example # Content author, when there is only one
authors: Author Example1, Author Example2 # Content authors, when there are multiple
summary: An example article # Brief description of content for index pages
lang: en # Content language ID (en, fr, etc.)
translation: false # If content is a translation of another (true or false)
status: hidden # Content status (draft, hidden, published)
template: example # Name of template to use to generate content (without extension)
save_as: /some/relative/path # Save content to this relative file path
url: /example/url # URL to use for this article/page
---
```

Visit the *[Pelican Documentation Site](https://docs.getpelican.com/en/latest/content.html#file-metadata)* for more information.
