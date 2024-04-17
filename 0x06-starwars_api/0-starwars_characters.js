#!/usr/bin/node

const request = require('request');

function getCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
        } else if (response.statusCode !== 200) {
            console.error('Status:', response.statusCode);
        } else {
            const filmData = JSON.parse(body);
            const characters = filmData.characters;

            characters.forEach(characterUrl => {
                request(characterUrl, (error, response, body) => {
                    if (error) {
                        console.error('Error:', error);
                    } else if (response.statusCode !== 200) {
                        console.error('Status:', response.statusCode);
                    } else {
                        const characterData = JSON.parse(body);
                        console.log(characterData.name);
                    }
                });
            });
        }
    });
}

const movieId = process.argv[2];
if (!movieId) {
    console.error('Usage: node 0-starwars_characters.js <movie_id>');
} else {
    getCharacters(movieId);
}
