document.addEventListener("DOMContentLoaded", () => {
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

    document.getElementById("platform-select").addEventListener("change", software_platform_changed);
    document.getElementById("xep-select").addEventListener("click", software_show_xep_select_dropdown);
    document.getElementById("xep-select-dropdown-container").addEventListener("focusout", software_hide_xep_select_dropdown);
    document.getElementById("xep-search").addEventListener("keyup", software_search_xeps);
    document.getElementById("reset-xep-filter").addEventListener("click", software_reset_xep_filter);

    software_set_filters();
    software_filter_list();
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

  initialize_bootstrap_tooltips()

  software_resize_extensions_collapse();
});

function initialize_bootstrap_tooltips() {
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
}

// Page /extensions/
function filter_xeps() {
  const xeplist = document.getElementById("xeplist");
  const search_string = document.getElementById("xep-search-input").value.toLowerCase();
  const checkboxes = document.querySelectorAll("#status-selector input");
  const xepFilterResultsCountElement = document.getElementById("xep-filter-results-count");
  const dormantWarning = document.getElementById("dormant_xeps_filter_warning")

  if (search_string !== "") {
    // Ignore status checkboxes when searching
    for (const checkbox of checkboxes) {
      checkbox.disabled = true;
    }
    dormantWarning.classList.add("d-none")

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

    const hiddenXepsCount = xeplist.querySelectorAll('tr[hidden]').length;
    const shownXeps = xeplist.querySelectorAll('tr:not([hidden])').length - 1;

    xepFilterResultsCountElement.innerText = `Showing ${shownXeps} of ${shownXeps + hiddenXepsCount} XEPs`
    return
  }

  // Handle status checkboxes
  let activeFilterCount = 0

  for (const checkbox of checkboxes) {
    checkbox.disabled = false;
    const xep_status = checkbox.getAttribute("name");
    const relevant_xeps = document.querySelectorAll(`.XEP-${xep_status}`);
    for (const row of relevant_xeps) {
      row.hidden = !checkbox.checked;
    }

    if (checkbox.checked) {
      activeFilterCount += 1
    }
  }

  const hiddenXepsCount = xeplist.querySelectorAll('tr[hidden]').length;
  const shownXeps = xeplist.querySelectorAll('tr:not([hidden])').length - 1;

  xepFilterResultsCountElement.innerText = `Showing ${shownXeps} of ${shownXeps + hiddenXepsCount} XEPs `

  if (activeFilterCount > 0) {
    const filterSpan = document.createElement("a")
    filterSpan.href = "#"
    filterSpan.dataset.bsToggle = "collapse"
    filterSpan.dataset.bsTarget = "#filter_collapse"

    if (activeFilterCount === 1) {
      filterSpan.innerText = "(1 filter active)"
      xepFilterResultsCountElement.append(filterSpan)
    } else if (activeFilterCount > 1) {
      filterSpan.innerText = `(${activeFilterCount} filters active)`
      xepFilterResultsCountElement.append(filterSpan)
    }
  }

  if (document.getElementById("Dormant").checked) {
    dormantWarning.classList.add("d-none")
  } else {
    dormantWarning.classList.remove("d-none")
  }
}

function show_xep_implementations() {
  let xep_number = window.location.hash.slice(5, 9);

  const tableBody = document.getElementById("implementations-table-body")
  tableBody.innerHTML = ""
  for (const item of xepListData) {
    const paddedXEPNum = item.number.toString().padStart(4, '0')
    if (paddedXEPNum === xep_number) {
      const heading = document.getElementById("implementations-heading")
      heading.innerText = `XEP-${paddedXEPNum}: ${item.title}`;
      heading.href = `/extensions/xep-${paddedXEPNum}.html`;
      document.getElementById("implementations-description").innerText = `Last XEP revision: Version ${item.last_revision_version} (${item.last_revision_date})`

      for (const implementation of item.implementations) {
        const implementationRow = document.createElement("tr")
        const nameCell = document.createElement("td")
        const nameContainer = document.createElement("div")
        nameContainer.classList.add("d-flex", "align-items-center")
        implementationRow.append(nameContainer)

        if (implementation.package_logo) {
          const logo = document.createElement("img")
          logo.src = implementation.package_logo
          logo.style.width = "1rem"
          logo.classList.add("ms-2")
          nameContainer.append(logo)
        }

        const nameLink = document.createElement("a")
        nameLink.innerText = implementation.package_name
        nameLink.href = `/software/${implementation.package_name_slug}/`
        nameCell.append(nameLink)
        nameContainer.append(nameCell)

        const stateCell = document.createElement("td")
        if (implementation.implementation_status) {
          // Complete (default)
          let iconClasses = ["fa-solid", "fa-check"]
          let badgeClass = "text-bg-success"

          if (implementation.implementation_status === "planned") {
            iconClasses = ["fa-solid", "fa-plus"]
            badgeClass = "text-bg-primary"
          }
          if (implementation.implementation_status === "removed" || implementation.implementation_status === "wontfix" || implementation.implementation_status === "deprecated") {
            iconClasses = ["fa-regular", "fa-circle-xmark"]
            badgeClass = "text-bg-secondary"
          }
          if (implementation.implementation_status === "partial") {
            badgeClass = "text-bg-warning"
          }
          const stateSpan = document.createElement("span")
          stateSpan.classList.add("badge", "opacity-50", badgeClass)
          stateSpan.dataset.bsToggle = "tooltip"
          stateSpan.title = implementation.implementation_status.charAt(0).toUpperCase() + implementation.implementation_status.slice(1)
          const stateIcon = document.createElement("i")
          stateIcon.classList.add("text-reset", ...iconClasses)
          stateSpan.append(stateIcon)
          stateCell.append(stateSpan)
        } else {
          stateCell.innerText = "-"
        }
        implementationRow.append(stateCell)

        const implementationSinceVersionCell = document.createElement("td")
        implementationSinceVersionCell.innerText = implementation.implementation_since ?? "-"
        implementationRow.append(implementationSinceVersionCell)

        const implementedVersionCell = document.createElement("td")
        implementedVersionCell.innerText = implementation.implemented_version ?? "-"
        implementationRow.append(implementedVersionCell)

        tableBody.append(implementationRow)
      }
    }
  }

  initialize_bootstrap_tooltips()
  const implementations_offcanvas = new bootstrap.Offcanvas(
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

function get_user_platform_by_user_agent() {
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

function software_platform_changed(event) {
  const url_params = new URLSearchParams(window.location.search);
  url_params.set("platform", event.target.value);
  history.pushState(null, "", `${window.location.pathname}?${url_params.toString()}`);

  software_filter_list()
}

function software_set_filters() {
  // Software list: Set filters for displaying software

  // Select platform by query parameter or via reported user agent
  const url_params = new URLSearchParams(window.location.search);

  let user_platform = "";
  if(window.location.search) {
    user_platform = url_params.get("platform")
  }

  if (user_platform === "") {
    user_platform = get_user_platform_by_user_agent();
    url_params.set("platform", user_platform);
    history.pushState(null, "", `${window.location.pathname}?${url_params.toString()}`);
  }

  let platform_select = document.getElementById("platform-select");
  if (platform_select) {
    for (const option of platform_select) {
      if (option.value == user_platform) {
        option.setAttribute("selected", true);
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
