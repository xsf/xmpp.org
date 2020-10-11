'use strict';

window.addEventListener("load", function() {
  const checkboxes = document.querySelectorAll("#status-selector > input");
  const show_hide = function(checkbox) {
    const xep_status = checkbox.getAttribute("name");
    const relevant_xeps = document.querySelectorAll(".XEP-" + xep_status);
    relevant_xeps.forEach(function(xep) {
      // TODO: add an animation maybe.
      xep.hidden = !checkbox.checked;
    });
    checkbox.addEventListener("click", function(event) {
      show_hide(event.target);
    });
  };
  checkboxes.forEach(show_hide);

  const jsSupport = document.querySelectorAll(".jsSupport");
  jsSupport.forEach(function(elem) {
    elem.classList.remove("jsSupport");
  });
});
