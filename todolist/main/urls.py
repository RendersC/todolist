from django.urls import path
from . import views
from .views import TodoListView, TodoUpdateView, TodoDeleteView, TodoCreateView


urlpatterns = [
    path("", TodoListView.as_view(),name='home'),
    path("about/", views.about,name='about'),
    path("create/", TodoCreateView.as_view(),name='todo_create'),
    path("edit/<int:pk>/", TodoUpdateView.as_view(),name='todo_edit'),
    path("delete/<int:pk>/", TodoDeleteView.as_view(),name='todo_delete'),
]