from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Season = Literal["Spring", "Summer", "Fall", "Winter"]


@dataclass(frozen=True)
class Birthday:
    villager: str
    season: Season
    day: int


VILLAGER_BIRTHDAYS: list[Birthday] = [
    # Spring
    Birthday("Kent", "Spring", 4),
    Birthday("Lewis", "Spring", 7),
    Birthday("Vincent", "Spring", 10),
    Birthday("Haley", "Spring", 14),
    Birthday("Pam", "Spring", 18),
    Birthday("Shane", "Spring", 20),
    Birthday("Pierre", "Spring", 26),
    Birthday("Emily", "Spring", 27),
    # Summer
    Birthday("Jas", "Summer", 4),
    Birthday("Gus", "Summer", 8),
    Birthday("Maru", "Summer", 10),
    Birthday("Alex", "Summer", 13),
    Birthday("Sam", "Summer", 17),
    Birthday("Demetrius", "Summer", 19),
    Birthday("Dwarf", "Summer", 22),
    Birthday("Willy", "Summer", 24),
    Birthday("Leo", "Summer", 26),
    # Fall
    Birthday("Penny", "Fall", 2),
    Birthday("Elliott", "Fall", 5),
    Birthday("Jodi", "Fall", 11),
    Birthday("Abigail", "Fall", 13),
    Birthday("Sandy", "Fall", 15),
    Birthday("Marnie", "Fall", 18),
    # Winter
    Birthday("Krobus", "Winter", 1),
    Birthday("Linus", "Winter", 3),
    Birthday("Caroline", "Winter", 7),
    Birthday("Sebastian", "Winter", 10),
    Birthday("Harvey", "Winter", 14),
    Birthday("Wizard", "Winter", 17),
    Birthday("Evelyn", "Winter", 20),
    Birthday("Leah", "Winter", 23),
    Birthday("Clint", "Winter", 26),
]


@dataclass(frozen=True)
class Festival:
    name: str
    season: Season
    day: int
    note: str | None = None


FESTIVALS: list[Festival] = [
    # Spring
    Festival("Egg Festival", "Spring", 13),
    Festival("Flower Dance", "Spring", 24),
    # Summer
    Festival("Luau", "Summer", 11),
    Festival("Dance of the Moonlight Jellies", "Summer", 28),
    # Fall
    Festival("Stardew Valley Fair", "Fall", 16),
    Festival("Spirit's Eve", "Fall", 27),
    # Winter
    Festival("Festival of Ice", "Winter", 8),
    Festival("Night Market", "Winter", 15, note="Also 16–17 in-game"),
    Festival("Feast of the Winter Star", "Winter", 25),
]

