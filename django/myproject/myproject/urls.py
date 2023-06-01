from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('', include('tasks.urls')), 
    path('', include('django.contrib.auth.urls'))
]
