/* Securing AI Systems — quiz widget.
 * Progressive enhancement: the questions are plain HTML radio groups written by the
 * generator, so the page is readable and answerable with JavaScript disabled. This file
 * adds marking, explanations, a score and local persistence. Nothing leaves the browser.
 */
(function () {
  "use strict";

  var STORAGE_PREFIX = "sas-quiz:";

  function readKey(quiz) {
    var script = quiz.querySelector('script[type="application/json"]');
    if (!script) return null;
    try {
      return JSON.parse(script.textContent);
    } catch (error) {
      return null;
    }
  }

  function store(quizId, state) {
    try {
      window.localStorage.setItem(STORAGE_PREFIX + quizId, JSON.stringify(state));
    } catch (error) {
      /* private mode or storage disabled: marking still works, it just will not persist */
    }
  }

  function restore(quizId) {
    try {
      return JSON.parse(window.localStorage.getItem(STORAGE_PREFIX + quizId) || "{}");
    } catch (error) {
      return {};
    }
  }

  function letter(index) {
    return "ABCD".charAt(index);
  }

  function mark(quiz, fieldset, key, entry, checked) {
    var correct = key.a;
    var chosen = fieldset.querySelector('input[type="radio"]:checked');
    var feedback = fieldset.querySelector(".sas-q__fb");
    var state = fieldset.querySelector(".sas-q__state");
    var options = fieldset.querySelectorAll(".sas-opt");

    Array.prototype.forEach.call(options, function (option) {
      option.classList.remove("is-correct", "is-wrong", "is-answer");
    });

    if (!chosen && checked) {
      state.textContent = "Choose an option first.";
      return false;
    }

    options[correct].classList.add("is-answer");
    if (chosen) {
      var picked = Number(chosen.value);
      options[picked].classList.add(picked === correct ? "is-correct" : "is-wrong");
      state.textContent = picked === correct ? "Correct." : "Not quite — see the explanation.";
    } else {
      state.textContent = "Answer: " + letter(correct) + ".";
    }

    var list = ["<p class='sas-q__verdict'><strong>" + (chosen && Number(chosen.value) === correct ? "Correct" :
      "Answer: " + letter(correct)) + ".</strong> " + entry.e + "</p>", "<ul class='sas-q__why'>"];
    var wrongIndex = 0;
    for (var index = 0; index < 4; index += 1) {
      if (index === correct) continue;
      list.push("<li><strong>" + letter(index) + "</strong> — " + entry.w[wrongIndex] + "</li>");
      wrongIndex += 1;
    }
    list.push("</ul>");
    feedback.innerHTML = list.join("");
    feedback.hidden = false;
    fieldset.classList.add("is-marked");
    return { correct: Boolean(chosen) && Number(chosen.value) === correct, answered: Boolean(chosen) };
  }

  function collect(quiz) {
    var items = {};
    Array.prototype.forEach.call(quiz.querySelectorAll(".sas-q"), function (fieldset) {
      var chosen = fieldset.querySelector('input[type="radio"]:checked');
      if (chosen) items[fieldset.dataset.q] = Number(chosen.value);
    });
    return { items: items };
  }

  function updateScore(quiz) {
    var fieldsets = quiz.querySelectorAll(".sas-q");
    var total = fieldsets.length;
    var checked = 0;
    var correct = 0;
    Array.prototype.forEach.call(fieldsets, function (fieldset) {
      if (!fieldset.classList.contains("is-marked")) return;
      checked += 1;
      if (fieldset.dataset.result === "correct") correct += 1;
    });
    var score = quiz.querySelector("[data-sas-quiz-score]");
    if (score) {
      score.textContent = checked === 0
        ? "0 of " + total + " checked"
        : correct + " of " + checked + " correct · " + (total - checked) + " to go";
    }
    var bar = quiz.querySelector("[data-sas-quiz-bar]");
    if (bar) {
      var percent = total ? Math.round((checked / total) * 100) : 0;
      bar.style.width = percent + "%";
      bar.parentElement.setAttribute("aria-valuenow", String(percent));
    }
    if (checked === total) {
      var summary = quiz.querySelector("[data-sas-quiz-summary]");
      var pass = Number(quiz.dataset.pass || 70);
      var percentScore = Math.round((correct / total) * 100);
      if (summary) {
        summary.hidden = false;
        summary.innerHTML = "<strong>" + correct + " / " + total + " (" + percentScore + "%).</strong> " +
          (percentScore >= pass
            ? "Above the " + pass + "% practice threshold. Re-test in two days before trusting this."
            : "Below the " + pass + "% practice threshold. Reread the sections named by the items you missed.");
      }
      var state = collect(quiz);
      state.checked = checked;
      state.correct = correct;
      store(quiz.dataset.quiz, state);
    }
  }

  function init(quiz) {
    var key = readKey(quiz);
    if (!key) return;
    var saved = restore(quiz.dataset.quiz);

    Array.prototype.forEach.call(quiz.querySelectorAll(".sas-q"), function (fieldset) {
      var entry = key[fieldset.dataset.q];
      var button = fieldset.querySelector(".sas-q__check");
      if (!entry || !button) return;

      button.addEventListener("click", function () {
        var result = mark(quiz, fieldset, entry, entry, true);
        if (!result) return;
        fieldset.dataset.result = result.correct ? "correct" : "wrong";
        store(quiz.dataset.quiz, collect(quiz));
        updateScore(quiz);
      });

      Array.prototype.forEach.call(fieldset.querySelectorAll('input[type="radio"]'), function (input) {
        input.addEventListener("change", function () {
          fieldset.querySelector(".sas-q__state").textContent = "";
          if (fieldset.classList.contains("is-marked")) {
            fieldset.classList.remove("is-marked");
            fieldset.querySelector(".sas-q__fb").hidden = true;
          }
          store(quiz.dataset.quiz, collect(quiz));
        });
      });

      var stored = saved && saved.items ? saved.items[fieldset.dataset.q] : undefined;
      if (typeof stored === "number" && entry) {
        var inputs = fieldset.querySelectorAll('input[type="radio"]');
        if (inputs[stored]) {
          inputs[stored].checked = true;
          var restored = mark(quiz, fieldset, entry, entry, true);
          if (restored && restored.answered) {
            fieldset.dataset.result = restored.correct ? "correct" : "wrong";
          }
        }
      }
    });

    var all = quiz.querySelector("[data-sas-quiz-all]");
    if (all) {
      all.addEventListener("click", function () {
        Array.prototype.forEach.call(quiz.querySelectorAll(".sas-q"), function (fieldset) {
          var entry = key[fieldset.dataset.q];
          if (!entry) return;
          var result = mark(quiz, fieldset, entry, entry, true);
          if (!result || !result.answered) return;
          fieldset.dataset.result = result.correct ? "correct" : "wrong";
        });
        updateScore(quiz);
      });
    }

    var reset = quiz.querySelector("[data-sas-quiz-reset]");
    if (reset) {
      reset.addEventListener("click", function () {
        Array.prototype.forEach.call(quiz.querySelectorAll(".sas-q"), function (fieldset) {
          fieldset.classList.remove("is-marked");
          delete fieldset.dataset.result;
          var feedback = fieldset.querySelector(".sas-q__fb");
          if (feedback) {
            feedback.hidden = true;
            feedback.innerHTML = "";
          }
          fieldset.querySelector(".sas-q__state").textContent = "";
          Array.prototype.forEach.call(fieldset.querySelectorAll(".sas-opt"), function (option) {
            option.classList.remove("is-correct", "is-wrong", "is-answer");
          });
          Array.prototype.forEach.call(fieldset.querySelectorAll('input[type="radio"]'), function (input) {
            input.checked = false;
          });
        });
        var summary = quiz.querySelector("[data-sas-quiz-summary]");
        if (summary) summary.hidden = true;
        updateScore(quiz);
        store(quiz.dataset.quiz, { items: {} });
      });
    }

    updateScore(quiz);
  }

  function boot() {
    Array.prototype.forEach.call(document.querySelectorAll(".sas-quiz"), init);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
  /* Material's instant navigation swaps the document body without a reload. */
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(boot);
  }
})();
