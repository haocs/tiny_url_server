A shorten URL service using Flask and MySQL
---

## Features(TODO)
* [ ] Memcached/redis caching
* [ ] Rate limit
* [ ] Simple webui
* [ ] Distribute Database
* [ ] Logging and debuging
* [ ] Performance test
* custom URL(optional)

## System and Environment:
* OS: *(default for linux)
* python: 2.7.* (If all the dependencies are working well with py3, should upgrade to 3)
* flask: 0.10.*
* db: mysql/mariadb

## Setup
* Create DB and DB user
```bash
DB:
  name:devdb
  user:tiny_url
  passwd:tiny1234
```

* Or running db setup scirpts:
```bash
mysql -uroot -ppasswd < create_user_dev.sql
mysql -uroot -ppasswd < init_db.sql
```
* Install dependencies
```bash
# mysql client
sudo apt-get install libmysqlclient-dev # mysql
sudo apt-get install libmariadbclient-dev # mariaDB
# python-dev 
sudo apt-get install python-dev # ubuntu
sudo zypper install python-devel # opensuse
```
* Install flask
```bash
# install pip
# install virtualenv
pip install -r requirements.txt
```

## Use
* Start
```bash
python app.py
```

* With cURL:
```bash
# visit:
curl localhost:5000
# generate short url:
cur --form "origin_url='haoc.io'" localhost:5000/v
# visit short url:
curl "localhost:5000/v/******
```

## Running Tests
Forget TDD :)  
The only piece of code coverd by tests is urlconverter.py
```python
python -m tests.urlconverter-test
```
