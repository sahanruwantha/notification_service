from celery import Celery
from app.utils.notification_utils import send_email, send_push_notification, save_on_site_notification, mark_onsite_notifications_as_read, get_unread_onsite_notifications
import logging

logger = logging.getLogger(__name__)
app = Celery('celery_app', broker='amqp://guest:guest@rabbitmq:5672//', backend='rpc://')

@app.task
def save_notification(user_id, payload):
    save_on_site_notification(user_id, payload)

@app.task
def get_unread_notifications_for_user(user_id):
    unread_notifications = get_unread_onsite_notifications(user_id)
    return unread_notifications

@app.task
def mark_notification_as_read(notification_ids):
    print('from celery', notification_ids)
    try:
        updated_count = mark_onsite_notifications_as_read(notification_ids)
        return updated_count
    except Exception as e:
        logger.error(f"Error in mark_notification_as_read task: {e}")
        raise

@app.task
def handle_email_notifications(content):
    send_email(content)

@app.task
def hadle_push_notifications(content):
    send_push_notification(content)
