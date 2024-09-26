from django.urls import path
from .views import Cric_userView,Cric_userMangaeView
urlpatterns = [
    path('cricuser/',Cric_userView.as_view(),name="cricuser"),
    path('cricusermanage/<int:id>/',Cric_userMangaeView.as_view(),name="cricusermanage")
]