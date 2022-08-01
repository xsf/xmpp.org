window.onload = function() {
    // Software list: Select tab for platform reported by user agent
    const packages_list = document.getElementById("pills-software-content");
    const select_tab = function(os_name) {
      var tab_trigger_element = document.querySelector('#' + os_name+ '-tab');
      if (tab_trigger_element) {
        var tab = new bootstrap.Tab(tab_trigger_element);
        tab.show();
      }
    };
    if (packages_list) {
      if (navigator.userAgent.indexOf("Android") >= 0) {
        select_tab("android");
      } else if (navigator.userAgent.indexOf("Linux") >= 0) {
        select_tab("linux");
      } else if (navigator.userAgent.indexOf("iPhone") >= 0) {
        select_tab("ios");
      } else if (navigator.userAgent.indexOf("Windows") >= 0) {
        select_tab("windows");
      } else if (navigator.userAgent.indexOf("Macintosh") >= 0) {
        select_tab("macos");
      } else {
        select_tab("other");
      }
    }
};
