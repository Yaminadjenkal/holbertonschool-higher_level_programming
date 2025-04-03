document.querySelector('#add_item').addEventListener('click', () => {
  const newItem = document.createElement('li'); // Créer un nouvel élément <li>
  newItem.textContent = 'Item'; // Ajouter le texte "Item" à l'élément
  document.querySelector('.my_list').appendChild(newItem); // Ajouter <li> à la liste
});

