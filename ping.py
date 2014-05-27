import os
from celery import Celery

import colorama
colorama.init(autoreset=True)

rabbitmq = os.getenv('BROKER_URL')
app = Celery(backend=rabbitmq, broker=rabbitmq)
worker_statuses = app.control.ping()

for worker_status in worker_statuses:
	
	worker = worker_status.keys()[0]
	status = worker_status.values()[0]

	status_text = colorama.Fore.GREEN + str(status) if status.get('ok') != -1 else colorama.Fore.RED + str(status)

	print worker, status_text