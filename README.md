# Flask Blueprint Tutorial

![Python](https://img.shields.io/badge/Python-v^3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v2.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/flask-blueprint-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-blueprint-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/flask-blueprint-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-blueprint-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/flask-blueprint-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-blueprint-tutorial/network)

![Flask Blueprint Tutorial](https://github.com/hackersandslackers/flask-blueprint-tutorial/blob/master/.github/flaskblueprints-3@2x.jpg?raw=true)

Structure your Flask apps in a scalable and intelligent way using Blueprints.

This repository contains source code for the accompanying tutorial on Hackers and Slackers: https://hackersandslackers.com/flask-blueprints/

A live demo of this repository can be found here: https://flaskblueprints.hackersandslackers.app/


## Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/hackersandslackers/flask-blueprint-tutorial.git
$ cd flask-blueprint-tutorial
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ flask run
```

**Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)**:

```shell
$ git clone https://github.com/hackersandslackers/flask-blueprint-tutorial.git
$ cd flask-blueprint-tutorial
$ pipenv shell
$ pipenv update
$ flask run
```

**Installation via [Poetry](https://python-poetry.org/)**:

```shell
$ git clone https://github.com/hackersandslackers/flask-blueprint-tutorial.git
$ cd flask-blueprint-tutorial
$ poetry shell
$ poetry update
$ poetry run
```

## Usage

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
* `FLASK_ENV`: The environment to run your app in (either `development` or `production`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `LESS_BIN`: Path to your local LESS installation via `which lessc` (optional for static assets).
* `ASSETS_DEBUG`: Debug asset creation and bundling in `development` (optional).
* `LESS_RUN_IN_DEBUG`: Debug LESS while in `development` (optional).
* `COMPRESSOR_DEBUG`: Debug asset compression while in `development` (optional).


*Remember never to commit secrets saved in .env files to Github.*

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
