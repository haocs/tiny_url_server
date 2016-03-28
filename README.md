A shorten URL service using Flask and MySQL
---

## Features(TODO)
* [] Distribute Database
* [] Memcached
* [] Rate limit
* [] simple webui
* [] loggin and debuging
* [] performance test
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

## Running Tests
Forget TDD :)  
The only piece of code coverd by tests is urlconverter.py
```python
python -m tests.urlconverter-test
```
