# Try out FastApi with Celery and Redis

Study from [here](https://testdriven.io/courses/fastapi-celery/getting-started/#H-7-sending-a-task-to-celery)

## Manual Test

Run a worker in one terminal window:

```sh
(env)$ celery -A main.celery worker --loglevel=info
```

On windows it's necessary to add another option in order to make it work

run it by adding --pool=solo at the end

```sh
(env)$ celery -A main.celery worker --loglevel=info --pool=solo
```

## Simple test using docker-compose

Let's test things out by entering the Python shell of the running web service:

```sh
$ docker-compose exec web python
```

after that, just run next instructions

```py
>>> from main import app
>>> from project.users.tasks import divide
>>>
>>> divide.delay(1, 2)
<AsyncResult: aeaff43e-9807-49ed-8118-8537c00e35a9>
```

