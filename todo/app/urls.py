from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('update/<int:pk>', views.UpdateView.as_view(), name="update"),
    path('delete/<int:pk>',views.deleteTodo, name="delete"),
    path('about/', views.about, name="about")
]
