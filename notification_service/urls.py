from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from app.services import NotificationService
from django.contrib import admin
from django.urls import path


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("app", server)
    app_registry.register(NotificationService)


urlpatterns = [
    path('admin/', admin.site.urls),
]