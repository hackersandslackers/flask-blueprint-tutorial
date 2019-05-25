"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask Session Tutorial',
    version='0.0.1',
    description='Example Flask project for implementing Flask-Session with Redis.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/toddbirchard/flasksession-tutorial',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Flask Flask-Session Redis Session Tutorial',
    packages=find_packages(),  # Required
    install_requires=['flask',
                      'flask_login',
                      'flask_sqlalchemy',
                      'flask_assets',
                      'flask_session',
                      'redis',
                      'psycopg2-binary',
                      'wtforms'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            '__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/toddbirchard/flasksession-tutorial/issues',
        'Source': 'https://github.com/toddbirchard/flasksession-tutorial/',
    },
)
