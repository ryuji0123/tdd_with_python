#!/bin/sh
. docker/env.sh
docker stop $CONTAINER_NAME
docker run \
  -dit \
  -v $PWD:/workspace \
  -p $DJANGO_PORT:$DJANGO_PORT \
  -p $NVC_HOST_PORT:$NVC_GUEST_PORT \
  --name $CONTAINER_NAME \
  --rm \
  --shm-size=2g \
  $IMAGE_NAME
