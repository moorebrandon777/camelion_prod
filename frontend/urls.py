from django.urls import path

from . import views

app_name = 'frontend'

urlpatterns = [
    path('capture_screenshot/', views.capture_screenshot, name='capture_screenshot'),
    path('my_bg', views.fetch_background_image, name='fetch_image'),
    path('detail', views.recieve_details, name="recieve_details"),
]