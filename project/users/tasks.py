from celery import shared_task


@shared_task
def divide(x, y):
    import time
    time.sleep(10)
    return x / y

@shared_task
def multiply(x, y):
    import time
    time.sleep(25)
    result = x * y
    return f"The result of {x} times {y} is : {result}"
