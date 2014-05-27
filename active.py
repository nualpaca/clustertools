import os
from celery import Celery
rabbitmq = os.getenv('BROKER_URL')
app = Celery(backend=rabbitmq, broker=rabbitmq)
i = app.control.inspect()

active_tasks = i.active()

for worker,tasks in active_tasks.iteritems():
	print worker
	for task in tasks:
		print "    ", task['args'], task['name'], task['id']
		# res = app.AsyncResult(task['id'])
		# print res.status
		# print res.info