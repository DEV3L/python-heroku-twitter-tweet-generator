from setuptools import setup, find_packages

setup(
    name='python_heroku_random_taylor_swift_lyrics',
    packages=find_packages(),
    version='0.1',
    description='Flask application that can post to Facebook a random taylor swift lyric.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/python-heroku-random-taylor-swift-lyrics',
    download_url='https://github.com/DEV3L/python-heroku-random-taylor-swift-lyrics/tarball/0.1',
    keywords=['dev3l', 'facebook', 'graph', 'heroku', 'python', 'taylor swift', 'markov', 'flask'],
    install_requires=[
        'Flask==0.10.1',
        'Flask-Runner==2.1.1',
        'Flask-Script==0.6.7',
        'Jinja2==2.8',
        'MarkupSafe==0.23',
        'Werkzeug==0.11.11',
        'click==6.6',
        'facebook-sdk==2.0.0',
        'gunicorn==19.6.0',
        'itsdangerous==0.24',
        'nose==1.3.7',
        'ordered-set==2.0.1',
        'requests==2.11.1',
        'tweepy==3.5.0'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
