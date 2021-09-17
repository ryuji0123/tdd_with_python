#!/bin/sh
. ./docker/env.sh
docker exec \
  -it \
  "${USER}_${REPOSITORY_NAME}" zsh
