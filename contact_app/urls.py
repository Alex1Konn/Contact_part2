from django.urls import path
from contact_app import views

urlpatterns = [
    path('person/', views.person_view, name="person"),
]