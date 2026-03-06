from collections import defaultdict
import re
from typing import Any, Dict, List

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .data import FESTIVALS, VILLAGER_BIRTHDAYS, Season


SEASONS: list[Season] = ["Spring", "Summer", "Fall", "Winter"]


def _normalize_season(raw: str | None) -> Season:
    if not raw:
        return "Spring"
    normalized = raw.capitalize()
    if normalized not in SEASONS:
        return "Spring"
    return normalized  # type: ignore[return-value]

def _slugify_asset_name(name: str) -> str:
    """
    Create a stable, filesystem-friendly slug for static asset filenames.
    Example: "Mr. Qi" -> "mr-qi"
    """
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "unknown"


def calendar_view(request: HttpRequest, season: str | None = None) -> HttpResponse:
    active_season: Season = _normalize_season(season)

    # Organize events per day (1–28) for the chosen season.
    events_by_day: Dict[int, List[Dict[str, Any]]] = defaultdict(list)

    for bday in VILLAGER_BIRTHDAYS:
        if bday.season == active_season:
            events_by_day[bday.day].append(
                {
                    "type": "birthday",
                    "label": f"{bday.villager}'s Birthday",
                    "villager": bday.villager,
                    "villager_slug": _slugify_asset_name(bday.villager),
                }
            )

    for festival in FESTIVALS:
        if festival.season == active_season:
            events_by_day[festival.day].append(
                {
                    "type": "festival",
                    "label": festival.name,
                    "note": festival.note,
                }
            )

    days = list(range(1, 29))
    calendar_days: List[Dict[str, Any]] = [
        {"day": day, "events": events_by_day.get(day, [])} for day in days
    ]

    context = {
        "season": active_season,
        "seasons": SEASONS,
        "calendar_days": calendar_days,
    }
    return render(request, "calendar_app/calendar.html", context)

