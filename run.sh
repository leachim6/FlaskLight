#!/bin/bash
if [ -n `which flask` ]; then
  FLASK_APP=app.py flask run
else
  echo "Please install Flask"
  return 1
fi
