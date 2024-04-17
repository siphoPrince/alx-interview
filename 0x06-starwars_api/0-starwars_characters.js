#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else if (response.statusCode !== 200) {
        console.error('Status:', response.statusCode);
    } else {
        const film = JSON.parse(body);
        const charactersUrls = film.characters;
        Promise.all(charactersUrls.map(getCharacterName))
            .then(characterNames => {
                characterNames.forEach(name => console.log(name));
            })
            .catch(err => {
                console.error('Error fetching character names:', err);
            });
    }
});

function getCharacterName(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else if (response.statusCode !== 200) {
                reject(`Status ${response.statusCode}`);
            } else {
                const character = JSON.parse(body);
                resolve(character.name);
            }
        });
    });
}
