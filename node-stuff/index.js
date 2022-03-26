// inlcude express 
const express = require("express");

//googleapis
const { google } = require("googleapis");

//initilize express
const app = express();

//set app view engine
app.set("view engine", "ejs");

app.post("/", async (req, res) => {
    const { request, name } = req.body;
})
