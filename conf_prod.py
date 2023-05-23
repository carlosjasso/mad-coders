# Configuration overrides used for the production build

from conf_base import *

OUTPUT = "site"

# Ignored files
IGNORE_FILES = IGNORE_FILES + [
    "*.scss"
]
