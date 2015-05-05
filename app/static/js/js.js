// tool function
function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      oldonload();
      func();
    };
  }
}

// tool function
function addClass(element,value) {
  if (!element.className) {
    element.className = value;
  } else {
    newClassName = element.className;
    newClassName+= " ";
    newClassName+= value;
    element.className = newClassName;
  }
}

// 改变所有class名为time_from_now的时间戳标签的内容，转换为距离今年的时间
function timeFromNow() {
  var timestamps = document.getElementsByClassName("time_from_now");
  for (var i = 0; i < timestamps.length; i++) {
    var current_timestamp = timestamps[i];
    var time_from_now = moment(current_timestamp.textContent).fromNow();
    current_timestamp.textContent = time_from_now;
  }
}

// 为当前所在页面的导航标签添加 class="here",便于更改样式
function highlightPage() {
  var navbar = document.getElementsByClassName("navbar");
  // 取得导航链接
  var links = navbar[0].getElementsByTagName("a");
  var linkurl;
  for (var i = 0; i < links.length; i++) {
      // 遍历导航链接，比较当前链接的 URL 与当前页面的 URL。
      linkurl = links[i].getAttribute("href");
      if (window.location.href.indexOf(linkurl) != -1) {
        // window.location.href 用来表示当前页面的网址，
        // indexOf() 函数返回 -1 时，表示字符串不再里面。
        addClass(links[i],"here");
      }
  }
}
addLoadEvent(timeFromNow);
addLoadEvent(highlightPage);
