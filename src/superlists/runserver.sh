#!/bin/sh
. /workspace/docker/env.sh
python3 manage.py runserver 0.0.0.0:$DJANGO_PORT
