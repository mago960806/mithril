from django.urls import path

from dashborad.views import index

urlpatterns = [
    path("", index, name="index"),
]
