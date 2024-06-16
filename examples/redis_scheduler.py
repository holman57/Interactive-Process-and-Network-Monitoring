from datetime import datetime, timedelta
from redis import Redis
from rq_scheduler import Scheduler

# https://www.redwood.com/article/python-job-scheduling/
# https://redis.io/docs/latest/develop/connect/clients/python/

redis_conn = Redis(host='localhost', port=6379)

scheduler = Scheduler(connection=redis_conn)


def my_job():
    print("hello from my_job() !")


scheduler.schedule(
    # start immediately
    scheduled_time=datetime.utcnow(),
    func=my_job,
    interval=timedelta(minutes=1)
)
