#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Celtec Rastreamento'
SITENAME = u'Celtec Rastreamento'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
SOCIAL = (('IVEI', 'https://www.ivei.com.br'),
         ('Github', 'https://github.com/celtec'),
         ('Autocargo', 'https://www2.autocargo.com.br')
         )

# Social widget
NEST_SITEMAP_MENU = (('LinkedIn', 'https://www.linkedin.com/company/3855537'),
          ('Facebook', 'https://www.facebook.com/inteligenciaveicular'),
          ('Instagram', 'https://www.instagram.com/ivei.veicular')
          )

DEFAULT_PAGINATION = False

THEME = 'nest'

## NEST TEMPLATE CONF
SITESUBTITLE = u'Celtec Rastreamento'
# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages
MENUITEMS = [('Jobs', '/category/open-positions.html'),('About','/about.html')]
# Add header background image from content/images : 'background.jpg'
#NEST_HEADER_IMAGES = 'banner-homepage.jpg'
NEST_HEADER_LOGO = '/images/logo_celtec.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Social'
NEST_SOCIAL_COLUMN_TITLE = u'Links'
#NEST_LINKS_COLUMN_TITLE = u'Links'
NEST_COPYRIGHT = u'&copy; Celtec Rastreamento Jobs'
# Footer optional
NEST_FOOTER_HTML = """
<style type="text/css">
.header-container {
    background: #233b6f !important;
}

.footer.gradient-2 {
    background-color: #e2e2e2;
    color: #233b6f;
    border-top: 1px solid #b5b5b5;
}

.footer.gradient-2 a {
    color: #101213;
}
</style>

<div style="position:absolute;left:-215px;top:8px">
    <a href="https://www.ivei.com.br" target="_blank" style="display:block">
        <img src="/images/logo_ivei.png" title="IVEI" />
    </a>

    <a href="https://www2.autocargo.com.br" target="_blank" style="display:block;margin-top: 15px">
        <img src="/images/logo_autocargo.png" title="Autocargo" />
    </a>
</div>
"""
# index.html
NEST_INDEX_HEAD_TITLE = u'Homepage'
NEST_INDEX_HEADER_TITLE = u'Jobs'
NEST_INDEX_HEADER_SUBTITLE = u'Celtec Rastreamento Open Positions'
NEST_INDEX_CONTENT_TITLE = u'Open Positions'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archives for all posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# article.html
NEST_ARTICLE_HEADER_BY = u'By'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives listed by category'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Category Archive'
NEST_CATEGORY_HEADER_TITLE = u'Category'
NEST_CATEGORY_HEADER_SUBTITLE = u'Category Archive'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archives'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archives'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'
# Static files
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'}
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
