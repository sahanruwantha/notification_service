from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from app.services import NotificationService

def grpc_handlers(server):
    app_registry = AppHandlerRegistry("app", server)
    app_registry.register(NotificationService)
