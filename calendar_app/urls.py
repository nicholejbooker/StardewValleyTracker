from django.urls import path

from . import views

app_name = "calendar_app"

urlpatterns = [
    path("", views.landing_view, name="landing"),
    path("calendar/", views.calendar_view, name="calendar"),
    path("calendar/<str:season>/", views.calendar_view, name="calendar_by_season"),
    path(
        "perfection/",
        views.coming_soon_view,
        {"page_title": "Perfection"},
        name="perfection",
    ),
    path(
        "relationships/",
        views.coming_soon_view,
        {"page_title": "Relationships"},
        name="relationships",
    ),
    path(
        "animals/",
        views.coming_soon_view,
        {"page_title": "Animals"},
        name="animals",
    ),
    path(
        "skills/",
        views.coming_soon_view,
        {"page_title": "Skills"},
        name="skills",
    ),
    path(
        "collections/",
        views.coming_soon_view,
        {"page_title": "Collections"},
        name="collections",
    ),
    path(
        "account/",
        views.coming_soon_view,
        {"page_title": "Account"},
        name="account",
    ),
]

