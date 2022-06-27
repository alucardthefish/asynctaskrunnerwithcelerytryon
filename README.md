# Try out FastApi with Celery and Redis

Study from [here](https://testdriven.io/courses/fastapi-celery/getting-started/#H-7-sending-a-task-to-celery)

On windows it's necessary to add another option in order to make it work

run it by adding --pool=solo at the end

```sh
(env)$ celery -A main.celery worker --loglevel=info --pool=solo
```

