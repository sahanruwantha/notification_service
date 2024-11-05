import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def send_email(content, recipient_email="sahanr.silva@proton.me"):
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    
    subject = "Notification"
    body = content

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com"
    port = 587

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  
        server.login(sender_email, sender_password)
        text = message.as_string()
        
        server.sendmail(sender_email, recipient_email, text)  
        print(f"OTP sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

def send_push_notification(content):
    return None
    #         notification.notify(
    #     title='Notification',
    #     message=content,
    #     app_name='Notification Service', 
    #     timeout=10 
    # )
            
def get_db_connection():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def save_on_site_notification(user_id, payload):
    print('from save on site notification')
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS onsite_notifications (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL,
        payload TEXT NOT NULL,
        status INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                
                cursor.execute(create_table_query)

                
                insert_query = """
                INSERT INTO onsite_notifications (user_id, payload, status)
                VALUES (%s, %s, %s)
                RETURNING id;
                """
                
                
                cursor.execute(insert_query, (user_id, payload, 1))
                notification_id = cursor.fetchone()[0]
                conn.commit()
                print('Notification saved with ID:', notification_id)
                return notification_id
        except Exception as e:
            print(f"Error saving notification: {e}")
            conn.rollback()  
        finally:
            conn.close()  
    else:
        print("Failed to connect to the database.")
    
    return None


def get_unread_onsite_notifications(user_id):
    """Retrieve all unread notifications for a specific user."""
    query = """
    SELECT id, user_id, payload, status
    FROM onsite_notifications
    WHERE user_id = %s AND status = 1;
    """
    
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (user_id,))
                unread_notifications = cursor.fetchall()
                
                if not unread_notifications:
                    print(f"No unread notifications found for user: {user_id}")
                return unread_notifications
        except Exception as e:
            print(f"Error retrieving unread notifications: {e}")
            return [] 
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")
    return []


def mark_onsite_notifications_as_read(notification_ids):
    print('from postgres database', notification_ids)
    """Mark a list of specific notifications as read and return the number of updated rows."""
    query = """
    UPDATE onsite_notifications
    SET status = '0'
    WHERE id = ANY(%s)
    RETURNING id;
    """
    
    conn = get_db_connection()
    updated_count = 0
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (notification_ids,))
                updated_rows = cursor.fetchall()
                updated_count = len(updated_rows)
                conn.commit()
                return updated_count
        except Exception as e:
            print(f"Error marking notifications as read: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()
    return updated_count