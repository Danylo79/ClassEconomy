const express = require('express')
const path = require('path')
const bodyParser = require('body-parser');
const port = 3000
const fs = require('fs');
const app = express()

app.get('/', function (req, res) {
    //Home
});

app.get('/account', function (req, res) {
    //Account
});

app.get('/fines', function (req, res) {
    //Fines
});

app.get('/transactions', function (req, res) {
  //Transactions
});