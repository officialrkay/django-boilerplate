import os

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'assets/style/scss'),
    os.path.join(BASE_DIR, 'node_modules'),
]

SASS_PROCESSOR_AUTO_INCLUDE = False

SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'

SASS_OUTPUT_STYLE = 'compact'

SASS_PRECISION = 8
