from django.db import models


class Event(models.Model):
    """
    Placeholder model for future custom events/reminders.

    For now the calendar uses static in-game birthdays and festivals defined
    in calendar_app.data.
    """

    SEASON_CHOICES = [
        ("Spring", "Spring"),
        ("Summer", "Summer"),
        ("Fall", "Fall"),
        ("Winter", "Winter"),
    ]

    name = models.CharField(max_length=100)
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    day = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["season", "day", "name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.season} {self.day})"

