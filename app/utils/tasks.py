from app.utils.celery_app import hadle_push_notifications, handle_email_notifications, save_notification, mark_notification_as_read, get_unread_notifications_for_user
import logging

logger = logging.getLogger(__name__)

def dispatch_notifications(user_id ,notfication):
    type = notfication.type
    if type == 1:
        handle_email_notifications.delay(notfication.payload)

    if type == 2:
        hadle_push_notifications.delay(notfication.payload)

    if type == 3:
        save_notification.delay(user_id, notfication.payload)

def get_unread_notifications_utils(user_id):
    notification_task = get_unread_notifications_for_user.delay(user_id)
    notifications = notification_task.get()
    return notifications

def mark_notifications_as_read_utils(notification_ids):
    print('from mark notifications as utils', notification_ids)
    """Initiate the celery task and return the result."""
    try:
        result = mark_notification_as_read.apply_async(args=[notification_ids])
        updated_count = result.get(timeout=10)
        return updated_count
    except Exception as e:
        logger.error(f"Error in mark_notifications_as_read_utils: {e}")
        raise


