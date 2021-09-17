#!/bin/sh
. /workspace/docker/env.sh
python3 manage.py runserver $DJANGO_PORT
