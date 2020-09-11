# Watchlist

### [Raphael Katana](https://github.com/RKatana)

This project is powered by [The Movie Database API](https://www.themoviedb.org/).

### Technologies used
- Python 
- Flask
- Bootstrap4

### Application dependencies
```
certifi==2020.6.20
chardet==3.0.4
click==7.1.2
dominate==2.5.2
Flask==1.1.2
Flask-Bootstrap4==4.0.2
Flask-Script==2.0.6
Flask-WTF==0.14.3
gunicorn==20.0.4
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
requests==2.24.0
urllib3==1.25.10
visitor==0.1.3
Werkzeug==1.0.1
WTForms==2.3.3

```
### Setup instructions
> create an account on https://www.themoviedb.org/ to access the api key. Read the documentation for more details.

> `git clone https://github.com/RKatana/watchlist.git`  to your machine

> On your terminal(commandline)` cd watchlist`

> create and activate virtual environment `python3 -m venv virtual && source virtual/bin/activate`

> install dependencies from requirements.txt file `pip install -r requirements.txt`

> create a .env file and add your api key and secret key to the .env file in the format shown in the .env-sample file

> run your application using `make serve` or `python manage.py serve`

### Link to the site
https://watchlist-mc31.herokuapp.com/