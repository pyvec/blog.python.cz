
import platform

from danube_delta.settings import *  # NOQA


# Authors
AUTHOR = 'Python v ČR'
SITENAME = 'Python v ČR bloguje'
SITESUBTITLE = 'Zprávy z české Python komunity'

ABOUT = '''
Tento blog píše [česká komunita kolem programovacího jazyka Python](http://python.cz/).
I ty sem můžeš napsat článek! Chceš oznámit nějakou akci, zamyslet se nad budoucností
[srazů](http://pyvo.cz/) nebo sepsat, co se ti líbilo na [konferenci](https://cz.pycon.org)?
Stačí [postupovat podle návodu](https://github.com/pyvec/blog.python.cz/#write-an-article-in-5-steps).
'''
ABOUT_IMAGE = 'images/about.png'


# Production settings
if PRODUCTION:  # NOQA
    SITEURL = 'http://blog.python.cz'


# Theming
DISQUS_SITENAME = 'blog-python-cz'
GOOGLE_ANALYTICS = 'UA-1316071-20'
GOOGLE_FONTS = ['Arbutus Slab']
