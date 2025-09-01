"""Gunicorn configuration file."""

from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

ENVIRONMENT = environ.get("ENVIRONMENT")

proc_name = "flaskblueprint"
wsgi_app = "wsgi:app"
bind = "unix:flask.sock"
threads = 2
workers = 2

if ENVIRONMENT == "development":
    reload = True
    workers = 1
    threads = 1
    bind = ["127.0.0.1:8008"]
elif ENVIRONMENT == "production":
    daemon = True
    accesslog = "/var/log/flaskblueprint/info.log"
    errorlog = "/var/log/flaskblueprint/error.log"
    loglevel = "trace"
    dogstatsd_tags = "env:prod,service:flaskblueprint,language:python,type:tutorial"
else:
    raise ValueError(f"Unknown environment provided: `{ENVIRONMENT}`. Must be `development` or `production`.")
