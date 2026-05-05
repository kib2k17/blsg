(function () {
  var toggle = document.getElementById("nav-toggle");
  var panel = document.getElementById("mobile-nav");
  if (!toggle || !panel) return;

  function setOpen(open) {
    panel.hidden = !open;
    panel.classList.toggle("hidden", !open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }

  setOpen(false);

  toggle.addEventListener("click", function () {
    setOpen(panel.hidden);
  });

  panel.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      setOpen(false);
    });
  });
})();
