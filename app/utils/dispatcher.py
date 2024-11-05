from celery_app import handle_push_notifications, handle_email_notifications, save_notification, mark_notification_as_read, get_unread_notifications_for_user
import logging

logger = logging.getLogger(__name__)

def dispatch_notifications(user_id, notification):
    try:
        notification_type = notification.type
        if notification_type == 1:
            handle_email_notifications.delay(notification.payload)
        elif notification_type == 2:
            handle_push_notifications.delay(notification.payload)
        elif notification_type == 3:
            save_notification.delay(user_id, notification.payload)
        else:
            logger.warning(f"Unknown notification type: {notification_type}")
    except Exception as e:
        logger.error(f"Error dispatching notifications for user {user_id}: {e}")

def get_unread_notifications(user_id):
    try:
        notification_task = get_unread_notifications_for_user.delay(user_id)
        notifications = notification_task.get()
        return notifications
    except Exception as e:
        logger.error(f"Error getting unread notifications for user {user_id}: {e}")
        return []