/* ==========================================================================
   Mermaid diagrams for the Securing AI Systems course
   --------------------------------------------------------------------------
   Material's built-in Mermaid integration fetches mermaid from unpkg.com at
   runtime. On a machine without internet access the fetch fails, the diagram
   container is left empty, and every figure becomes a blank box — which is
   exactly what the rendered site did before this file existed.

   This module loads a locally vendored copy instead (assets/javascript/
   vendor/mermaid.min.js, mermaid 11), renders the `sas-mermaid` fences itself,
   and re-renders them when the colour scheme changes so the diagrams stay
   legible in both themes. It is only fetched on pages that contain a diagram.

   The fences use `class: sas-mermaid` (see mkdocs.yml) so Material's own
   integration does not claim them.
   ========================================================================== */

(function () {
  "use strict";

  var SOURCE_SELECTOR = "pre.sas-mermaid";
  var FIGURE_SELECTOR = "figure.sas-diagram";
  var loader = null;
  var sequence = 0;

  var FONT = '"Inter", "Segoe UI", system-ui, -apple-system, sans-serif';

  function scriptUrl() {
    if (document.currentScript && document.currentScript.src) {
      return document.currentScript.src;
    }
    var scripts = document.querySelectorAll('script[src$="diagrams.js"]');
    return scripts.length ? scripts[scripts.length - 1].src : window.location.href;
  }

  function loadMermaid() {
    if (window.mermaid) return Promise.resolve(window.mermaid);
    if (loader) return loader;
    loader = new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = new URL("vendor/mermaid.min.js", scriptUrl()).href;
      script.onload = function () {
        resolve(window.mermaid || null);
      };
      script.onerror = reject;
      document.head.appendChild(script);
    });
    return loader;
  }

  function isDark() {
    return document.body.getAttribute("data-md-color-scheme") !== "default";
  }

  function themeVariables(dark) {
    if (dark) {
      return {
        background: "#0b1a2f",
        mainBkg: "#10243c",
        primaryColor: "#10243c",
        primaryTextColor: "#e6edf6",
        primaryBorderColor: "#22d3ee",
        secondaryColor: "#122a47",
        tertiaryColor: "#0b1a2f",
        lineColor: "#8aa3bd",
        textColor: "#e6edf6",
        nodeBorder: "#22d3ee",
        clusterBkg: "#0b1a2f",
        clusterBorder: "#1b3a5e",
        edgeLabelBackground: "#0b1a2f",
        titleColor: "#e6edf6",
        fontFamily: FONT
      };
    }
    return {
      background: "#ffffff",
      mainBkg: "#e8f1fb",
      primaryColor: "#e8f1fb",
      primaryTextColor: "#0b1a2f",
      primaryBorderColor: "#0e7490",
      secondaryColor: "#eef3f9",
      tertiaryColor: "#f7f9fc",
      lineColor: "#40566f",
      textColor: "#0b1a2f",
      nodeBorder: "#0e7490",
      clusterBkg: "#f7f9fc",
      clusterBorder: "#c8d5e3",
      edgeLabelBackground: "#ffffff",
      titleColor: "#0b1a2f",
      fontFamily: FONT
    };
  }

  function configure(mermaid) {
    mermaid.initialize({
      startOnLoad: false,
      securityLevel: "strict",
      theme: "base",
      fontFamily: FONT,
      themeVariables: themeVariables(isDark()),
      flowchart: { htmlLabels: true, curve: "basis", padding: 12 },
      sequence: { actorFontSize: 14, messageFontSize: 14, noteFontSize: 14 }
    });
  }

  function buildFigure(svg, source) {
    var figure = document.createElement("figure");
    figure.className = "sas-diagram";
    figure.setAttribute("role", "img");
    figure.dataset.source = source;
    figure.innerHTML = svg;
    return figure;
  }

  function renderNode(mermaid, node) {
    var source = node.dataset.source || node.textContent || "";
    if (!source.trim()) return;
    var id = "sas-mermaid-" + (sequence += 1);
    mermaid
      .render(id, source)
      .then(function (result) {
        var figure = buildFigure(result.svg, source);
        node.replaceWith(figure);
        if (typeof result.bindFunctions === "function") {
          result.bindFunctions(figure);
        }
      })
      .catch(function () {
        // Leave the marked-up source visible: a readable code block is better
        // than an empty rectangle, and the page already has a text description
        // of every diagram in a <details> block.
        node.classList.add("sas-mermaid--failed");
      });
  }

  function renderPending(mermaid) {
    var nodes = document.querySelectorAll(SOURCE_SELECTOR);
    for (var i = 0; i < nodes.length; i += 1) renderNode(mermaid, nodes[i]);
  }

  function retheme(mermaid) {
    configure(mermaid);
    var figures = document.querySelectorAll(FIGURE_SELECTOR);
    for (var i = 0; i < figures.length; i += 1) {
      var figure = figures[i];
      if (!figure.dataset.source) continue;
      renderNode(mermaid, {
        dataset: { source: figure.dataset.source },
        textContent: "",
        classList: { add: function () {} },
        replaceWith: figure.replaceWith.bind(figure)
      });
    }
  }

  function start() {
    var pending = document.querySelectorAll(SOURCE_SELECTOR).length;
    if (!pending && !document.querySelector(FIGURE_SELECTOR)) return;

    loadMermaid()
      .then(function (mermaid) {
        if (!mermaid) return;
        configure(mermaid);
        renderPending(mermaid);

        // Instant navigation swaps the article without a page load.
        var host = document.querySelector(".md-content") || document.body;
        var timer = null;
        new MutationObserver(function () {
          if (!document.querySelector(SOURCE_SELECTOR)) return;
          window.clearTimeout(timer);
          timer = window.setTimeout(function () {
            renderPending(mermaid);
          }, 80);
        }).observe(host, { childList: true, subtree: true });

        // Palette toggle: diagrams must follow the scheme.
        new MutationObserver(function () {
          retheme(mermaid);
        }).observe(document.body, {
          attributes: true,
          attributeFilter: ["data-md-color-scheme"]
        });
      })
      .catch(function () {
        /* offline with no vendored copy: sources stay visible */
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
