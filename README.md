## Getting Started
### Create virtual environment and install packages
In project folder run:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```


### Setup database
 - make sure PostgreSQL is installed and running on your system
 - login to postgres and create database gameshop
 - check and edit postgres credentials in import_xml.py and gameshop/settings.py
 
Create table:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
Import data:
```
$ python import_xml.py
```

### Run app
```
$ python manage.py runserver
```