/*
 * Securing AI Systems — module progress tracking.
 *
 * Local only: state lives in localStorage under "sas.progress.v1".
 * No network requests, no identifiers, no cookies.
 *
 * Two mount points:
 *   [data-sas-progress]  on a module page -> renders a completion toggle
 *   [data-sas-overview]  on the roadmap   -> renders per-part totals
 *
 * The module-to-level map below is the single place where structure is
 * duplicated outside mkdocs.yml. If a module is added, moved or renumbered,
 * update PARTS as well.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "sas.progress.v1";

  var PARTS = [
    { name: "Level 1 — Foundation", modules: ["01", "02", "03", "04", "05"] },
    { name: "Level 2 — Intermediate", modules: ["06", "07", "08", "09", "10"] },
    { name: "Level 3 — Advanced", modules: ["11", "12", "13", "14", "15"] },
    { name: "Level 4 — Professional Practice", modules: ["16", "17", "18", "19", "20"] }
  ];

  var memoryFallback = {};
  var storageAvailable = (function () {
    try {
      var probe = "__sas_probe__";
      window.localStorage.setItem(probe, "1");
      window.localStorage.removeItem(probe);
      return true;
    } catch (error) {
      return false;
    }
  })();

  function load() {
    if (!storageAvailable) {
      return memoryFallback;
    }
    try {
      var raw = window.localStorage.getItem(STORAGE_KEY);
      var parsed = raw ? JSON.parse(raw) : {};
      return parsed && typeof parsed === "object" ? parsed : {};
    } catch (error) {
      return {};
    }
  }

  function save(state) {
    memoryFallback = state;
    if (!storageAvailable) {
      return;
    }
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (error) {
      /* Quota or privacy mode: keep the in-memory value and carry on. */
    }
  }

  function moduleIdFromPath(pathname) {
    var match = pathname.match(/\/modules\/(\d{2})[-/]/);
    return match ? match[1] : null;
  }

  function partOf(moduleId) {
    for (var i = 0; i < PARTS.length; i += 1) {
      if (PARTS[i].modules.indexOf(moduleId) !== -1) {
        return PARTS[i];
      }
    }
    return null;
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) {
      node.className = className;
    }
    if (typeof text === "string") {
      node.textContent = text;
    }
    return node;
  }

  /* ---------------------------------------------------------------- module */

  function renderModuleControl(host, moduleId) {
    var state = load();
    var done = Boolean(state[moduleId]);
    var part = partOf(moduleId);

    host.classList.add("sas-progress");
    host.textContent = "";

    var status = el("span", "sas-progress__state");
    status.setAttribute("role", "status");
    status.setAttribute("aria-live", "polite");

    var button = el("button", "sas-progress__btn");
    button.type = "button";
    button.setAttribute("aria-pressed", done ? "true" : "false");
    button.textContent = "Mark this module complete";

    function paint(isDone, announce) {
      button.setAttribute("aria-pressed", isDone ? "true" : "false");
      status.textContent = isDone
        ? "Completed on this device."
        : "Not yet marked as complete.";
      status.classList.toggle("is-complete", isDone);
      if (announce) {
        status.textContent = isDone
          ? "Module marked complete."
          : "Module marked as not complete.";
      }
    }

    button.addEventListener("click", function () {
      var next = load();
      var isDone = !Boolean(next[moduleId]);
      if (isDone) {
        next[moduleId] = new Date().toISOString().slice(0, 10);
      } else {
        delete next[moduleId];
      }
      save(next);
      paint(isDone, true);
    });

    var label = el("span", "sas-progress__label");
    var context = part ? part.name : "Securing AI Systems";
    label.textContent = "Your progress · " + context;

    host.appendChild(label);
    host.appendChild(button);
    host.appendChild(status);

    paint(done, false);

    if (!storageAvailable) {
      var note = el(
        "span",
        "sas-progress__note",
        "This browser is blocking local storage, so progress will not persist."
      );
      host.appendChild(note);
    }
  }

  /* -------------------------------------------------------------- overview */

  function renderOverview(host) {
    var state = load();
    var total = 0;
    var completed = 0;

    host.classList.add("sas-overview");
    host.textContent = "";

    var heading = el("div", "sas-overview__heading", "Completion by level");
    host.appendChild(heading);

    PARTS.forEach(function (part) {
      var done = part.modules.filter(function (id) {
        return Boolean(state[id]);
      }).length;
      var count = part.modules.length;
      total += count;
      completed += done;

      var row = el("div", "sas-overview__row");

      var name = el("div", "sas-overview__name", part.name);
      var numbers = el("div", "sas-overview__numbers", done + " / " + count);

      var track = el("div", "sas-progressbar");
      var fill = el("div", "sas-progressbar__fill");
      var percent = count ? Math.round((done / count) * 100) : 0;
      fill.style.width = percent + "%";

      track.setAttribute("role", "progressbar");
      track.setAttribute("aria-valuemin", "0");
      track.setAttribute("aria-valuemax", String(count));
      track.setAttribute("aria-valuenow", String(done));
      track.setAttribute(
        "aria-valuetext",
        done + " of " + count + " modules complete, " + percent + " percent"
      );
      track.appendChild(fill);

      row.appendChild(name);
      row.appendChild(track);
      row.appendChild(numbers);
      host.appendChild(row);
    });

    var summary = el(
      "div",
      "sas-overview__summary",
      "Total: " + completed + " of " + total + " modules complete."
    );
    summary.setAttribute("role", "status");
    summary.setAttribute("aria-live", "polite");
    host.appendChild(summary);

    if (completed > 0) {
      var reset = el("button", "sas-progress__btn sas-progress__btn--ghost", "Reset progress");
      reset.type = "button";
      reset.addEventListener("click", function () {
        if (window.confirm("Clear completion marks for every module on this device?")) {
          save({});
          renderOverview(host);
        }
      });
      host.appendChild(reset);
    }
  }

  /* ------------------------------------------------------------------ boot */

  function boot() {
    var moduleHosts = document.querySelectorAll("[data-sas-progress]");
    var moduleId = moduleIdFromPath(window.location.pathname);

    if (moduleHosts.length && moduleId) {
      Array.prototype.forEach.call(moduleHosts, function (host) {
        renderModuleControl(host, moduleId);
      });
    }

    var overviewHosts = document.querySelectorAll("[data-sas-overview]");
    if (overviewHosts.length) {
      Array.prototype.forEach.call(overviewHosts, function (host) {
        renderOverview(host);
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
