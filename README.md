# python-heroku-random-taylor-swift-lyrics

A Python Flask application that can post to Facebook or Twitter a random taylor swift lyric.


## References

Setting up a new Flask application

- [Setting Up Flask on Nitrous](https://community.nitrous.io/tutorials/setting-up-flask-on-nitrous)
- [Deploying a Flask Application to Heroku](https://community.nitrous.io/tutorials/deploying-a-flask-application-to-heroku)
- [Python Facebook tutorial - post to Facebook page in 4 steps](http://nodotcom.org/python-facebook-tutorial.html)
- [Introduction to tweepy, Twitter for Python](http://pythoncentral.io/introduction-to-tweepy-twitter-for-python/)


## Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
- [Heroku toolbelt](https://devcenter.heroku.com/articles/heroku-command-line)


## Environment Variables

Facebook
[Python Facebook tutorial - post to Facebook page in 4 steps](http://nodotcom.org/python-facebook-tutorial.html)
- 'FACEBOOK_PAGE_ID'
- 'FACEBOOK_USER_ACCESS_TOKEN'

Twitter
[Introduction to tweepy, Twitter for Python](http://pythoncentral.io/introduction-to-tweepy-twitter-for-python/)
- 'TWITTER_CONSUMER_KEY'
- 'TWITTER_CONSUMER_SECRET' 
- 'TWITTER_ACCESS_TOKEN'
- 'TWITTER_TOKEN_SECRET'


## Running Locally

```sh
$ git git@github.com:DEV3L/python-heroku-random-taylor-swift-lyrics.git
$ cd python-heroku-random-taylor-swift-lyrics

$ mkvirtualenv -p /usr/local/bin/python3 heroku-random-taylor-swift-lyrics
$ python setup.py develop

$ python app.py --host 0.0.0.0 --port 5000
# OR
$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

- [localhost:5000](http://localhost:5000/)
- [Twitter](http://localhost:5000/facebook)
- [Facebook](http://localhost:5000/twitter)
