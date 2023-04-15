#!/bin/bash

cd ~/Documents/github/turtlebot/

git add .

git commit -m "Update bot code"

git push heroku master

heroku ps:scale worker=1

heroku logs --tail

