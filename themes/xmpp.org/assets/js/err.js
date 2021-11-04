var errorEmojiContainer = document.getElementsByClassName('error-emoji')[0];
var emojiArray = [
  '\\(o_o)/', '(o^^)o', '(˚Δ˚)b', '(^-^*)', '(≥o≤)', '(^_^)b', '(·_·)',
  '(=\'X\'=)', '(>_<)', '(;-;)', '\\(^Д^)/',
];
var errorEmoji = emojiArray[Math.floor(Math.random() * emojiArray.length)];
errorEmojiContainer.appendChild(document.createTextNode(errorEmoji));
