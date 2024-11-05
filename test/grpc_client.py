import grpc
import logging
from google.protobuf.empty_pb2 import Empty
import app_pb2
import app_pb2_grpc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NotificationClient:
    def __init__(self, host="localhost", port=50051):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = app_pb2_grpc.NotificationControllerStub(self.channel)
        logger.info(f"Client initialized - connecting to {host}:{port}")

    def close(self):
        self.channel.close()

    def send_notification(self, user_id, notification_type, payload):
        """
        Send a notification
        """
        try:
            request = app_pb2.NotificationRequest(
                user_id=user_id,
                type=notification_type,
                payload=payload,
            )
            response = self.stub.Create(request)
            logger.info(f"Notification sent successfully: {response}")
            return response
        except grpc.RpcError as e:
            logger.error(f"Failed to send notification: {e.details()}")
            raise

    def get_unread_notifications(self, user_id):
        """
        Get unread notifications for a specific user

        Args:
            user_id (str): The ID of the user to get notifications for
            
        Returns:
            app_pb2.NotificationListResponse: Contains list of notifications and total count
            
        Raises:
            grpc.RpcError: If the gRPC call fails
        """
        try:
            request = app_pb2.GetUnreadNotificationsRequest(
                user_id=user_id
            )
            response = self.stub.GetUnreadNotifications(request)
            logger.info(f"Retrieved {response.total_count} unread notifications for user {user_id}")
            return response
        except grpc.RpcError as e:
            logger.error(f"Failed to get unread notifications: {e.details()}")
            raise

def test_notification_service():
    """
    Test all notification service functionalities
    """
    client = NotificationClient()
    
    try:
        print("\n1. Testing SendNotification")
        notifications = [
            ("user1", 1, "Test email notification"),
            ("user1", 2, "Test on-site notification"),
            ("user2", 3, "Test push notification"),
        ]
        
        for user_id, n_type, payload in notifications:
            response = client.send_notification(user_id, n_type, payload)
            print(f"Sent notification: {response}")

    except Exception as e:
        print(f"Error during testing: {str(e)}")
    
    finally:
        client.close()

def test_notification_service_for_get():
    """
    Test getting unread notifications
    """
    client = NotificationClient()
    
    try:
        response = client.get_unread_notifications("sahan")
        print(f"Unread notifications response: {response}")
        print(f"Total unread notifications: {response.total_count}")
        print("\nNotifications:")
        for notification in response.notifications:
            print(f"- ID: {notification.id}")
            print(f"  User ID: {notification.user_id}")
            print(f"  Type: {notification.type}")
            print(f"  Payload: {notification.payload}")
            print(f"  Is Read: {notification.is_read}")
            print()

    except Exception as e:
        print(f"Error during testing: {str(e)}")
    
    finally:
        client.close()

if __name__ == "__main__":
    test_notification_service_for_get()