# Rate Youtubers

## About

You can rate (almost) any video on YouTube. But you can't really rate YouTubers. This website lets you do that.

## Setup

You need to need to have the following pieces of software installed on your system:

- git
- Python 3, at least version 3.6
- pip
- [pipenv](https://pipenv.pypa.io/en/latest/)

Run the following commands:

```bash
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

The app runs on [localhost:5000](http://localhost:5000/).

After you completed these steps once, all you have to do next time is:

```bash
pipenv shell
flask run
```


## User Stories

1. You can log in
1. Confirm email, change password
1. Admin can delete reviews, users etc.
1. You can leave a rating with a message
1. You can reply to reviews
1. YouTuber can reply to review to his channel (I'm not sure yet if it's possible)


## Todo

1. Authentication
1. Authorization
1. Define schemas etc
1. Not store passwords as plain text
1. Populate YouTuber's basic data at the first review
1. YouTubers can confirm their identity with signing up with YouTube
1. Templates to navbar, footer, etc
1. Real database
1. Create API's documentation
