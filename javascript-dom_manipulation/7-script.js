fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then(data => {
    const movieList = document.getElementById('list_movies');
    for (const movie of data.results) {
      const movieElement = document.createElement('li');
      movieElement.textContent = movie.title;
      movieList.appendChild(movieElement);
    }
  });
