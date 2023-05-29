import os

from conf_base import *

# Configuration overrides used for the production build

OUTPUT = "site"


# Ignored files
###
# these are not ignored on the base configuration for pelican to detect changes on them
# and process them every time they change. This is useful on the development environment.
###
IGNORE_FILES = IGNORE_FILES + [
    "*.scss",
    "*.js"
]


# Theme configuration
JS_FILTER = "rjsmin"


# Envinronment variables
os.environ["LIBSASS_STYLE"] = "compressed"
