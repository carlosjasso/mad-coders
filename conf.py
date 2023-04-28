# More: https://docs.getpelican.com/en/latest/settings.html

SITENAME = "Mad Coders"
PATH = "articles"
DEFAULT_LANG = "en"

ARTICLE_OUTPUT_PATH = "articles"
ARTICLE_SAVE_AS = f"{ARTICLE_OUTPUT_PATH}/{{slug}}.html"

# Disable not needed pages
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAG_SAVE_AS = ""

# Disable feed generation
TIMEZONE = "America/Mexico_City"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Ignore example files
IGNORE_FILES = ["*.example.*"]

# Theme configuration
THEME = "./theme"
