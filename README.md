# Rate Youtubers

## About

For now there's only boilerplate.

## Setup

You need to need to have the following pieces of software installed on your system:
- git
- Python 3, at least version 3.6
- pip
- [pipenv](https://pipenv.pypa.io/en/latest/)

Run the following commands:
```
git clone https://github.com/kolaczyn/rate-youtubers
cd rate-youtubers

pipenv install
pipenv shell

# create .env file
echo \
"SECRET_KEY=mysuperdupersecretkey 
FLASK_APP=rate_youtubers
FLASK_ENV=development" \
> .env

# initialize the database
flask create

flask run
```
