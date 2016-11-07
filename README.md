Celtec Jobs
===========

Jobs website generated with [Python Pelican](https://github.com/getpelican/pelican) with [Nest theme](https://github.com/molivier/nest).

## Setup

```
pip install pelican
```

For more details, check [Pelican docs](http://docs.getpelican.com/en/stable/install.html)

## Publishing

```
pelican content/ -o output/ -s publishconf.py
ghp-import output/
git push origin gh-pages
```
