from django.urls import path
from . import views

urlpatterns = [
    path('auth/login/', views.login, name='login'),
    path('auth/register/', views.register, name='register'),
    path('auth/logout/', views.logout, name='logout'),
    path('upload/', views.upload_csv, name='upload'),
    path('summary/', views.get_summary, name='summary'),
    path('history/', views.get_history, name='history'),
    path('data/', views.get_latest_data, name='data'),
    path('download-report/', views.download_report, name='download_report'),
]
