window.onload = function() {
    // Software list: Select tab for platform reported by user agent
    const platform_buttons = document.querySelectorAll('button[name="platform-button"]');
    const filter_packages = function(os_name) {
      for (const button of platform_buttons) {
        if (button.dataset.platform == os_name) {
          button.click();
        }
      }
    };
    if (platform_buttons) {
      if (navigator.userAgent.indexOf("Android") >= 0) {
        filter_packages("android");
      } else if (navigator.userAgent.indexOf("Linux") >= 0) {
        filter_packages("linux");
      } else if (navigator.userAgent.indexOf("iPhone") >= 0) {
        filter_packages("ios");
      } else if (navigator.userAgent.indexOf("Windows") >= 0) {
        filter_packages("windows");
      } else if (navigator.userAgent.indexOf("Macintosh") >= 0) {
        filter_packages("macos");
      } else {
        filter_packages("other");
      }
    }
};

for (const button of document.querySelectorAll('button[name="platform-button"]')) {
  button.addEventListener("click", function() {
    var platform = button.dataset.platform;
    var cards = document.getElementsByClassName("package-card");
    for (const card of cards) {
      if (platform == "other") {
        // Show all cards
        card.classList.remove("d-none");
        continue;
      }

      var supported_platforms_list = card.querySelector('ul[name="supported_platforms_list"]');
      if (supported_platforms_list.innerHTML.toLowerCase().indexOf(platform) > -1) {
        card.classList.remove("d-none");
      } else {
        card.classList.add("d-none");
      }
    }
  });
} 

function resizeIframe(obj) {
  obj.style.height = obj.contentWindow.document.documentElement.scrollHeight + 20 + 'px';
}
