from setuptools import setup, find_packages

requirements = []

with open('requirements.txt') as file:
    for line in file:
        if line:
            requirements.append(line)

setup(
    name='python_heroku_twitter_random_sentence_generator',
    packages=find_packages(),
    version='0.2',
    description='A Python Flask application that can post to a randomly generated sentence to Twitter using Heroku.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/python-heroku-twitter-random-sentence-generator',
    download_url='https://github.com/DEV3L/python-heroku-twitter-random-sentence-generator/tarball/0.2',
    keywords=['dev3l', 'facebook', 'graph', 'heroku', 'python', 'taylor swift', 'twenty one pilots' 'markov', 'flask'],
    install_requires=[
        requirements
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
