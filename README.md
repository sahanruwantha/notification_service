# Notification Service

A scalable notification system built with Django, gRPC, React, and Celery for handling different types of notifications (email, push, on-site) efficiently.

## Architecture Overview

```mermaid
graph TB
    subgraph "Frontend"
        React[React Application]
    end

    subgraph "API Gateway"
        Envoy[Envoy Proxy]
    end

    subgraph "Backend Services"
        API[gRPC API Service]
        Worker[Celery Workers]
        Cache[RabbitMQ]
        DB[(PostgreSQL)]
    end

    React -->|gRPC-Web| Envoy
    Envoy -->|gRPC| API
    API --> DB
    API -->|Tasks| Worker
    Worker --> Cache
    Worker -->|Read/Write| DB
```

## Features

- Multiple notification types support (Email, Push, On-site)
- Real-time notification delivery
- Asynchronous processing using Celery
- gRPC communication for efficient client-server interaction
- Scalable architecture with Docker containerization
- Background task processing for heavy operations

## Tech Stack

- **Frontend**: React with gRPC-web
- **Backend**: Django with django-socio-grpc
- **Database**: PostgreSQL
- **Cache & Message Broker**: RabbitMQ
- **API Gateway**: Envoy Proxy
- **Task Queue**: Celery
- **Containerization**: Docker & Docker Compose

## Project Structure

```
app       # main application
    grpc  # protocall buffer and grpc services
    migrations
    utils
notification_service # django app
notification-client  # react app
test                 # test scripts for the backend
```

## Prerequisites

- Docker and Docker Compose
- Node.js 16+ (for local development)
- Python 3.8+ (for local development)
- Make (optional, for using Makefile commands)

## Environment Variables

Create `.env` file in the root directory:

```env
# Django Settings
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=notifications
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

# RabbitMQ
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672

# Celery
CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
CELERY_RESULT_BACKEND=rpc://
```

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/notification-service.git
cd notification-service
```

2. Build and start the services:
```bash
docker-compose up --build
```

3. Run database migrations:
```bash
docker-compose exec backend python manage.py migrate
```

4. Create a superuser (optional):
```bash
docker-compose exec backend python manage.py createsuperuser
```

## Services

The application runs the following services:

- Frontend: `http://localhost:3000`
- Backend gRPC: `localhost:50051`
- Envoy Proxy: `localhost:8080`
- PostgreSQL: `localhost:5432`
- RabbitMQ: `localhost:5672`

## API Documentation

### Notification Types

```python
UNKNOWN = 0
EMAIL = 1
ON_SITE = 2
PUSH = 3
```

### gRPC Methods

1. **Create Notification**
   - Method: `Create`
   - Request: `SendNotificationRequest`
   - Response: `NotificationResponse`

2. **Get Unread Notifications**
   - Method: `GetUnreadNotifications`
   - Request: `GetUnreadNotificationsRequest`
   - Response: `NotificationListResponse`

3. **Mark Notifications as Read**
   - Method: `MarkNotificationsAsRead`
   - Request: `MarkNotificationsAsReadRequest`
   - Response: `Empty`

## Development

### Generating Protocol Buffers

```bash
# Generate Python code
python -m grpc_tools.protoc -I./protos --python_out=./backend/app/grpc \
    --grpc_python_out=./backend/app/grpc ./protos/app.proto

# Generate JavaScript code
protoc -I./protos app.proto \
    --js_out=import_style=commonjs:./frontend/src/generated \
    --grpc-web_out=import_style=commonjs,mode=grpcwebtext:./frontend/src/generated
```

## Monitoring & Debugging

- Django Admin: `http://localhost:8000/admin`
- Celery Flower: `http://localhost:5555`
- RabbitMQ Management: `http://localhost:15672` (default credentials: `guest`/`guest`)
