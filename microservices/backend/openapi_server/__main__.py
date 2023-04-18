#!/usr/bin/env python3

import connexion
from flask import request

from openapi_server import encoder
from flask_cors import CORS, cross_origin
import sqlite3
from flask_injector import FlaskInjector
from injector import SingletonScope, inject


def configure(binder):
    binder.bind(sqlite3.Connection, to=sqlite3.Connection(':memory:'), scope=SingletonScope)


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Main API'},
                pythonic_params=True)
    
    FlaskInjector(app=app.app, modules=[configure])

    app.run(port=8080)


if __name__ == '__main__':
    main()
