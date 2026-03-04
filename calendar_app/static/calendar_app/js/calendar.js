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
  dayCards.forEach((card) => {
    card.addEventListener("click", () => {
      if (activeCard && activeCard !== card) {
        activeCard.classList.remove("calendar-day--active");
      }
      card.classList.toggle("calendar-day--active");
      activeCard = card.classList.contains("calendar-day--active") ? card : null;
    });
  });
});

