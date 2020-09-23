#!/usr/bin/node

'use strict';

const requestMod = require('request');
const requestUrl = process.argv[2];
const fs = require('fs');
requestMod(requestUrl, 'utf-8').pipe(fs.createWriteStream(process.argv[3]));
