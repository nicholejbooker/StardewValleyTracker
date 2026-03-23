# StardewTracker

A **Django** web app—**Star-Done Valley**—a companion for *Stardew Valley*. The UI uses a shared layout, optional **dark mode**, and local **SVThin / SVBold** pixel fonts for body text and headings.

---

## Overview

### Landing page (`/`)
- Welcome message aimed at a broad companion experience (not tied to a single feature).

### Calendar (`/calendar/`, `/calendar/<season>/`)
- Seasonal **calendar** (Spring–Winter) with **villager birthdays** and **festivals** (data in `calendar_app/data.py`).
- Villager **sprites** under `calendar_app/static/calendar_app/img/villagers/`.
- Day cells open a popover with details (`calendar_app/static/calendar_app/js/calendar.js`).

### Site-wide navigation
- Left sidebar on all pages: **Home**, **Calendar**, **Perfection**, **Relationships**, **Animals**, **Skills**, **Collections**, **Account** (Account is at the bottom of the nav; **Collections** and **Account** sit in the lower block with spacing so Account stays last).
- Routes for **Perfection**, **Relationships**, **Animals**, **Skills**, **Collections**, and **Account** use a shared placeholder page (`coming_soon_view` + `coming_soon.html`); each can be swapped for dedicated views and templates later.

### Theming & fonts
- **Dark / light** theme in `localStorage` (`stardewTheme`); theme is applied early so full-page navigations (e.g. changing seasons) avoid a light flash in dark mode.
- Fonts: `calendar_app/static/calendar_app/fonts/svthin.otf.woff2` and `svbold.otf.woff2`, declared in `styles.css` (thin for most UI, bold for headings).

### Stack
- **Django** (`requirements.txt`), **SQLite** (`db.sqlite3`, gitignored).
- Static assets under `calendar_app/static/` for development.

---

## Prerequisites

- Python **3.10+** (recommended: `venv`)
- **Docker Desktop** (optional, for containerized run)

---

## Setup (local, without Docker)

1. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   # macOS/Linux
   source .venv/bin/activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Migrate**

   ```bash
   python manage.py migrate
   ```

4. **Run the dev server**

   ```bash
   python manage.py runserver
   ```

5. Open **http://127.0.0.1:8000/**

---

## Run with Docker

From the project root (Docker Desktop running):

```bash
docker compose up --build
```

Open **http://127.0.0.1:8000/** — stop with `docker compose down`.

---

## Project structure

```text
StardewTracker/
  manage.py
  requirements.txt
  README.md
  Dockerfile
  docker-compose.yml
  stardewtracker/          # project settings, root urls
  calendar_app/
    urls.py                # landing, calendar, placeholder routes
    views.py
    data.py                # birthdays, festivals, seasons
    templates/calendar_app/
      base.html            # layout, nav, theme toggle
      landing.html
      calendar.html
      coming_soon.html     # placeholder sections
    static/calendar_app/
      css/styles.css
      js/calendar.js
      fonts/               # svthin.otf.woff2, svbold.otf.woff2
      img/villagers/       # sprite PNGs + placeholder SVG
```

---

## Extensions

- Replace placeholder routes with full pages for **Perfection**, **Relationships**, **Animals**, **Skills**, **Collections**, and **Account**.

---

## Admin (optional)

```bash
python manage.py createsuperuser
```

Visit `/admin/` (enabled in `stardewtracker/urls.py`).
