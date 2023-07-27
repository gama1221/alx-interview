#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    for (const value of JSON.parse(body).characters) {
      const res = await Makerequest(value);
      console.log(res);
    }
  }
});

function Makerequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) {
        console.log(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}
