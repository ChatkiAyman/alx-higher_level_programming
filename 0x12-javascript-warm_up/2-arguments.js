#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 2) console.log('No argument');
if (argv.length === 3 || argv.length > 3) {
	  console.log('Argument found');
}
