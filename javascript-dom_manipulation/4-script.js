document.addEventListener('DOMContentLoaded', function() {
  const addItemButton = document.getElementById('add_item');
  const list = document.querySelector('ul');

  addItemButton.addEventListener('click', function() {
    const li = document.createElement('li');
    li.textContent = 'Item';
    list.appendChild(li);
  });
});
