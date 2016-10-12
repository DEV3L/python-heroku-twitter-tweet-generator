# python-heroku-random-taylor-swift-lyrics

A Python Flask application that can post to Facebook a random taylor swift lyric


## References

Setting up a new Flask application

- [Setting Up Flask on Nitrous](https://community.nitrous.io/tutorials/setting-up-flask-on-nitrous)
- [Deploying a Flask Application to Heroku] (https://community.nitrous.io/tutorials/deploying-a-flask-application-to-heroku)


## Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
- [Heroku toolbelt](https://devcenter.heroku.com/articles/heroku-command-line)


## Running Locally

```sh
$ git git@github.com:DEV3L/python-heroku-random-taylor-swift-lyrics.git
$ cd python-heroku-random-taylor-swift-lyrics

$ mkvirtualenv -p /usr/local/bin/python3 heroku-random-taylor-swift-lyrics
$ python setup.py develop

$ python app.py --host 0.0.0.0 --port 5000

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

