#!/bin/bash
if [ -n `which flask` ]; then
  FLASK_APP=app.py flask run -h 0.0.0.0
else
  echo "Please install Flask"
  return 1
fi
