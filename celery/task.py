from app import celery


@celery.task
def celery_checker():
    return 'SUCCESS'


@celery.task
def smtp_sender():
    pass


@celery.task
def python_executor():
    pass


@celery.task
def mysql_executor():
    pass
