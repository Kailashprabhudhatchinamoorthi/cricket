from django.urls import path
from .views import cric_userView
urlpatterns = [
    path('user/',cric_userView),
]