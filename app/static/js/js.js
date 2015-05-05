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

// 改变所有class名为time_from_now的时间戳标签的内容，转换为距离今年的时间
function timeFromNow() {
  var timestamps = document.getElementsByClassName("time_from_now");
  for (var i = 0; i < timestamps.length; i++) {
    var current_timestamp = timestamps[i];
    var time_from_now = moment(current_timestamp.textContent).fromNow();
    current_timestamp.textContent = time_from_now;
  }
}

addLoadEvent(timeFromNow);
