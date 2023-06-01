from . import views
from django.urls import path

urlpatterns = [
    path('tasks/<int:id>/redact', views.redact_task),
    path('tasks/<int:id>', views.index_with_id),
    path('tasks/search', views.SearchTasks.as_view(), name="search-view"),
    path('tasks/', views.view_lists),
    path('', views.rederect_to_list)
]