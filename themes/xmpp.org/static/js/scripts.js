document.addEventListener("DOMContentLoaded", () => {

  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

  if (window.location.pathname == "/software/") {
    for (const button of document.querySelectorAll('button[name="category-button"]')) {
      button.addEventListener("click", software_filter_list);
      if (button.id == "category-button-clients") {
        button.click();
      }
    }
    for (const check of document.getElementById("select-options-list").querySelectorAll('input[id^="xep-"')) {
      check.addEventListener("click", software_filter_list);
    }
    document.getElementById("compliance-core").addEventListener("change", software_filter_list);
    document.getElementById("compliance-im").addEventListener("change", software_filter_list);
    document.getElementById("compliance-mobile").addEventListener("change", software_filter_list);
    document.getElementById("compliance-web").addEventListener("change", software_filter_list);
    document.getElementById("compliance-av").addEventListener("change", software_filter_list);

    document.getElementById("platform-select").addEventListener("change", software_filter_list);
    document.getElementById("xep-select").addEventListener("click", software_show_xep_select_dropdown);
    document.getElementById("xep-select-dropdown-container").addEventListener("focusout", software_hide_xep_select_dropdown);
    document.getElementById("xep-search").addEventListener("keyup", software_search_xeps);
    document.getElementById("reset-xep-filter").addEventListener("click", software_reset_xep_filter);

    software_set_platform_by_user_agent();
  }

  if (window.location.pathname == "/software/software-comparison/") {
    for (const element of document.getElementById("comparison-dropdown").querySelectorAll("a")) {
      element.addEventListener("click", add_to_comparison);
    }
    for (const button of document.getElementsByName("remove-from-comparison")) {
      button.addEventListener("click", remove_from_comparison);
    }
  }

  if (window.location.pathname == "/extensions/") {
    const xep_search_input = document.getElementById("xep-search-input")

    document.addEventListener("keypress", function (event) {
      if ((event.code != "Slash" && event.code != "Find") || xep_search_input == document.activeElement) {
        return;
      }
      xep_search_input.focus();
      event.preventDefault();
    });

    // XEP checkboxes and search bar
    xep_search_input.addEventListener("input", filter_xeps)

    const checkboxes = document.querySelectorAll("#status-selector input");
    for (const checkbox of checkboxes) {
      checkbox.addEventListener("click", filter_xeps)
    }
    filter_xeps()

    // XEP implementations offcanvas
    for (const button of document.getElementsByName("show-xep-implementations")) {
      button.addEventListener("click", function() {
        window.location.hash = "xep-" + button.dataset.xep + "-implementations";
        show_xep_implementations();
      });
    }
    if(window.location.hash) {
      show_xep_implementations();
    }
  }

  software_resize_extensions_collapse();
});

// Page /extensions/
function filter_xeps() {
  const search_string = document.getElementById("xep-search-input").value.toLowerCase();
  const checkboxes = document.querySelectorAll("#status-selector input");

  if (search_string !== "") {
    // Ignore status checkboxes when searching
    for (const checkbox of checkboxes) {
      checkbox.disabled = true;
    }
    const rows = document.querySelectorAll("[class*=XEP-]")
    for (const row of rows) {
      const xep_number = row.id.slice(3)
      const xep_name = row.querySelector('td:nth-child(2)').innerHTML.toLowerCase();
      const xep_shortname = row.dataset.shortname
      let tags = ""
      const tag_array = row.querySelector('td:nth-child(6)').querySelectorAll("span")
      if (tag_array.length > 0) {
        for (const tag of tag_array) {
          tags += ` ${tag.innerHTML.toLocaleLowerCase()}`
        }
      }

      if (xep_number.includes(search_string) || xep_name.includes(search_string) || xep_shortname.includes(search_string) || tags.includes(search_string)) {
        row.hidden = false
      } else {
        row.hidden = true
      }
    }
    return
  }

  // Handle status checkboxes
  for (const checkbox of checkboxes) {
    checkbox.disabled = false;
    const xep_status = checkbox.getAttribute("name");
    const relevant_xeps = document.querySelectorAll(`.XEP-${xep_status}`);
    for (const row of relevant_xeps) {
      row.hidden = !checkbox.checked;
    }
  }
}

function show_xep_implementations() {
  let xep_number = window.location.hash.slice(5, 9);
  let row = document.getElementById("xep" + xep_number);
  let xep_title = row.cells[1].innerHTML;
  let xep_name = "XEP-" + xep_number + ": " + xep_title;
  document.getElementById("implementations-heading").innerHTML = xep_name;

  let all_rows = document.querySelectorAll('tr[name^="implementation-xep-"');
  for (const row of all_rows) {
    row.classList.add("d-none");
  }

  let xep_rows = document.getElementsByName("implementation-xep-" + xep_number);
  for (const row of xep_rows) {
    row.classList.remove("d-none");
  }

  var implementations_offcanvas = new bootstrap.Offcanvas(
    document.getElementById("implementations-offcanvas")
  );
  implementations_offcanvas.show();
}


// Page: /software/
function software_reset_xep_filter() {
  for (const check of document.getElementById("select-options-list").querySelectorAll("[data-xep]")) {
    check.checked = false;
  }
  document.getElementById("xep-search").value = "";
  software_search_xeps();
  software_filter_list();
}

function software_search_xeps() {
  let input = document.getElementById("xep-search");
  let filter = input.value.toLowerCase();
  for (const option of document.getElementById("select-options-list").children) {
    let title = option.dataset.title.toLowerCase();
    if (title.includes(filter)) {
      option.classList.remove("d-none");
    } else {
      option.classList.add("d-none");
    }
  }
}

function software_show_xep_select_dropdown() {
  let dropdown = document.getElementById("xep-select-dropdown-container");
  if (!dropdown.classList.contains("d-none")) {
    dropdown.classList.add("d-none");
  } else {
    dropdown.classList.remove("d-none");
    document.getElementById("xep-select-dropdown-container").focus();
  }
}
function software_hide_xep_select_dropdown(event) {
  if (!event.currentTarget.contains(event.relatedTarget)) {
    document.getElementById("xep-select-dropdown-container").classList.add("d-none");
  }
}

function get_user_platform() {
  if (navigator.userAgent.indexOf("Android") >= 0) {
    return "android";
  } else if (navigator.userAgent.indexOf("Linux") >= 0) {
    return "linux";
  } else if (navigator.userAgent.indexOf("iPhone") >= 0) {
    return "ios";
  } else if (navigator.userAgent.indexOf("Windows") >= 0) {
    return "windows";
  } else if (navigator.userAgent.indexOf("Macintosh") >= 0) {
    return "macos";
  } else {
    return "all-platforms";
  }
}

function software_set_platform_by_user_agent() {
  // Software list: Select platform reported by user agent
  let platform_select = document.getElementById("platform-select");
  if (platform_select) {
    let user_platform = get_user_platform();
    for (const option of platform_select) {
      if (option.value == user_platform) {
        option.setAttribute("selected", true);
        software_filter_list();
        return;
      }
    }
  }
}

function software_get_selected_category() {
  for (const button of document.querySelectorAll('button[name="category-button"]')) {
    if (button.classList.contains("active")) {
      return button.dataset.category;
    }
  }
}

function software_get_selected_xeps() {
  let xep_select = document.getElementById("xep-select");
  let select_options_list = document.getElementById("select-options-list");
  let selected_xeps = [];
  for (const check of select_options_list.querySelectorAll("[data-xep]")) {
    if(check.checked) {
      selected_xeps.push(check.dataset.xep);
    }
  }
  if (selected_xeps.length === 0) {
    xep_select.value = "Select XEPs...";
  } else if (selected_xeps.length === 1) {
    xep_select.value = "XEP-" + selected_xeps[0];
  } else {
    xep_select.value = "XEP-" + selected_xeps.slice(0, -1).join(", XEP-") + " and XEP-" + selected_xeps.at(-1);
  }

  return selected_xeps;
}

function software_is_package_compliant(card) {
  let package_core = card.dataset.cscore
  let package_im = card.dataset.csim
  let package_mobile = card.dataset.csmobile
  let package_web = card.dataset.csweb
  let package_av = card.dataset.csav

  switch (document.getElementById("compliance-core").value) {
    case "core":
      if (package_core == "-" ) { return false; }
      break;
    case "advanced":
      if (package_core != "advanced") { return false; }
  }

  switch (document.getElementById("compliance-im").value) {
    case "core":
      if (package_im == "-") { return false; }
      break;
    case "advanced":
      if (package_im != "advanced") { return false; }
  }

  switch (document.getElementById("compliance-mobile").value) {
    case "core":
      if (package_mobile == "-") { return false; }
      break;
    case "advanced":
      if (package_mobile != "advanced") { return false; }
  }
  switch (document.getElementById("compliance-web").value) {
    case "core":
      if (package_web == "-") { return false; }
      break;
    case "advanced":
      if (package_web != "advanced") { return false; }
  }
  switch (document.getElementById("compliance-av").value) {
    case "core":
      if (package_av == "-") { return false; }
      break;
    case "advanced":
      if (package_av != "advanced") { return false; }
  }

  return true;
}

function software_filter_list() {
  let category = software_get_selected_category();
  if (category == null) {
    return;
  }

  if (category == "libraries") {
    category = "library";
  } else {
    category = category.slice(0, -1);
  }

  let selected_xeps = software_get_selected_xeps();
  let platform = document.getElementById("platform-select").value;

  let hidden_cards = 0;
  for (const card of document.getElementsByClassName("package-card")) {
    let category_list = card.dataset.categories;
    let xep_list = card.dataset.xeps.split(',');
    let package_compliant = software_is_package_compliant(card);

    let show_card = false;
    card.classList.remove("d-none");

    if (category_list.toLowerCase().includes(category)) {
      if (card.dataset.platforms.toLowerCase().includes(platform) || platform == "all-platforms") {
        if (package_compliant) {
          if (selected_xeps.length === 0 || selected_xeps.every(r => xep_list.includes(r))) {
            show_card = true;
          } else {
            hidden_cards++;
          }
        } else {
          hidden_cards++;
        }
      } else {
        hidden_cards++;
      }
    }
    if (!show_card) {
      card.classList.add("d-none");
    }
  }
  let hidden_results_info = document.getElementsByName("hidden-results-info");
  for (const info_text of hidden_results_info){
    if (hidden_cards === 0) {
      info_text.innerHTML = "All software entries are shown.";
    } else {
      info_text.innerHTML = "Your filter settings omit " + hidden_cards + " entries.";
    }
  }
}

// Page: /software/software-comparison/
function add_to_comparison(event) {
  let name = event.srcElement.innerHTML;
  let col_index = 0;
  let cells = document.querySelectorAll("#comparison-table thead tr th");
  cells.forEach(function(cell) {
    if (cell.getAttribute("name") == name) {
      col_index = cell.cellIndex + 1;
    }
  })
  document.querySelectorAll("#comparison-table thead tr th:nth-child(" + col_index + ")").forEach(
    element => element.classList.remove("d-none")
  )
  document.querySelectorAll("#comparison-table tbody tr td:nth-child(" + col_index + ")").forEach(
    element => element.classList.remove("d-none")
  )
}

function remove_from_comparison(event) {
  let col_index = event.srcElement.closest("TH").cellIndex + 1;
  document.querySelectorAll("#comparison-table thead tr th:nth-child(" + col_index + ")").forEach(
    element => element.classList.add("d-none")
  )
  document.querySelectorAll("#comparison-table tbody tr td:nth-child(" + col_index + ")").forEach(
    element => element.classList.add("d-none")
  )
}

// Page: /software/<app>/
function software_resize_extensions_collapse() {
  // Resize DOAP iframe in software details view
  let extensions_collapse = document.getElementById("extensions-collapse");
  if (extensions_collapse) {
    extensions_collapse.addEventListener("shown.bs.collapse", function () {
      let frame = document.getElementById("doap-iframe");
      if (frame) {
        frame.style.height = frame.contentWindow.document.documentElement.scrollHeight + 20 + 'px';
      }
    });
  }
}
