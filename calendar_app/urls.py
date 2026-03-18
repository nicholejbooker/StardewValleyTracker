from django.urls import path

from . import views

app_name = "calendar_app"

urlpatterns = [
    path("", views.landing_view, name="landing"),
    path("calendar/", views.calendar_view, name="calendar"),
    path("calendar/<str:season>/", views.calendar_view, name="calendar_by_season"),
]

