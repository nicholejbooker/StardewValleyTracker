# StardewTracker Django Project

**[View on GitHub](https://github.com/nicholejbooker/StardewValleyTracker)**

A small Stardew Valley companion web app built with **Django**.  
The first feature is an **interactive in-game calendar** that shows **villager birthdays** and **seasonal events**, with a **bright, cheery theme** and optional **dark mode**.

---

## Prerequisites

- Python 3.10+ installed
- (Recommended) A virtual environment tool such as `venv`

---

## Setup (without Docker)

1. **Create and activate a virtual environment (recommended)**

   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   # Windows (cmd)
   .venv\Scripts\activate.bat
   # macOS/Linux
   source .venv/bin/activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create the Django database**

   ```bash
   python manage.py migrate
   ```

4. (Optional) **Create a superuser for the admin site**

   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. Open the site in your browser:

   - `http://127.0.0.1:8000/`

---

## Run with Docker

You can also run the app in a container if you have **Docker Desktop** installed.

### Build and run directly with Docker

From the project root:

```bash
docker build -t stardew-tracker .
docker run --rm -p 8000:8000 stardew-tracker
```

Then open:

- `http://127.0.0.1:8000/`

### Using docker-compose

Alternatively, use the provided `docker-compose.yml`:

```bash
docker compose up --build
```

and visit `http://127.0.0.1:8000/`.

---

## Project structure (planned)

This is the approximate structure we will use:

```text
StardewTracker/
  manage.py
  requirements.txt
  README.md
  stardewtracker/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
  calendar_app/
    __init__.py
    apps.py
    urls.py
    views.py
    data.py
    templates/
      calendar_app/
        calendar.html
    static/
      calendar_app/
        css/
          styles.css
        js/
          calendar.js
```

---

## Next steps

- Expand the calendar to track:
  - Festivals and events
  - Custom player reminders
  - Crop planning and other farming tasks
- Add user accounts and per-player save data.
