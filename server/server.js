const express = require('express')
const path = require('path')
const fs = require('fs');
const { hostname } = require('os');
const app = express()

const host = "localhost"
const port = 3000

app.get('/', function (req, res) {
    //Home
});

app.get('/account/:name/:homeroom/:studentId', function (req, res) {
    //Account
    fs.readFile('data/' + req.params.homeroom + "/" + req.params.name + "-" + req.params.homeroom + "-" + req.params.studentId + ".json", (err, data) => {
        if (err)
            throw err;

        const json = JSON.parse(data);
        const out = {
            "name": json.name,
            "homeroom":  json.homeroom,
            "studentId":  json.studentId,
            "balance": json.balance,
            "isComittee": json.isComittee,
            "jobs": json.jobs
        };
        console.log(out);
        res.json(out);
    });

    
});

app.get('/fines', function (req, res) {
    //Fines
});

app.get('/transactions', function (req, res) {
  //Transactions
});

app.listen(port, () => console.log('Listening on ' + host + ":" + port))