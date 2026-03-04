from django.urls import path

from . import views

app_name = "calendar_app"

urlpatterns = [
    path("", views.calendar_view, name="calendar"),
    path("<str:season>/", views.calendar_view, name="calendar_by_season"),
]

