#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = size; i > 0; i--) {
    let s = '';
    for (let j = size; j > 0; j--) {
      s += 'X';
    }
    console.log(s);
  }
}
