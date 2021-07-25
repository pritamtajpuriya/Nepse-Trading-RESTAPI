# Nepse-Trading-RESTAPI
Live Stock , Company listed  API build with Beatiful Soup & Django REST Framework
## Getting Started

### Requirement
Celery requires a message broker to send and receive messages, so we have to utilize RabbitMQ as a solution
You can install RabbitMQ through Ubuntu’s repositories by the following command:

```
$ sudo apt-get install rabbitmq-server
```
### Virtual Environment
To create Virtual environment
```
python3 -m venv venv (name of env anything)
```
To activate 

```
source venv/bin/activate
```

  
### Install the project dependencies

```
python3 -m pip3 install -r requirements.txt
```

### Run project

run following commands:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
start Celery worker:
```
celery -A nepsetrade worker -l info
```
