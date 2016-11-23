Celtec Github Site
==================

Jobs website generated with [Python Pelican](https://github.com/getpelican/pelican) with [Nest theme](https://github.com/molivier/nest).

## Setup

```
pip install pelican --user
pip install Markdown --user
```

For more details, check [Pelican docs](http://docs.getpelican.com/en/stable/install.html)

### Install themes

```
git clone git@github.com:celtec/celtec-custom-nest.git /path/for/celtec/custom/nest/theme
pelican-themes --install /path/for/celtec/custom/nest/theme
```
## Preview

```
./develop_server.sh start
```

Then access [localhost:8000](http://localhost:8000)

To stop server just run:

```
./develop_server.sh stop
```

## Publishing

```
pelican content/ -o output/ -s publishconf.py
ghp-import -b master output/
git push origin master
```

Or just run:

```
./publish
```
