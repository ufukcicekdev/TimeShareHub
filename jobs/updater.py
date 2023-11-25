from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from jobs.tasks import delete_expired_files_s3


def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(delete_expired_files_s3, 'interval', minutes=1)
	scheduler.start()