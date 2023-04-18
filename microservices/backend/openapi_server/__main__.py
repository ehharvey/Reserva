#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from flask_cors import CORS, cross_origin



def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Main API'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()
