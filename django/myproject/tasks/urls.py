from . import views
from django.urls import path

urlpatterns = [
    path('<int:id>/<int:id2>', views.index_with_two_id),
    path('<int:id>/redact', views.redact_task),
    path('<int:id>', views.index_with_id),
    path('', views.index),
]