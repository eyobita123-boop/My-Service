AUTHOR = 'Eyob Dereje Bekele'
SITENAME = 'Eyob Dereje Bekele | Financial & Digital Services'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Africa/Addis_Ababa'
DEFAULT_LANG = 'en'

# Theme
THEME = 'theme/my_theme'

# Feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blog settings
DEFAULT_PAGINATION = False

# Default metadata
DEFAULT_METADATA = {
    'status': 'draft',
}

# Direct templates to render
DIRECT_TEMPLATES = ['index', 'thanks']

# Static paths - THIS COPIES YOUR PHOTO TO OUTPUT
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/eyob-hero.jpg': {'path': 'eyob-hero.jpg'},
}
