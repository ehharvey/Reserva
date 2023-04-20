#! /bin/bash

./create_all_routes.py
./create_all_schemas.py

swagger-cli bundle ./service_routes/_all.yaml -o all.json