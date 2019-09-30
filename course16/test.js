'use strict';

function makeid(numberFlag, length) {
    var text = "";
    var possible;

    if (numberFlag) {
        possible = "0123456789";
    } else {
        possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    }


    for( var i=0; i < length; i++ )
        text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
}

var arr = [];
var result = [];

for (var i = 0; i < 50; i++) {
    arr.push(i % 2 ? makeid(true, 3) : makeid(false, 5))
}


for (var i in arr) {
    var item = arr[i]
    result.push(!!Number(item) ? Number(item) : 8)
}

console.log(result)
