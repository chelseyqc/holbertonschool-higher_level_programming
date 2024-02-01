document.getElementById('toggle_header').addEventListener('click', function () {
  let header = document.getElementsByTagName('header')[0];
  if (header.className === 'green') {
    header.className = 'red';
  } else {
    header.className = 'green';
  }});
