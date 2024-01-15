#!/usr/bin/env ts-node

// Import the required modules
import readline from 'readline';
import crypto from 'crypto';
import { Buffer } from 'buffer';

// Create a readline interface to read user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Prompt the user to enter the IMEI number
rl.question('Enter your IMEI: ', (imei) => {
  // Append the word "simlock" to the IMEI number
  const input = imei + 'simlock';
  // Compute the SHA1 hash of the input
  const hash = crypto.createHash('sha1').update(input).digest('hex');
  // Cut the first eight characters of the hash
  const code = hash.slice(0, 8);
  // Print the code to the standard output
  console.log(code);
  // Close the readline interface
  rl.close();
});
