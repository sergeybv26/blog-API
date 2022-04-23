#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
  echo "Waiting for start postgres..."

  while [ ! nc -z $SQL_HOST $SQL_PORT ]; do
      sleep 0.1
  done

  echo "PostgreSQL is started"
fi

exec "$@"