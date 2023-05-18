import os

# More: https://docs.getpelican.com/en/latest/settings.html

SITENAME = "Mad Coders"
PATH = "articles"
DEFAULT_LANG = "en"

ARTICLE_OUTPUT_PATH = PATH
ARTICLE_SAVE_AS = f"{ARTICLE_OUTPUT_PATH}/{{slug}}.html"

STATIC_PATHS = ["static"]

OUTPUT = "output"

# Disable not needed pages
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

# Disable feed generation
TIMEZONE = "America/Mexico_City"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Ignored files
IGNORE_FILES = [
    "*.example.*",
    "*.psd"
]

# Theme configuration
THEME = "./theme"
THEME_STATIC_DIR = "resources"
THEME_STATIC_PATHS = [THEME_STATIC_DIR]
