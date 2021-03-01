#!/bin/sh

pipenv install
pipenv shell

# create .env file
echo \
"SECRET_KEY=mysuperdupersecretkey
FLASK_APP=rate_youtubers
FLASK_ENV=development" \
> .env

cd rate_youtubers/static
# use npm, unless yarn is installed
if [ $(yarn --version) ]; then
  yarn install
else
  npm install
fi
npm run compile-styles
cd ../..

# initialize the database
flask create
