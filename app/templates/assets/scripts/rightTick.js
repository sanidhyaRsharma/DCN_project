$(document.forms[0]).submit(function(event) {
  event.preventDefault();
  $.get('rightTick.php', function(data) {
    alert('all good');
  });
});
