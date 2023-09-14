#!/usr/bin/node

let x = parseInt(process.argv[2]);
if (x) {
    for(let i = x;i > 0; i--){
        let row ='';
        for(let y = x; y > 0; y--){
            row+='X'
        }
        console.log(row);
    }
    
  } else {
    console.log('Missing size');
  }
  