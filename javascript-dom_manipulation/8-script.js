document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => response.json()) // Convertir la réponse en JSON
    .then((data) => {
      document.querySelector('#hello').textContent = data.hello; // Mettre à jour le contenu avec "hello" traduit
    })
    .catch((error) => {
      console.error('Error fetching translation:', error); // Gestion des erreurs
    });
});

