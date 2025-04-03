fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json()) // Convertir la réponse en JSON
  .then((data) => {
    const movies = data.results; // Liste des films dans les résultats
    const list = document.querySelector('#list_movies'); // Sélection de l'élément <ul> avec id "list_movies"

    movies.forEach((movie) => {
      const listItem = document.createElement('li'); // Créer un élément <li>
      listItem.textContent = movie.title; // Ajouter le titre du film
      list.appendChild(listItem); // Ajouter <li> à <ul>
    });
  })
  .catch((error) => {
    console.error('Error fetching movies:', error); // Gestion des erreurs
  });

