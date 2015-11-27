import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repo')
SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = True
SECRET_KEY = 'anfdsa9840#@$(asdf{!@#^#VzcAsd'

OPENID_PROVIDERS = [
    {
        'name': 'Yahoo',
        'url': 'https://me.yahoo.com',
    },
    {
        'name': 'AOL',
        'url': 'http://openid.aol.com',
    },
    {
        'name': 'Flickr',
        'url': 'http://www.flickr.com/<username>',
    },
    {
        'name': 'MyOpenID',
        'url': 'https://www.myopenid.com',
    },
]

POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50
