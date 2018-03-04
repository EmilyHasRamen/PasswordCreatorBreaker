var express = require('express');
var fs = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var app = express();

app.get('/scrape', function(req, res) {

// url below

url = 'https://www.mdbg.net/chinese/dictionary'

request(url, function(error, response, html){

  if)!error){
    
    var $ = cheerio.load(html);
    
    var 

})

exports = module.exports = app;
