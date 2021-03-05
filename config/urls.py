from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('todoadmin/', admin.site.urls),
    path('', include('todolist.urls')),
]
