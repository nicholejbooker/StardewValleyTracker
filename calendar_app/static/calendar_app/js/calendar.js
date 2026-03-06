document.addEventListener("DOMContentLoaded", () => {
  const root = document.documentElement;
  const themeToggle = document.getElementById("theme-toggle");
  const dayCards = document.querySelectorAll(".calendar-day");

  const THEME_KEY = "stardewTheme";

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    if (themeToggle) {
      themeToggle.textContent = theme === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode";
    }
  }

  const storedTheme = window.localStorage.getItem(THEME_KEY);
  if (storedTheme === "dark" || storedTheme === "light") {
    applyTheme(storedTheme);
  } else {
    applyTheme("light");
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      const current = root.getAttribute("data-theme") === "dark" ? "dark" : "light";
      const next = current === "dark" ? "light" : "dark";
      window.localStorage.setItem(THEME_KEY, next);
      applyTheme(next);
    });
  }

  let activeCard = null;
  let dayPopover = null;

  function getOrCreatePopover() {
    if (!dayPopover) {
      dayPopover = document.createElement("div");
      dayPopover.className = "day-popover";
      dayPopover.innerHTML = `
        <h2 class="day-popover-heading"></h2>
        <div class="day-popover-body"></div>
      `;
      document.body.appendChild(dayPopover);
    }
    return dayPopover;
  }

  function hidePopover() {
    if (dayPopover) {
      dayPopover.classList.remove("day-popover--visible");
    }
  }

  function showDayPopover(card, clickEvent) {
    const pop = getOrCreatePopover();
    const headingEl = pop.querySelector(".day-popover-heading");
    const bodyEl = pop.querySelector(".day-popover-body");
    if (!headingEl || !bodyEl) return;

    const day = card.getAttribute("data-day") || "";
    const eventItems = card.querySelectorAll(".event-pill");

    headingEl.textContent = day ? `Day ${day}` : "Selected day";
    bodyEl.innerHTML = "";

    if (!eventItems.length) {
      const empty = document.createElement("p");
      empty.className = "day-popover-empty";
      empty.textContent = "No events for this day.";
      bodyEl.appendChild(empty);
    } else {
      const list = document.createElement("ul");
      list.className = "day-popover-list";

      eventItems.forEach((item) => {
        const labelEl = item.querySelector(".event-label");
        const noteEl = item.querySelector(".event-note");
        const li = document.createElement("li");
        li.className = "day-popover-item";

        const labelText = labelEl ? labelEl.textContent || "" : "";
        const noteText = noteEl ? noteEl.textContent || "" : "";

        const main = document.createElement("div");
        main.className = "day-popover-item-main";
        main.textContent = labelText;
        li.appendChild(main);

        if (noteText) {
          const note = document.createElement("div");
          note.className = "day-popover-item-note";
          note.textContent = noteText;
          li.appendChild(note);
        }

        list.appendChild(li);
      });

      bodyEl.appendChild(list);
    }

    // Position near the cursor, keeping within viewport bounds.
    const clickX = clickEvent.clientX;
    const clickY = clickEvent.clientY;

    pop.style.left = "0px";
    pop.style.top = "0px";
    pop.classList.add("day-popover--visible");

    const popRect = pop.getBoundingClientRect();
    const margin = 12;

    let left = clickX + margin;
    let top = clickY + margin;

    if (left + popRect.width > window.innerWidth - margin) {
      left = clickX - popRect.width - margin;
    }
    if (left < margin) {
      left = margin;
    }

    if (top + popRect.height > window.innerHeight - margin) {
      top = window.innerHeight - popRect.height - margin;
    }
    if (top < margin) {
      top = margin;
    }

    pop.style.left = `${left}px`;
    pop.style.top = `${top}px`;
    pop.classList.add("day-popover--visible");
  }

  dayCards.forEach((card) => {
    card.addEventListener("click", (event) => {
      if (activeCard && activeCard !== card) {
        activeCard.classList.remove("calendar-day--active");
      }
      card.classList.toggle("calendar-day--active");
      activeCard = card.classList.contains("calendar-day--active") ? card : null;

      if (card.classList.contains("calendar-day--active")) {
        showDayPopover(card, event);
      } else {
        hidePopover();
      }
    });
  });

  const spriteImages = document.querySelectorAll(".event-sprite");
  spriteImages.forEach((img) => {
    const el = img;
    el.addEventListener("error", () => {
      const placeholder = el.getAttribute("data-placeholder-src");
      if (!placeholder || el.dataset.fallbackApplied === "1") return;
      el.dataset.fallbackApplied = "1";
      el.src = placeholder;
    });
  });

  document.addEventListener("click", (event) => {
    if (!dayPopover) return;
    const target = event.target;
    if (
      target instanceof Element &&
      (target.closest(".calendar-day") || target.closest(".day-popover"))
    ) {
      return;
    }
    if (activeCard) {
      activeCard.classList.remove("calendar-day--active");
      activeCard = null;
    }
    hidePopover();
  });
});

