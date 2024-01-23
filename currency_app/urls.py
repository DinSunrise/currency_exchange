from django.urls import path
from .views import GetCurrentUSDView

urlpatterns = [
    path("get-current-usd/", GetCurrentUSDView.as_view(), name="get_current_usd"),
]
