const express = require('express')
const SpotifyWebApi = require('spotify-web-api-node');


const app = express();

app.post('/login', (req, res) => {
    const code = req.body.code
    const spotifyApi = new SpotifyWebApi({
      redirectUri: 'http://localhost:3000',
      clientId: '922b769acc5d47f5952a2da0e4d34f2b',
      clientSecret: '6a5cd3e8d3ea4fefb54b634cadb8baaf'
    })

  spotifyApi
    .authorizationCodeGrant(code)
    .then(data => {
      res.json({
        accessToken: data.body.access_token,
        refreshToken: data.body.refresh_token,
        expiresIn: data.body.expires_in,
      })
    })
    .catch(() => {
      res.sendStatus(400)
    })
})


app.listen(3001);


