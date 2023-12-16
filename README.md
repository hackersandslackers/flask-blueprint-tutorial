# Flask Blueprint Tutorial

![Python](https://img.shields.io/badge/Python-v3.10-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v3.0.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v2.1.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Gunicorn](https://img.shields.io/badge/Gunicorn-v21.2.0-blue.svg?longCache=true&logo=gunicorn&style=flat-square&logoColor=white&colorB=a3be8c&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/flask-blueprint-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-blueprint-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/flask-blueprint-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-blueprint-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/flask-blueprint-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-blueprint-tutorial/network)

![Flask Blueprint Tutorial](./.github/img/flaskblueprints@2x.jpg?raw=true)

Structure your Flask apps in a scalable and intelligent way using Blueprints.

* **Tutorial**: [https://hackersandslackers.com/flask-blueprints/](https://hackersandslackers.com/flask-blueprints/)
* **Demo**: [https://flaskblueprints.hackersandslackers.app/](https://flaskblueprints.hackersandslackers.com/)

## Getting Started

Get set up locally in two steps:

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `ENVIRONMENT`: The environment in which to run your application (either `development` or `production`).
* `FLASK_DEBUG`: Set to `True` to enable Flask's debug mode (default to `False` in prod).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.

*Remember never to commit secrets saved in .env files to Github.*

### Installation

Get up and running with `make run`:

```shell
git clone https://github.com/hackersandslackers/flask-blueprint-tutorial.git
cd flask-blueprint-tutorial
make deploy
```

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
