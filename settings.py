
import platform

from danube_delta.settings import *  # NOQA


# Authors
AUTHOR = 'Python\u00A0v\u00A0ČR'
SITENAME = 'Python\u00A0v\u00A0ČR bloguje'
SITESUBTITLE = 'Zprávy z\u00A0české Python komunity'

ABOUT = '''
Tento blog píše [česká komunita kolem programovacího jazyka Python](https://python.cz/).
I ty sem můžeš napsat článek! Chceš oznámit nějakou akci, zamyslet se nad budoucností
[srazů](https://pyvo.cz/) nebo sepsat, co se ti líbilo na [konferenci](https://cz.pycon.org)?
Stačí [postupovat podle návodu](https://github.com/pyvec/blog.python.cz/#write-an-article-in-5-steps).
'''
ABOUT_IMAGE = 'images/about.png'


# Production settings
if PRODUCTION:  # NOQA
    SITEURL = 'https://blog.python.cz'


# Theming
DISQUS_SITENAME = 'blog-python-cz'
SIMPLE_ANALYTICS = True
GOOGLE_FONTS = ['Arbutus Slab']


# Drafts and hidden articles
DRAFT_URL = '{slug}'
DRAFT_SAVE_AS = '{slug}.html'
