# python-heroku-twitter-random-sentence-generator

A Python Flask application that can post to a randomly generated sentence to Twitter.


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

Heroku
- 'HEROKU_HOUR_MODULO'
  - Used to work around Heroku's limited scheduler capabilities.
  - When set to a numerical value, will only post on the modulo
    - E.g.: '2' will limt post 12 times a day, '3' will limit posts to 8 times a day, etc 
- 'TWITTER_TAG'
  - Comma separated list (pick 1 at random) of hashtags or mentions to tag on to the end of the post 

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
$ git git@github.com:DEV3L/python-heroku-random-sentence-generator.git
$ cd python-heroku-random-taylor-swift-lyrics

$ mkvirtualenv -p /usr/local/bin/python3 python-heroku-random-sentence-generator-lyrics
$ python setup.py develop

$ python app.py --host 0.0.0.0 --port 5000
# OR
$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

- [localhost:5000](http://localhost:5000/)
- [Twitter](http://localhost:5000/facebook)
- [Facebook](http://localhost:5000/twitter)
