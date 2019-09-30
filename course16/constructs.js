'use strict';

var x = 1 === 1 ? 'true' : 'false';

var flag = true;

if (!flag) {
    console.log('if');

} else if ((flag && 1 < 2)  || (5 < 3)) { // || - or, && - and.
    console.log('elseif');
} else {
    // do nothing.
}


var ternary = 40 > 13 ? 'yes' : 'no';
console.log(ternary);

var value = '321';

switch (value) {
    case '321':
        console.log('1');
        break;
    case '123':
        console.log('2');
        break;
    default:
        console.log('other');
        break;
}

var i = 42;
console.log(i++); // shows 42
console.log(i); // shows 43
i = 42;
console.log(++i); // shows 43
console.log(i); // shows 43
for (var j = 0; j < 10; j++) {
    for (var i = 0; i < 10; i++) { // ++i, i++
        console.log(i);
    }
}


var iterable = ['a', 'b', 1, 2, 3, 4, 5];
for (var item in iterable) {
    console.log(item, iterable[item]);
}

var iterable = [null, NaN,1, 2, 3, 4, 5];
for (var item of iterable) {   // Not supported in many browsers
    console.log(item);
}

// var i = 0;
var s = 0;

do {
    console.log(++s);  // s++
} while (s < 4);
