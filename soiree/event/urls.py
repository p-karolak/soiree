from django.urls import path

from . import views

app_name = "event"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create_event, name='create'),
    path('<int:event_id>/', views.event_detail, name='detail'),
    path('<int:event_id>/attend/', views.attend_event, name='attend'),
]
