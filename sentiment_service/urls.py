from django.urls import path
from . import views

urlpatterns = [
    path('mails/', views.MailList.as_view()),
    path('mails/<int:pk>/', views.MailDetail.as_view()),
]