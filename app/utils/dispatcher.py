from celery_app import hadle_push_notifications, handle_email_notifications, save_notification, mark_notification_as_read, get_unread_notifications_for_user

def dispatch_notifications(user_id ,notfication):
    type = notfication.type
    if type == 1:
        handle_email_notifications.delay(notfication.payload)

    if type == 2:
        hadle_push_notifications.delay(notfication.payload)

    if type == 3:
        save_notification.delay(user_id, notfication.payload)
        print(notfication)

def get_unread_notifications(user_id):
    notification_task = get_unread_notifications_for_user.delay(user_id)
    notifications = notification_task.get()
    return notifications