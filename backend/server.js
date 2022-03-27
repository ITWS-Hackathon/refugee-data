const express = require('express')
const app = express()
const PORT = 3000
const fs = require('fs')
const path = require('path'); 

app.use(express.static('public'));

app.use(express.static(path.join(__dirname, '../frontend/dist/refugeesite'))); 

app.listen(PORT, () => {
  console.log(`Listening on http://localhost:${PORT}`)
});

app.get('/continents', (req, res) => {
    let rawdata = fs.readFileSync('data_continents.json');
    let data = JSON.parse(rawdata);
    console.log("got a get request for continents")
    res.status(200).send(data)
})


app.get('/countries', (req, res) => {
  let rawdata = fs.readFileSync('data_countries.json');
  let data = JSON.parse(rawdata);
  // console.log(data)
  res.status(200).send(data)
})