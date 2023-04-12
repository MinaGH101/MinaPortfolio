from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('message/', views.MessageView.as_view(), name='message'),
    path('edu-contact/', views.ButtomView.as_view(), name='buttom'),
    
]
