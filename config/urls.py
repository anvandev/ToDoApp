from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('todoadmin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('todolist.urls')),
]
