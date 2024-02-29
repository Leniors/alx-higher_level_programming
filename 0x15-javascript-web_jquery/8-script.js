$.ajax({
	type: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	success: function (data) {
		const films = data.results;
		films.forEach(element => {
			$('UL#list_movies').append(`<li>${element.title}</li>`);
		});
	}
});
