from os import path

# Project configuration
WORKSPACE_PATH = path.dirname(path.abspath(__name__))
# python required version based on pelican requirements
# info: https://docs.getpelican.com/en/latest/quickstart.html#installation
REQUIRED_PYTHON_VERSION_MAJOR = 3
REQUIRED_PYTHON_VERSION_MINOR = 7

# Pelican configuration
# More: https://docs.getpelican.com/en/latest/settings.html
SITENAME = "Mad Coders"
DEFAULT_LANG = "en"
TIMEZONE = "UTC"

PATH = "articles"

ARTICLE_OUTPUT_PATH = PATH
ARTICLE_SAVE_AS = f"{ARTICLE_OUTPUT_PATH}/{{slug}}.html"
ARTICLE_ORDER_BY = "reversed-modified"

OUTPUT_DEV = "output"
OUTPUT_PROD = "site"
DELETE_OUTPUT_DIRECTORY = True

CACHE_PATH = ".cache"

# Disable not needed pages
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

# Disable feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Ignored files
IGNORE_FILES = [
    "*.psd",
    "*.scss",
    "*.js"
]

# Theme configuration
THEME = "theme"
THEME_STATIC_DIR = "resources"
THEME_STATIC_PATHS = [THEME_STATIC_DIR]
