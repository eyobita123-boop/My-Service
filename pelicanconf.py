AUTHOR = 'Eyob Dereje Bekele'
SITENAME = 'Eyob Dereje Bekele | Financial & Digital Services'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Africa/Addis_Ababa'
DEFAULT_LANG = 'en'

# Theme
THEME = 'theme/eyob-theme'

# Use the custom home template for any page with slug 'home'
TEMPLATE_PAGES = {
    'pages/home.html': 'index.html',   # this makes the home page our custom template
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blog settings (keep for future)
DEFAULT_PAGINATION = False
