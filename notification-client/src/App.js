import React, { useState, useCallback } from 'react';
import {
  NotificationRequest,
  GetUnreadNotificationsRequest,
  MarkNotificationsAsReadRequest,
} from './app_pb';
import { NotificationControllerClient } from './app_grpc_web_pb';

const client = new NotificationControllerClient('http://localhost:8080', null, {
  'Content-Type': 'application/grpc-web+proto',
  'x-grpc-web': '1',
});

const NOTIFICATION_TYPES = [
  { value: 1, label: 'Email' },     
  { value: 2, label: 'Push' },   
  { value: 3, label: 'On Site' }      
];

const NotificationApp = () => {
  const [unreadNotifications, setUnreadNotifications] = useState([]);
  const [selectedNotificationIds, setSelectedNotificationIds] = useState(new Set());
  
  const [formData, setFormData] = useState({
    userId: '',
    notificationType: '',
    payload: ''
  });

  const [status, setStatus] = useState({
    loading: false,
    success: false,
    error: null,
    operation: null
  });

  const handleInputChange = useCallback((field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }));
  }, []);

  const handleNotificationSelect = useCallback((notificationId) => {
    const numericId = Number(notificationId);
    if (isNaN(numericId)) {
      console.error('Invalid notification ID:', notificationId);
      return;
    }

    setSelectedNotificationIds(prev => {
      const newSet = new Set(prev);
      if (newSet.has(numericId)) {
        newSet.delete(numericId);
      } else {
        newSet.add(numericId);
      }
      return newSet;
    });
  }, []);

  const fetchUnreadNotifications = useCallback(async (userId) => {
    if (!userId) return;
    
    setStatus(prev => ({ ...prev, loading: true, operation: 'fetchUnread' }));

    try {
      const request = new GetUnreadNotificationsRequest();
      request.setUserId(userId);

      const response = await new Promise((resolve, reject) => {
        client.getUnreadNotifications(request, {}, (err, response) => {
          if (err) reject(err);
          else resolve(response);
        });
      });

      const notifications = response.getNotificationsList() || [];
      setUnreadNotifications(notifications);
      setSelectedNotificationIds(new Set()); 
      
      setStatus(prev => ({ 
        ...prev, 
        loading: false, 
        success: true, 
        error: null 
      }));
    } catch (error) {
      setStatus(prev => ({
        ...prev,
        loading: false,
        success: false,
        error: error.message || 'Failed to fetch unread notifications'
      }));
    }
  }, []);

  const handleMarkAsRead = useCallback(async () => {
    if (selectedNotificationIds.size === 0) return;

    setStatus(prev => ({ ...prev, loading: true, operation: 'markRead' }));

    try {
      const request = new MarkNotificationsAsReadRequest();
      request.setUserIdsList([...selectedNotificationIds].join(','));
      console.log([...selectedNotificationIds].join(','))
      
      client.markNotificationsAsRead(request, {}, () => {});

      setUnreadNotifications(prev => 
        prev.filter(notification => !selectedNotificationIds.has(notification.getId()))
      );
      
      setSelectedNotificationIds(new Set());

      setStatus(prev => ({
        ...prev,
        loading: false,
        success: true,
        error: null
      }));

      if (formData.userId) {
        await fetchUnreadNotifications(formData.userId);
      }
    } catch (error) {
      setStatus(prev => ({
        ...prev,
        loading: false,
        success: false,
        error: error.message || 'Failed to mark notifications as read'
      }));
    }
  }, [selectedNotificationIds, formData.userId, fetchUnreadNotifications]);

  const handleSubmit = useCallback(async (e) => {
    e.preventDefault();
    setStatus(prev => ({ ...prev, loading: true, operation: 'send' }));

    try {
      const request = new NotificationRequest();
      request.setUserId(formData.userId);
      request.setType(parseInt(formData.notificationType, 10));
      request.setPayload(formData.payload);
      
      await new Promise((resolve, reject) => {
        client.create(request, {}, (err, response) => {
          if (err) reject(err);
          else resolve(response);
        });
      });

      setStatus(prev => ({
        ...prev,
        loading: false,
        success: true,
        error: null
      }));

      setFormData(prev => ({
        ...prev,
        notificationType: '',
        payload: ''
      }));
      
      await fetchUnreadNotifications(formData.userId);
    } catch (error) {
      console.error('Error sending notification:', error);
      setStatus(prev => ({
        ...prev,
        loading: false,
        success: false,
        error: error.message || 'Failed to send notification'
      }));
    }
  }, [formData, fetchUnreadNotifications]);

  return (
    <div className="container">
      <div className="form-card">
        <div className="form-header">
          <h2>Send Notification</h2>
        </div>
        
        <form onSubmit={handleSubmit} className="form-content">
          <div className="form-group">
            <label>User ID</label>
            <input
              type="text"
              value={formData.userId}
              onChange={(e) => handleInputChange('userId', e.target.value)}
              placeholder="Enter user ID"
              required
              disabled={status.loading}
              className="form-input"
            />
          </div>
  
          <div className="form-group">
            <label>Notification Type</label>
            <select
              value={formData.notificationType}
              onChange={(e) => handleInputChange('notificationType', e.target.value)}
              required
              disabled={status.loading}
              className="form-select"
            >
              <option value="">Select notification type</option>
              {NOTIFICATION_TYPES.map((type) => (
                <option key={type.value} value={type.value}>
                  {type.label}
                </option>
              ))}
            </select>
          </div>
  
          <div className="form-group">
            <label>Message</label>
            <textarea
              value={formData.payload}
              onChange={(e) => handleInputChange('payload', e.target.value)}
              placeholder="Enter notification message"
              required
              disabled={status.loading}
              className="form-textarea"
            />
          </div>
  
          {status.error && status.operation === 'send' && (
            <div className="alert error">
              <strong>Error:</strong> {status.error}
            </div>
          )}
  
          {status.success && status.operation === 'send' && (
            <div className="alert success">
              <strong>Success:</strong> Notification sent successfully!
            </div>
          )}
  
          <button
            type="submit"
            disabled={status.loading}
            className="button primary"
          >
            {status.loading && status.operation === 'send' ? 'Sending...' : 'Send Notification'}
          </button>
        </form>
      </div>
  
      <div className="notifications-card">
        <div className="notifications-header">
          <h2>Unread Notifications</h2>
          <div className="notifications-actions">
            <button
              onClick={handleMarkAsRead}
              className="button primary"
              disabled={selectedNotificationIds.size === 0 || status.loading}
            >
              Mark Selected as Read
            </button>
            <button
              onClick={() => formData.userId && fetchUnreadNotifications(formData.userId)}
              className="button secondary"
              disabled={!formData.userId || status.loading}
            >
              Refresh Unread
            </button>
          </div>
        </div>
  
        {status.error && (status.operation === 'fetchUnread' || status.operation === 'markRead') && (
          <div className="alert error">
            <strong>Error:</strong> {status.error}
          </div>
        )}
  
        <div className="notifications-list">
          {unreadNotifications.map((notification) => {
            const notificationId = notification.getId();
            return (
              <div key={notificationId} className="notification-item">
                <div className="notification-checkbox">
                  <input
                    type="checkbox"
                    checked={selectedNotificationIds.has(notificationId)}
                    onChange={() => handleNotificationSelect(notificationId)}
                    className="checkbox"
                  />
                </div>
                <div className="notification-content">
                  <span className="notification-type">
                    On site Notification
                  </span>
                  <p className="notification-payload">{notification.getPayload()}</p>
                </div>
              </div>
            );
          })}
          {unreadNotifications.length === 0 && (
            <p className="no-notifications">No unread notifications</p>
          )}
        </div>
      </div>
  
      <style jsx>{`
        .container {
          max-width: 1200px;
          margin: 0 auto;
          padding: 2rem;
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 2rem;
          font-family: 'Arial', sans-serif;
          color: #374151;
        }
  
        .form-card,
        .notifications-card {
          background: #f3f4f6;
          border-radius: 16px;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
          padding: 2rem;
          transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .form-header, .notifications-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 1.5rem;
          color: #1f2937;
        }
  
        .form-group {
          margin-bottom: 1.5rem;
        }
  
        .form-group label {
          display: block;
          margin-bottom: 0.5rem;
          font-weight: 600;
          color: #6b7280;
        }
  
        .form-input, .form-select, .form-textarea {
          width: 100%;
          padding: 0.75rem;
          border: 1px solid #d1d5db;
          border-radius: 12px;
          font-size: 1rem;
          color: #374151;
          background-color: #ffffff;
          transition: border-color 0.2s, background-color 0.2s;
        }
  
        .form-input:focus, .form-select:focus, .form-textarea:focus {
          border-color: #2563eb;
          background-color: #f3f4f6;
          outline: none;
        }
  
        .button {
          padding: 0.75rem 1.5rem;
          border-radius: 8px;
          font-weight: 600;
          cursor: pointer;
          transition: background-color 0.3s, transform 0.2s;
        }
  
        .button:disabled {
          opacity: 0.6;
          cursor: not-allowed;
        }
  
        .button.primary {
          background-color: #2563eb;
          color: white;
        }
  
        .button.primary:hover:not(:disabled) {
          background-color: #1e40af;
          transform: translateY(-2px);
        }
  
        .button.secondary {
          background-color: #e5e7eb;
          color: #374151;
        }
  
        .button.secondary:hover:not(:disabled) {
          background-color: #d1d5db;
          transform: translateY(-2px);
        }
  
        .notifications-actions {
          display: flex;
          gap: 1rem;
        }
  
        .notification-item {
          display: flex;
          align-items: flex-start;
          gap: 1rem;
          background: #ffffff;
          border: 1px solid #e5e7eb;
          border-radius: 12px;
          padding: 1rem;
          margin-bottom: 0.5rem;
          transition: background-color 0.2s, transform 0.2s;
        }
  
        .notification-item:hover {
          background-color: #f9fafb;
          transform: translateY(-2px);
        }
  
        .checkbox {
          width: 1.25rem;
          height: 1.25rem;
          cursor: pointer;
        }
  
        .notification-content {
          flex: 1;
          display: flex;
          flex-direction: column;
          gap: 0.5rem;
        }
  
        .notification-type {
          font-weight: bold;
          color: #2563eb;
        }
  
        .notification-payload {
          margin: 0;
          color: #374151;
        }
  
        .alert {
          padding: 1rem;
          border-radius: 8px;
          margin-bottom: 1rem;
          font-weight: 500;
        }
  
        .alert.error {
          background-color: #fee2e2;
          border: 1px solid #ef4444;
          color: #991b1b;
        }
  
        .alert.success {
          background-color: #dcfce7;
          border: 1px solid #22c55e;
          color: #166534;
        }
  
        .no-notifications {
          text-align: center;
          color: #6b7280;
          padding: 2rem;
        }
  
        /* Responsive Styles */
        @media (max-width: 768px) {
          .container {
            grid-template-columns: 1fr;
            gap: 1rem;
            padding: 1rem;
          }
  
          .form-card, .notifications-card {
            padding: 1.5rem;
          }
  
          .notifications-actions {
            flex-direction: column;
            gap: 0.5rem;
          }
        }
      `}</style>
    </div>
  )}
  
  export default NotificationApp;